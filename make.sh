#!/bin/bash
# ผลิต 1 เรื่องครบ: ./make.sh <NNN-slug> [ขั้นเริ่ม: map|assets|build|mix|render]
#   map    = แผนที่ดาวเทียม + เขตแดน (ฟรี)
#   assets = ภาพตัวละคร + ฉากจำลอง (OpenRouter ~3–4 บาท/ภาพ)
#   build  = เสียงพากย์ ElevenLabs + timeline (ใช้เครดิตเสียงตามจำนวนตัวอักษร)
#   mix    = ดนตรี + เสียงเอฟเฟกต์
#   render = เรนเดอร์ MP4 ด้วย HyperFrames ในเครื่อง → renders/<slug>.mp4
set -e
cd "$(dirname "$0")"; S=${1%/}; S=${S#topics/}; T="$PWD/topics/$S"; FROM=${2:-map}
[ -f "$T/script.py" ] || { echo "ไม่พบ $T/script.py"; exit 1; }
mkdir -p renders; on=0
for st in map assets build mix render; do [ "$st" = "$FROM" ] && on=1; [ $on = 1 ] || continue
  echo "── $st"
  case $st in
    map) python3 tools/mapgen.py "$T" ;;
    assets) python3 tools/assets.py "$T" ;;
    build) python3 build.py "$T" ;;
    mix) python3 mix.py "$T" ;;
    render) (cd "$T" && npx -y hyperframes render --quality standard --output "$PWD/../../renders/$S.mp4") ;;
  esac
done
echo "เสร็จ: renders/$S.mp4"
