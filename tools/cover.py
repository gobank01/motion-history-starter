#!/usr/bin/env python3
"""ปก 9:16 ต่อเรื่อง (OpenRouter Gemini image) + ฝังเป็นเฟรมแรก 0.1 วิ ให้แพลตฟอร์มเลือกเป็นปก
   python3 tools/cover.py topics/<slug>   → renders/<slug>-cover.png + renders/<slug>-final.mp4
   อ่าน COVER ใน script.py: ("บรรทัดใหญ่", "บรรทัดรอง", "scene prompt (EN)", ["token.png", "scene_x.png"])
   ไม่มี COVER = ข้าม · มีปกแล้วจะไม่สร้างใหม่ (ลบไฟล์ -cover.png ถ้าอยากได้ปกใหม่)"""
import os, sys, runpy, subprocess
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.abspath(sys.argv[1]); S = os.path.basename(T.rstrip("/")); R = os.path.join(HERE, "renders")
cfg = runpy.run_path(os.path.join(T, "script.py"))
if "COVER" not in cfg: sys.exit(print(f"{S}: ไม่มี COVER ใน script.py — ข้ามปก"))
big, sub, scene, refs = cfg["COVER"]
png, mp4, final = os.path.join(R, f"{S}-cover.png"), os.path.join(R, f"{S}.mp4"), os.path.join(R, f"{S}-final.mp4")

if not os.path.exists(png):
    p = (f"Vertical 9:16 YouTube-Shorts/Reels cover for a Thai history channel, high click-through style. "
         f"Art: cute modern chibi illustration matching the attached references (thick dark-brown outlines, soft cel shading) "
         f"over a vivid satellite-map background (deep blue ocean, green land, the key area glowing). Scene: {scene}. "
         f"Text (Thai, spelled EXACTLY, huge, ultra-bold rounded Thai font, thick black outline, slight drop shadow): "
         f"line 1 \"{big}\" in bright yellow #FFD21F, very large; line 2 \"{sub}\" in white with the key word in red #E8343F, slightly smaller. "
         f"Place the text in the upper-middle area. Keep every important element inside the central 3:4 safe area and leave the bottom 15% "
         f"free of text and faces. One small red circle or arrow highlighting the key detail. No other text, no logos, no watermark.")
    pf = png + ".txt"; open(pf, "w").write(p)
    ref = [os.path.join(T, "assets", r) for r in refs if os.path.exists(os.path.join(T, "assets", r))]
    subprocess.run([sys.executable, os.path.join(HERE, "tools", "img.py"), pf, png, "9:16"] + ref, check=True)
    os.remove(pf)
print("ปก:", png)

if os.path.exists(mp4):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp4, "-loop", "1", "-i", png, "-filter_complex",
                    "[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[c];"
                    "[0:v][c]overlay=enable='lt(t,0.1)':shortest=1[v]",
                    "-map", "[v]", "-map", "0:a", "-c:v", "libx264", "-crf", "18", "-preset", "fast", "-c:a", "copy", final], check=True)
    print("คลิปพร้อมโพสต์ (ปกเป็นเฟรมแรก):", final)
