#!/usr/bin/env python3
"""topics/<slug>/script.py -> พากย์ (ElevenLabs with-timestamps) + timeline.js + index.html + sprites
   python3 build.py topics/<slug>"""
import json, os, re, sys, base64, shutil, subprocess, urllib.request, hashlib, runpy
from config import CHANNEL, key

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.abspath(sys.argv[1]); A = os.path.join(T, "assets"); os.makedirs(A, exist_ok=True)
cfg = runpy.run_path(os.path.join(T, "script.py"))
LINES, VOICE, MODEL = cfg["LINES"], cfg["VOICE"], cfg.get("MODEL", "eleven_v4")
KEY = key("ELEVENLABS_API_KEY")

says = [say or re.sub(r"[{}]", "", show) for show, say, _ in LINES]
text = " ".join(says)
cache = os.path.join(A, "tts_" + hashlib.md5((VOICE + MODEL + text).encode()).hexdigest()[:10] + ".json")
if not os.path.exists(cache):  # ponytail: cache by text hash — edit text = new TTS call (costs quota)
    body = json.dumps({"text": text, "model_id": MODEL,
                       "voice_settings": {"stability": 0.4, "similarity_boost": 0.8, "speed": 1.1}}).encode()
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps",
                                 body, {"xi-api-key": KEY, "content-type": "application/json"})
    data = urllib.request.urlopen(req, timeout=600).read().decode()
    open(cache, "w").write(data)
d = json.load(open(cache))
open(os.path.join(T, "voice.mp3"), "wb").write(base64.b64decode(d["audio_base64"]))
al = d["alignment"]; starts = al["character_start_times_seconds"]
assert "".join(al["characters"]) == text, "alignment text mismatch"
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", os.path.join(T, "voice.mp3")]))
out, pos = [], 0
for (show, _, cues), say in zip(LINES, says):
    out.append({"t": round(starts[pos], 3), "show": show, "cues": cues}); pos += len(say) + 1
for a, b in zip(out, out[1:] + [None]):
    a["end"] = b["t"] if b else round(dur, 3)
D = round(dur + 0.6, 3)
open(os.path.join(T, "timeline.js"), "w").write("window.TL = " + json.dumps({"duration": D, "channel": cfg.get("CHANNEL", CHANNEL), "style": cfg.get("STYLE", ""), "lines": out}, ensure_ascii=False, indent=1) + ";")
html = open(os.path.join(HERE, "engine", "index.html")).read()  # read before write: never open(...,"w") the same file first
open(os.path.join(T, "index.html"), "w").write(re.sub(r'data-duration="[\d.]+"', f'data-duration="{D}"', html))
for f in os.listdir(os.path.join(HERE, "engine", "sprites")):
    shutil.copy(os.path.join(HERE, "engine", "sprites", f), A)
print(f"{os.path.basename(T)}: voice {dur:.1f}s · {len(out)} lines · {len(text)} chars")
