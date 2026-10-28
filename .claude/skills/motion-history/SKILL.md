---
name: motion-history
description: ทำคลิปเล่าประวัติศาสตร์บนแผนที่แนวตั้ง 9:16 ภาษาไทย ~1 นาที ด้วยโปรเจค motion-history-starter — วิจัย เขียนบทแบบเล่าเรื่อง ตรวจข้อเท็จจริงอิสระ สร้างแผนที่ ภาพ เสียง และเรนเดอร์ ใช้เมื่อผู้ใช้พูดว่า "ทำคลิปประวัติศาสตร์", "เล่าประวัติศาสตร์บนแผนที่", "motion history" หรือให้หัวข้อประวัติศาสตร์ที่มีสถานที่/เส้นทาง
---

# motion-history

1. อ่าน `README.md`, `docs/STORY-RULES.md`, `docs/CUES.md` และตัวอย่าง `topics/015-pearl-harbor/script.py`
2. สร้าง `topics/<NNN-slug>/` แล้วเขียนบทตาม `prompts/BRIEF-WRITER.md` (ใช้เอเจนต์ย่อยได้)
3. ตรวจข้อเท็จจริงด้วยเอเจนต์อีกตัวตาม `prompts/BRIEF-CHECKER.md` — ห้ามข้าม (พากย์ใหม่เสียเงิน)
4. ใส่ `COVER` ใน script.py (ดูตัวอย่าง) แล้ว `./make.sh <NNN-slug>` → `renders/<NNN-slug>-final.mp4` (มีปก) — ยังไม่ติดตั้ง ให้รัน `./setup.sh` ก่อน
5. QA: `ffmpeg -i renders/<slug>.mp4 -vf "fps=1/2.5,scale=180:-2,tile=8x3" -frames:v 1 qa.jpg` แล้วเปิดดูภาพ เช็กซับล้นจอ ตัวละครหลุดเฟรม สีพื้นทึบ ช็อตว่าง
6. แก้แล้วเรนเดอร์ใหม่จากขั้น `build` (เสียงใช้แคชถ้าไม่แก้คำพากย์)
