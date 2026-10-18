# 015v3 เพิร์ลฮาร์เบอร์ (เล่าเรื่องแบบ STORY-RULES v3: เหตุ→แผน→ปม→ผลพลิก)
# คำถามเดียว: ทำไมญี่ปุ่นถึงกล้าตีอเมริกา แล้วทำไมชนะวันนั้นแต่แพ้ทั้งเกม?
# เพิ่มข้อเท็จจริง: ญี่ปุ่นนำเข้าน้ำมันส่วนใหญ่จากสหรัฐ (~80%) · ก.ค.–ส.ค. 1941 สหรัฐอายัดทรัพย์+ตัดน้ำมัน · น้ำมันสำรองราวปีครึ่ง–2 ปี
#   · เป้าหมายคือบ่อน้ำมันหมู่เกาะอินเดียตะวันออกของดัตช์ (อินโดนีเซีย) · ผู้วางแผน ยามาโมโตะ อิโซโรกุ
#   · เรดาร์โอพานา: พลทหาร Joseph Lockard + George Elliott · ร.ท. Kermit Tyler ตอบ "ไม่ต้องห่วง" (คิดว่าเป็น B-17 ที่จะมาจากแผ่นดินใหญ่)
#   · มิดเวย์ มิ.ย. 1942 ญี่ปุ่นเสียเรือบรรทุกเครื่องบิน 4 ลำ (อากางิ คางะ โซริว ฮิริว) = 4 ใน 6 ลำที่มาเพิร์ลฮาร์เบอร์
# 015 เพิร์ลฮาร์เบอร์ 7 ธ.ค. 1941 — กองเรือแล่นลับ เรดาร์ที่ถูกมองข้าม เรือบรรทุกเครื่องบินที่ไม่อยู่ในท่า
# แหล่งหลัก: en.wikipedia "Attack on Pearl Harbor" (+อ้างอิง Prange, Zimm, NHHC) · The National WWII Museum
#   "Kermit Tyler: A Call That Would Live in Infamy" · aviation.hawaii.gov "December 7, 1941" · AWM (Kota Bharu 8 Dec 1941)
#   · en.wikipedia "Battle of Kota Bharu" / "Japanese invasion of Thailand"
# เลี่ยง/ระวัง:
#   - "รูสเวลต์รู้ล่วงหน้าแล้วปล่อยให้โดน" = ทฤษฎีสมคบคิด ไม่มีหลักฐาน → ไม่พูดถึง
#   - วาทะยามาโมโตะ "ปลุกยักษ์หลับ" มาจากหนัง Tora! Tora! Tora! ไม่มีหลักฐานว่าพูดจริง → ไม่ใช้
#   - ระยะเส้นทางไม่มีตัวเลขทางการ (คำนวณเองได้ ~5,600–6,000 กม.) → ผู้ตรวจอิสระเปลี่ยนเป็น "หลายพันกิโลเมตร"
#   - เวลาเรดาร์: จับได้ ~07:02 · โทรแจ้ง ~07:15–07:20 · ระยะ 132 ไมล์ (บางแหล่ง 136 ไมล์ทะเล) → 7:02→7:48 (Wikipedia) = 46 นาที / →7:55 (NWWII Museum) = 53 นาที → บทใช้ "กว่า 45 นาที"
#   - ลำดับเวลามลายู vs ฮาวาย: โกตาบารูขึ้นบกก่อนเพิร์ลฮาร์เบอร์ราว 40–60 นาที (แหล่งไม่ตรงกัน) → บทใช้ "ตอนนั้น (ก่อนสหรัฐประกาศสงคราม) ขึ้นบกมลายูแล้ว" + "ภาคใต้ไทย เช้ามืด 8 ธ.ค."
#   - ไม่ภาพโหด: ไม่มีภาพเรือไฟลุก/ศพ ใช้ sail/plane/ไอคอน · ตัวเลขผู้เสียชีวิตแสดงแบบการ์ดเงียบ ไม่มี flash ซ้ำ
#   - แผนที่ใช้ลองจิจูดต่อเนื่องฝั่งลบ: เอเชีย = lon(E) − 360 (เช่น กรุงเทพฯ 100.5E → -259.5) เพื่อให้ hires โออาฮูใช้พิกัดจริง
TITLE = "เพิร์ลฮาร์เบอร์"
HOOK = "เรดาร์เห็นแล้ว แต่ไม่มีใครเชื่อ"
STYLE = "muted"
STYLE_WHY = "เรื่องสงคราม/การเมืองระหว่างประเทศ → แผนที่หม่นนูนให้สีญี่ปุ่น-ฮาวาย-ไทยเรืองแสงเด่น"
VOICE = "tAV9ucNkXgK2k9TLxWkM"
MODEL = "eleven_v4"
MUSIC = "tense"
# W = 112*80*cos(8°) ≈ 8873 · H = 104*80 = 8320 · span สูงสุด ≈ 104*0.5625/0.99 ≈ 59° (พอเห็นคูริล→ฮาวายทั้งเส้น)
# hires โออาฮู 0.75*4000*0.990 ≈ 2970 x 2200
MAP = dict(lon0=-262, lon1=-150, lat0=-44, lat1=60, ppd=80,
           hires=dict(lon0=-158.35, lon1=-157.60, lat0=21.20, lat1=21.75, ppd=4000))
REGIONS = [
    ("japan", "red", dict(adm0=["JPN"])),
    ("hawaii", "blue", dict(adm1={"USA": ["Hawaii"]})),
    ("thai", "gold", dict(adm0=["THA"])),
    ("dei", "purple", dict(adm0=["IDN"])),
    ("malaya", "orange", dict(adm0=["SGP"], adm1={"MYS": "*"}, adm1_not={"MYS": ["Sabah", "Sarawak", "Labuan"]})),
]
TOKENS = [
    ("carrier", "a cute chibi 1941 Japanese navy aircraft carrier with a flat grey flight deck, small island tower, a few tiny planes parked on deck, "
                "calm sea spray, no weapons firing, full body side view facing right"),
    ("plane", "a cute chibi 1941 Japanese navy carrier plane, light grey body with red circle insignia, spinning propeller, "
              "no bombs or guns firing, full body side view facing right"),
    ("uscv", "a cute chibi 1941 US Navy aircraft carrier, dark blue-grey hull, flat flight deck with tiny planes, small US flag, "
             "full body side view facing right"),
    ("radarman", "a cute chibi 1941 US Army young private radar operator in olive uniform with headphones, holding a telephone, "
                 "surprised curious face, full body side view facing right"),
]
SCENES = {
    "radar": "early morning 7 a.m. on a green hilltop on the north tip of Oahu, Hawaii, 1941; a small olive army radar truck and antenna, "
             "two chibi young US Army privates inside looking at a round green oscilloscope screen showing one very large bright blip, "
             "one of them talking on a field telephone, calm pink sunrise over the Pacific, tense but peaceful, no planes attacking, not violent",
    "memorial": "present day, the white USS Arizona Memorial building spanning over calm turquoise water in Pearl Harbor, Hawaii, "
                "a faint outline of the sunken ship hull under the clear water, a small US flag on a pole, chibi visitors in a small "
                "white ferry boat quietly looking, flower lei floating on the water, peaceful respectful mood, bright morning",
}
# พิกัด (ลองจิจูดต่อเนื่อง: ตะวันออก = E − 360)
HITO = "-212.33 44.97"           # อ่าวฮิโตกัปปุ (อ่าวคาซัตกา 44.965N 147.672E) เกาะเอโตโรฟุ หมู่เกาะคูริล
PEARL = "-157.95 21.35"          # เพิร์ลฮาร์เบอร์
OPANA = "-158.03 21.68"          # สถานีเรดาร์โอพานา ใกล้แหลมคาฮูกู
TOKYO = "-220.31 35.69"
BKK = "-259.50 13.75"
SONGKHLA = "-259.41 7.19"
PATTANI = "-258.75 6.87"
KOTABHARU = "-257.75 6.13"
MIDWAY = "-177.37 28.21"
# เส้นทางกองเรือ (โดยประมาณ): ออกตะวันออกตามแนว ~42–43°N → เติมน้ำมันแถว 170°W → ลงใต้ถึงจุดปล่อยเครื่องบิน ~26°N 158°W
KB = "-212.33,44.97 -205,43.6 -197,42.6 -190,42.0 -180,39.5 -170,35.0 -162,29.5 -158.2,26.6"
STRIKE = "-158.2,26.6 -158.15,24.0 -158.05,22.2 -157.95,21.4"
ENT = "-166.0,19.6 -163.0,20.4 -160.5,21.0"   # เรือบรรทุกเครื่องบินสหรัฐที่ยังอยู่กลางทะเล (สัญลักษณ์ ไม่ใช่ตำแหน่งแม่นยำ)
INV = ["arrow sg -255.5,9.6 -259.25,7.30", "arrow pt -255.0,9.0 -258.65,6.95", "arrow kb -254.5,8.4 -257.70,6.25"]

LINES = [
    ("เช้าวันอาทิตย์ {เรดาร์เห็นฝูงเครื่องบิน}", None,
     ["cam -158.0 21.5 1.2 0", "title เรดาร์เห็นแล้ว|แต่ไม่มีใครเชื่อ|เกิดอะไรขึ้น?", "show hawaii", "sprite rm radarman -158.25 21.62 190",
      "icon ic1 " + OPANA + " 📡", "flash", "sfx alarm"]),
    ("แต่{ไม่มีใครเชื่อ}", None, ["pulse hawaii", "sfx gasp"]),
    ("ปี 1941 {ญี่ปุ่นรบอยู่ในจีน}", "ปีหนึ่งเก้าสี่หนึ่ง ญี่ปุ่นรบอยู่ในจีน",
     ["clear", "chapter 1 ทางตัน", "cam -215 25 50 1.4", "show japan", "arrow cn -220,36 -240,33",
      "source Wikipedia (Attack on Pearl Harbor) · National WWII Museum", "sfx march"]),
    ("แต่น้ำมัน{ส่วนใหญ่ซื้อจากอเมริกา}", None, ["icon oil -205 33 🛢️", "arrow oil -152,38 -205,35", "sfx coin"]),
    ("จนอเมริกา{ตัดน้ำมัน}", None,
     ["card ก.ค.–ส.ค. 1941|อเมริกาตัดน้ำมัน|ญี่ปุ่นมีน้ำมันสำรองราว 1.5–2 ปี", "shake .4", "sfx boom"]),
    ("ญี่ปุ่นเลยต้อง{ยึดบ่อน้ำมันอินโดนีเซีย}", None,
     ["show dei", "pulse dei", "icon oil2 -247 -1 🛢️", "arrow go -222,30 -245,0", "sfx whoosh"]),
    ("แต่ทางนั้น{มีกองเรืออเมริกาขวาง}", None,
     ["cam -195 20 57 1.6", "pin ph " + PEARL, "label phl -157.95 23.0 เพิร์ลฮาร์เบอร์", "pill block -170 30 กองเรือแปซิฟิก", "sfx pop"]),
    ("แผนคือ {ตีให้จมก่อน}", None,
     ["clear", "chapter 2 แผนเสี่ยง", "cam -186 8 57 1.2", "sprite cv carrier -212.33 44.97 160", "pin hito " + HITO,
      "card กองเรือจู่โจม|เรือบรรทุกเครื่องบิน 6 ลำ|ออกจากหมู่เกาะคูริล 26 พ.ย. 1941", "sfx riser"]),
    ("แล่นอ้อมทางเหนือ {ปิดวิทยุเงียบ}", None,
     ["route kbr 6 " + KB, "sail cv 6 " + KB, "icon ic4 -180 41.5 📻", "sfx waves"]),
    ("7 ธ.ค. {เจ็ดโมงสองนาที}", "เจ็ดธันวา เจ็ดโมงสองนาที", ["clear", "chapter 3 เช้าวันอาทิตย์", "scene radar", "sfx tick"]),
    ("เรดาร์เจอ{เป้าใหญ่ที่สุดที่เคยเห็น}", None, ["sfx alarm"]),
    ("รายงานไป {ได้คำตอบว่า ไม่ต้องห่วง}", "รายงานไป ได้คำตอบว่า... ไม่ต้องห่วง", ["sfx gasp"]),
    ("เพราะเช้านั้น{มี B-17 ฝ่ายเราจะบินมา}", "เพราะเช้านั้น มีบีสิบเจ็ดฝ่ายเรา จะบินมา", ["endscene", "cam -157 24 14 1.0", "pin ph " + PEARL, "arrow b17 -150.5,30 -157.6,21.8", "icon b17i -151.5 28.5 ✈️", "label b17l -152.5 30.8 B-17 จากแคลิฟอร์เนีย", "sfx plane"]),
    ("{ไม่ถึงชั่วโมงต่อมา}", None,
     ["endscene", "clear", "cam -158.05 23.6 6 0.8", "pin ph " + PEARL, "sprite pl plane -158.2 26.6 130",
      "sail pl 3 " + STRIKE, "route sk 3 " + STRIKE, "flash", "shake .8", "sfx plane"]),
    ("{เรือรบทั้งแปดลำ} เสียหาย", "เรือรบทั้งแปดลำ เสียหาย",
     ["cam -157.97 21.45 1.0 1.0", "ring phr -157.95 21.36 70", "card ความสูญเสียฝั่งสหรัฐ|กว่า 2,400 ชีวิต|ไว้อาลัยทุกชีวิตทุกฝ่าย", "sfx boom"]),
    ("ญี่ปุ่นคิดว่าชนะ {แต่เป้าสำคัญไม่อยู่}", None,
     ["clear", "cam -166 23 24 1.2", "pin ph " + PEARL, "sprite us uscv -166.0 19.6 140", "sail us 3 " + ENT, "sfx gasp"]),
    ("{เรือบรรทุกเครื่องบินอเมริกา} ออกทะเลหมด", None, ["sfx waves"]),
    ("ครึ่งปีต่อมาที่มิดเวย์ {ญี่ปุ่นเสียเรือแบบนี้ 4 ลำ}", "ครึ่งปีต่อมาที่มิดเวย์ ญี่ปุ่นเสียเรือแบบนี้สี่ลำ",
     ["cam -172 24 22 1.2", "icon ic5 " + MIDWAY + " ✈️", "label mwl -177.37 29.5 มิดเวย์", "ring mwr " + MIDWAY + " 60",
      "bars มาเพิร์ลฮาร์เบอร์:6:red จมที่มิดเวย์:4:grey", "sfx boom"]),
    ("หวังจบสงครามเร็ว {กลับลากอเมริกาเข้ามา}", "หวังจะจบสงครามให้เร็ว กลับลากอเมริกาเข้ามาเต็มตัว",
     ["clear", "cam -186 8 57 1.4", "show japan", "show hawaii", "pulse hawaii", "sfx boom"]),
    ("คืนเดียวกัน {ทหารญี่ปุ่นก็ขึ้นฝั่งไทย}", None,
     ["whip -255 9 13", "show thai", "show malaya", "pin bkk " + BKK] + INV + ["sfx splash"]),
    ("{ติดตามตอนหน้า}", "ติดตามตอนหน้า", ["outro เพิร์ลฮาร์เบอร์ 1941|ตอนหน้า: 8 ธันวาคม 2484", "sfx chime"]),
]

COVER = ("เรดาร์เห็นแล้ว", "แต่ไม่มีใครเชื่อ", "a dark muted relief map of the North Pacific with a glowing dotted route from the Kuril Islands "
         "to Hawaii, a chibi Japanese aircraft carrier sailing in stormy waves and a chibi US radar operator with headphones looking surprised, "
         "a large glowing radar blip, not violent, no explosions",
         ["carrier.png", "radarman.png", "scene_radar.png"])
