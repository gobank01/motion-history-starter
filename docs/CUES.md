# คิวภาพ (เขียนในช่องที่ 3 ของแต่ละบรรทัดใน LINES) — ทุกคิวเริ่มพร้อมบรรทัดนั้น

## กล้อง / แผนที่
| คิว | ทำอะไร |
|---|---|
| `cam lon lat span [dur]` | เลื่อนกล้อง (span = องศาลองจิจูดที่เห็นทั้งจอ ยิ่งน้อยยิ่งใกล้) |
| `whip lon lat span` | ซูมเร็วแบบเบลอ |
| `show key [สี]` / `hide key` | แสดง/ซ่อนพื้นที่ใน REGIONS · `recolor key สี` · `pulse key` (ขอบกะพริบ) |
| `river key` | วาดแม่น้ำจาก LINES_GEO |
| สี | red blue orange purple green grey gold teal |

## หมุด ข้อความ เส้นทาง
| คิว | ทำอะไร |
|---|---|
| `pin id lon lat` · `label id lon lat ข้อความ` · `pill id lon lat ข้อความ` · `ring id lon lat rpx` · `icon id lon lat 🐘` | หมุด/ป้าย/ป้ายแดง/วงกลม/ไอคอน |
| `arrow id lon,lat lon,lat ...` | ลูกศรแดง |
| `route id dur lon,lat ...` | เส้นทางเรืองแสงค่อยๆ วาด · `band id สี กว้างpx dur ...` แถบหนาแบบ Minard · `dash id ...` เส้นประวิ่ง |
| `wave lon lat km dur` | คลื่นแผ่ (ระเบิด/แผ่นดินไหว) |

## ตัวละคร
| คิว | ทำอะไร |
|---|---|
| `sprite id ชื่อtoken lon lat สูงpx` | วางตัวละครจาก TOKENS (มาสคอต: `sprite mascot point|stand|map_pose lon lat 300`) |
| `walk id dur lon,lat ...` | เดินโยกตัวตามเส้นทาง หันหน้าตามทิศเอง |
| `sail id dur lon,lat ...` | เรือ/เครื่องบินโคลงเบาๆ ตามเส้นทาง |
| `move id lon lat dur` · `follow id dur lon,lat ...` | เลื่อนเฉยๆ |

## จอ / เอฟเฟกต์
| คิว | ทำอะไร |
|---|---|
| `title บน|คำเด่น|ล่าง` | ฮุกคำถามตัวใหญ่กลางจอ (บรรทัดนั้นไม่ขึ้นซับ) |
| `chapter 1 ชื่อบท` | ป้ายบทสีส้มด้านบน (`chapter -` ซ่อน) |
| `card หัวเล็ก|ข้อความใหญ่|บรรทัดเล็ก` | การ์ดข้อมูล · `big ตัวเลข|หน่วย` ตัวเลขยักษ์ |
| `bars ป้าย:ค่า:สี ...` | กราฟแท่งนับเลขขึ้น (ป้ายใช้ _ แทนช่องว่าง) |
| `scene ชื่อ [rain]` / `endscene` | ฉากจำลองเต็มจอจาก SCENES |
| `flash` · `shake [วิ]` | แสงวาบ · จอสั่น |
| `recap ข้อความ` | การ์ด "สรุป" ติ๊กทีละข้อ |
| `source ข้อความ` | ที่มาตัวเล็กด้านล่าง |
| `outro ชื่อเรื่อง|บรรทัดรอง` | การ์ดปิดท้ายสีทอง |
| `sfx ชื่อ` | whoosh boom pop cannon tick coin waves wind march rumble bell fire horse plane splash alarm gasp steps riser chime |
| `clear` | ล้างหมุด/เส้น/ตัวละครบนจอ |

## ใน script.py
- `STYLE = "muted"` แผนที่โทนหม่นนูน (เหมาะเรื่องอาณาเขต/สงคราม) · ไม่ใส่ = ภาพดาวเทียมสด
- `MAP = dict(lon0, lon1, lat0, lat1, ppd)` ppd 240 ระดับประเทศ · 120 ภูมิภาค · 60 ทวีป (W,H ≤ 9000 และ H ≥ 1920)
- `MAP[...]["hires"] = dict(lon0, lon1, lat0, lat1, ppd)` ภาพ Sentinel-2 ละเอียดสำหรับซูมระดับเมือง (เพิ่ม `shade=True` ถ้าเป็นภูเขาหิมะ)
- `REGIONS = [("key", "สี", dict(adm0=["THA"], adm1={"LAO": "*"}, poly=[[(lon,lat),...]]))]`
- `TOKENS = [("ชื่อ", "คำบรรยาย chibi ภาษาอังกฤษ ... full body side view facing right")]` · `SCENES = {"ชื่อ": "prompt ฉาก"}`
- `LINES = [("ซับ {คำเหลือง}", "คำพากย์ถ้าต่างจากซับ (ตัวเลขเป็นคำไทย)" หรือ None, ["คิว", ...])]`
- แผนที่ข้ามเส้นวันที่: ใช้ลองจิจูดต่อเนื่อง (เช่น เอเชีย = E − 360) ดูตัวอย่าง topics/015-pearl-harbor
