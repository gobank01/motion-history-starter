#!/bin/bash
# ผลิต 1 เรื่องครบ: ./make.sh <NNN-slug> [ขั้นเริ่ม: map|assets|build|mix|render|cover]
#   map    = แผนที่ดาวเทียม + เขตแดน (ฟรี)
#   assets = ภาพตัวละคร + ฉากจำลอง (OpenRouter ~3–4 บาท/ภาพ)
#   build  = เสียงพากย์ ElevenLabs + timeline (ใช้เครดิตเสียงตามจำนวนตัวอักษร)
#   mix    = ดนตรี + เสียงเอฟเฟกต์
#   render = เรนเดอร์ MP4 ด้วย HyperFrames ในเครื่อง → renders/<slug>.mp4
#   cover  = ปกจาก COVER ใน script.py → renders/<slug>-cover.png + renders/<slug>-final.mp4 (ปกเป็นเฟรมแรก)
set -e
cd "$(dirname "$0")"; S=${1%/}; S=${S#topics/}; T="$PWD/topics/$S"; FROM=${2:-map}
[ -n "$1" ] || { echo "ใช้: ./make.sh <ชื่อโฟลเดอร์ใน topics/>  เช่น ./make.sh 029-champa"; ls topics; exit 1; }
[ -f "$T/script.py" ] || { echo "ไม่พบ $T/script.py"; exit 1; }
PY=python3; [ -x .venv/bin/python ] && PY="$PWD/.venv/bin/python"
"$PY" -c "import numpy, PIL, shapefile" 2>/dev/null || { echo "ยังไม่ได้ติดตั้ง — รัน ./setup.sh ก่อน"; exit 1; }
mkdir -p renders; on=0
for st in map assets build mix render cover; do [ "$st" = "$FROM" ] && on=1; [ $on = 1 ] || continue
  echo "── $st"
  case $st in
    map) "$PY" tools/mapgen.py "$T" ;;
    assets) "$PY" tools/assets.py "$T" ;;
    build) "$PY" build.py "$T" ;;
    mix) "$PY" mix.py "$T" ;;
    render) (cd "$T" && npx -y hyperframes render --quality standard --output "$PWD/../../renders/$S.mp4") ;;
    cover) "$PY" tools/cover.py "$T" ;;
  esac
done
[ -f "renders/$S-final.mp4" ] && echo "เสร็จ: renders/$S-final.mp4 (มีปก) · ปก renders/$S-cover.png" || echo "เสร็จ: renders/$S.mp4"
