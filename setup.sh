#!/bin/bash
# ติดตั้งครั้งเดียวหลัง git clone: ./setup.sh
# ตรวจ/ลงโปรแกรมที่ต้องใช้ (Homebrew) · สร้าง .venv + ไลบรารี Python · สร้าง .env ให้ใส่คีย์
set -e
cd "$(dirname "$0")"
ok() { echo "  ✅ $1"; }; bad() { echo "  ❌ $1"; FAIL=1; }; FAIL=0

echo "── ตรวจเครื่อง"
[ "$(uname)" = "Darwin" ] && ok "macOS" || bad "ต้องใช้ macOS (ขั้นตัดพื้นหลังตัวละครใช้ Vision ของ Apple)"
if ! command -v brew >/dev/null; then
  bad "ยังไม่มี Homebrew — ลงก่อนด้วยคำสั่งในหน้า https://brew.sh แล้วรัน ./setup.sh อีกครั้ง"; exit 1
fi
ok "Homebrew"

need=()
command -v python3 >/dev/null || need+=(python)
command -v ffmpeg >/dev/null || need+=(ffmpeg)
NODE_MAJOR=$(node -v 2>/dev/null | sed 's/^v//; s/\..*//'); [ "${NODE_MAJOR:-0}" -ge 22 ] || need+=(node)
if [ ${#need[@]} -gt 0 ]; then
  echo "── ลง ${need[*]} ผ่าน Homebrew"; brew install "${need[@]}"
  [[ " ${need[*]} " == *" node "* ]] && brew link --overwrite node >/dev/null 2>&1 || true
fi
NODE_MAJOR=$(node -v 2>/dev/null | sed 's/^v//; s/\..*//')
[ "${NODE_MAJOR:-0}" -ge 22 ] && ok "Node.js $(node -v)" || bad "Node.js ต้อง 22 ขึ้นไป (ตอนนี้ $(node -v 2>/dev/null || echo ไม่มี)) — ลอง brew upgrade node"
command -v ffmpeg >/dev/null && ok "ffmpeg" || bad "ffmpeg"
if command -v swift >/dev/null; then ok "swift (Xcode Command Line Tools)"
else bad "ยังไม่มี Xcode Command Line Tools — รัน xcode-select --install กดติดตั้งให้เสร็จ แล้วรัน ./setup.sh อีกครั้ง"; fi

echo "── ไลบรารี Python (.venv)"
[ -x .venv/bin/python ] || python3 -m venv .venv
.venv/bin/python -m pip install -q --upgrade pip
.venv/bin/python -m pip install -q -r requirements.txt && ok "numpy · pillow · pyshp"

echo "── คีย์"
[ -f .env ] || { cp .env.example .env; echo "  สร้างไฟล์ .env แล้ว"; }
for k in ELEVENLABS_API_KEY OPENROUTER_API_KEY; do
  v=$(grep "^$k=" .env | cut -d= -f2- | sed 's/#.*//; s/[[:space:]]//g')
  [ -n "$v" ] && ok "$k" || bad "$k ยังว่าง — เปิดไฟล์ .env (open -e .env) ใส่คีย์หลังเครื่องหมาย ="
done
chmod +x make.sh

echo
if [ $FAIL = 0 ]; then echo "พร้อมทำคลิป ✅  ลองเลย: ./make.sh 029-champa"
else echo "ยังไม่พร้อม — แก้ข้อที่มี ❌ ด้านบน แล้วรัน ./setup.sh ซ้ำได้ (ไม่เสียอะไร)"; exit 1; fi
