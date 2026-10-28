# ค่ากลางของช่อง — แก้ที่นี่ที่เดียว
import os
CHANNEL = "ช่องของฉัน"   # ชื่อที่ขึ้นมุมขวาบนของคลิป (เปลี่ยนเป็นชื่อช่องคุณ)
HERE = os.path.dirname(os.path.abspath(__file__))

def key(name):
    """อ่านคีย์จาก environment ก่อน แล้วค่อยหาในไฟล์ .env ที่รากโปรเจค"""
    if os.environ.get(name): return os.environ[name]
    env = os.path.join(HERE, ".env")
    if os.path.exists(env):
        for l in open(env):
            if l.startswith(name + "="):
                v = l.split("=", 1)[1].split("#", 1)[0].strip().strip("'\"")  # ตัดคอมเมนต์ท้ายบรรทัด
                if v: return v
    raise SystemExit(f"ไม่พบ {name} — ก๊อป .env.example เป็น .env แล้วใส่คีย์ของคุณ")
