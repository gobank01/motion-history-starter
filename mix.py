#!/usr/bin/env python3
"""topics/<slug>: voice.mp3 + ดนตรี (ตาม MUSIC ใน script.py) + SFX ตามคิว `sfx` -> audio.wav
   SFX/ดนตรีเก็บกลางที่ assets/audio ใช้ซ้ำทุกเรื่อง"""
import json, os, re, sys, runpy, subprocess, urllib.request, urllib.error
from config import key

T = os.path.abspath(sys.argv[1])
A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "audio")
os.makedirs(A, exist_ok=True)
KEY = key("ELEVENLABS_API_KEY")
TL = json.loads(re.sub(r"^window\.TL = |;$", "", open(os.path.join(T, "timeline.js")).read().strip()))
MOOD = runpy.run_path(os.path.join(T, "script.py")).get("MUSIC", "tense")
DUR = TL["duration"]

SFX = {  # name: (prompt, seconds)
    "whoosh": ("fast cinematic whoosh swipe, airy, short", 0.8),
    "boom": ("deep cinematic impact hit with sub bass boom, documentary title hit", 1.6),
    "pop": ("soft UI pop bubble click, light and friendly", 0.5),
    "cannon": ("distant 19th century naval cannon fire, two booms with echo over water", 2.5),
    "tick": ("clock ticking fast, tense, four ticks", 1.6),
    "coin": ("pile of silver coins clinking and pouring", 1.5),
    "waves": ("ocean waves crashing against a wooden ship hull, creaking timber", 3.0),
    "wind": ("howling icy polar wind gust", 3.0),
    "march": ("many soldiers marching footsteps on dirt road, distant", 3.0),
    "rumble": ("massive volcanic eruption explosion rumble with deep sub bass", 3.0),
    "bell": ("single ship bell ring, distant", 1.5),
    "fire": ("big fire roaring and crackling, burning wooden city", 3.0),
    "horse": ("many horses galloping on open steppe, thundering hooves", 3.0),
    "plane": ("old propeller airplane engine flying past", 3.0),
    "splash": ("heavy splash into water", 1.2),
    "alarm": ("old air raid siren wailing, distant", 3.0),
    "gasp": ("crowd gasping in shock", 1.5),
    "steps": ("footsteps walking on gravel, light and quick", 2.0),
    "riser": ("cinematic tension riser building up, short", 2.0),
    "chime": ("magical soft chime sparkle, ending flourish", 1.5),
}

def post(path, body, out):
    if os.path.exists(out): return
    req = urllib.request.Request("https://api.elevenlabs.io" + path, json.dumps(body).encode(),
                                 {"xi-api-key": KEY, "content-type": "application/json"})
    for attempt in range(8):  # ElevenLabs answers 429 system_busy under load
        try: data = urllib.request.urlopen(req, timeout=600).read(); break
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 7: raise SystemExit(f"{path} {e.code}: {e.read()[:300]}")
            import time; time.sleep(20 * (attempt + 1))
    open(out, "wb").write(data)

for n, (p, s) in SFX.items():
    post("/v1/sound-generation", {"text": p, "duration_seconds": s, "prompt_influence": 0.5}, f"{A}/{n}.mp3")
MOODS = {  # one 150s bed per mood, shared by every topic
    "tense": "tense cinematic documentary underscore, low strings ostinato, soft taiko pulses, no vocals, steady, builds slightly",
    "adventure": "cinematic adventure documentary underscore, rolling strings and horns, sense of voyage and discovery, no vocals, steady",
    "somber": "somber reflective documentary underscore, solo piano and soft strings, respectful, no vocals, slow",
    "epic": "epic historical war documentary underscore, deep drums and choir-like pads without words, no vocals, building",
    "wonder": "mysterious awe documentary underscore, shimmering pads, deep rumble, slow pulse, no vocals",
}
post("/v1/music", {"prompt": MOODS[MOOD], "music_length_ms": 150000}, f"{A}/music_{MOOD}.mp3")

cues = [(l["t"], c.split()[1]) for l in TL["lines"] for c in l["cues"] if c.startswith("sfx ")]
inputs = ["-i", os.path.join(T, "voice.mp3"), "-stream_loop", "-1", "-i", f"{A}/music_{MOOD}.mp3"]
parts = ["[0:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=1.0[v]",
         f"[1:a]aformat=sample_rates=48000:channel_layouts=stereo,volume=0.13,afade=t=out:st={DUR - 2}:d=2[m]"]
vol = {"whoosh": .45, "boom": .7, "pop": .35, "cannon": .6, "tick": .5, "coin": .5, "waves": .45, "wind": .45, "march": .5, "rumble": .7, "bell": .4,
       "fire": .5, "horse": .5, "plane": .5, "splash": .5, "alarm": .4, "gasp": .45, "steps": .45, "riser": .45, "chime": .45}
for i, (t, n) in enumerate(cues):
    inputs += ["-i", f"{A}/{n}.mp3"]
    ms = int(max(t - (0.15 if n == "whoosh" else 0), 0) * 1000)
    parts.append(f"[{i + 2}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={vol[n]},adelay={ms}|{ms}[s{i}]")
mixin = "[v][m]" + "".join(f"[s{i}]" for i in range(len(cues)))
parts.append(f"{mixin}amix=inputs={len(cues) + 2}:normalize=0:duration=first,apad=whole_dur={DUR},alimiter=limit=0.95[out]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(parts), "-map", "[out]",
                "-t", str(DUR), os.path.join(T, "audio.wav")], check=True)
print(f"audio.wav {DUR}s · {len(cues)} sfx")
