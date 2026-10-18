# 029 อาณาจักรจามปา หายไปไหน (เล่าเรื่องแบบ STORY-RULES v3)
# คำถามเดียว: อาณาจักรริมทะเลที่อยู่มากว่าพันปี หายไปไหน — และทำไมคนของมันมาอยู่กลางกรุงเทพฯ?
# ตัวเอก: ชาวจาม (พ่อค้า/ชาวเรือ → ครอบครัวที่ต้องย้ายบ้าน) · เดิมพัน: ชายฝั่งที่เลี้ยงชีวิตมาหลายร้อยปี
# แหล่งหลัก: en.wikipedia "Champa" (+ Kiernan 2009, Maspero) · en.wikipedia "Chams" (สำมะโนเวียดนาม 2019, Al Jazeera 2019)
#   · en.wikipedia "Rudravarman III" (1069) · "Huyền Trân" (1306 แคว้นโอ/รี) · "Chế Bồng Nga" · "Ban Khrua"
#   · ศิลปวัฒนธรรม "บ้านครัว แหล่งทอผ้าไหมของชาวจาม" (silpa-mag.com/?p=118727) · มติชนสุดสัปดาห์ (จามบ้านครัวมาจากเขมร)
#   · Danny Wong Tze Ken / Archipel 2013 "The Cham Arrivals in Malaysia" · UNESCO "My Son Sanctuary" (มรดกโลก 1999)
# เลี่ยง/ระวัง:
#   - "หลินอี้ (ค.ศ. 192) = จุดเริ่มจามปา" นักวิชาการยังไม่ยุติ → ไม่ใช้ปี 192 ใช้ "อยู่มากว่าพันปี" (จารึกจาม ~ศ.4 → 1832)
#   - ตัวเลขผู้เสียชีวิต/ถูกจับปี 1471 แหล่งไม่ตรงกัน (Kiernan ~120,000 / บันทึกจีน 40,000–60,000) + เลี่ยงความโหด → พูดแค่ "ถูกกวาดต้อนไปจำนวนมาก"
#   - "1471 = จามปาจบสิ้น" เป็นมุมมองนักประวัติศาสตร์รุ่นเก่า (Maspero) → บทเล่าว่าทางใต้ (ปาณฑุรังคะ) อยู่ต่อถึง 1832
#   - เจ้าชายจามพาคนหนีไปมะละกา มาจากพงศาวดารมลายู (Sejarah Melayu) → ใช้ "เล่ากันว่า"
#   - ที่มาของจามบ้านครัว มี 2 สาย (ทหารอาสาสงคราม 2328 / ถูกเกณฑ์มาจากเขมร) → บทพูดแค่ "มาจากกัมพูชา ช่วยรบสมัยรัชกาลที่ 1 ได้ที่ดินตั้งชุมชน" (ตรงกันทั้งสองสาย)
#   - คลองแสนแสบขุดสมัยรัชกาลที่ 3 (หลังชุมชนเกิด) → พูดแค่ "ริมคลองแสนแสบ" ในปัจจุบัน
#   - เหตุของการรุกลงใต้ (นามเตี๋ยน) นักวิชาการยังถกเถียง (Taylor/Vickery/Momoki) → [ตรวจอิสระ] ตัด "คนเยอะ ที่นาไม่พอ เลย..." ออก เล่าแค่ "ชายแดนติดกัน ไดเวียดค่อยๆ ขยายลงใต้" · เล่าว่าสองฝ่ายรบกันไปมา (จามก็ตีถึงทังลอง) ไม่ทำให้ฝ่ายใดเป็นผู้ร้าย
#   - ไม่วาดกษัตริย์องค์ใดเป็นการ์ตูน · ไม่ภาพโหด · ตัวละครเวียดเป็นทหารเดินถือธง ไม่ใช่ฉากฆ่า
TITLE = "จามปา"
HOOK = "อาณาจักรที่หายไป"
STYLE = "muted"
STYLE_WHY = "เรื่องอาณาจักร/อาณาเขตที่หดลงทีละส่วน → แผนที่หม่นนูน ให้สีจามปาเรืองแสงแล้วค่อยๆ เปลี่ยนสีทีละแคว้น"
VOICE = "tAV9ucNkXgK2k9TLxWkM"
MODEL = "eleven_v4"
MUSIC = "somber"
# W = 20*150*cos(11.5°) ≈ 2940 · H = 25*150 = 3750 (≥1920) · span สูงสุดที่ใช้ 13
MAP = dict(lon0=94, lon1=114, lat0=-1, lat1=24, ppd=150)
DAIVIET = ["Hanoi", "Red River Delta", "Northeast Vietnam", "Haiphong", "Hà Nam", "Nam Định", "Ninh Bình", "Thái Bình",
           "Hải Dương", "Bắc Ninh", "Bắc Giang", "Vĩnh Phúc", "Phú Thọ", "Thái Nguyên", "Tuyên Quang", "Hòa Bình",
           "Thanh Hóa", "Nghệ An", "Hà Tĩnh", "Quảng Ninh", "Lạng Sơn", "Cao Bằng", "Hà Giang", "Yên Bái", "Lào Cai",
           "Sơn La", "Lai Châu", "Điện Biên"]
PENINSULA = ["Perlis", "Kedah", "Kelantan", "Perak", "Penang", "Selangor", "Negeri Sembilan", "Melaka", "Johor", "Pahang",
             "Terengganu", "Kuala Lumpur", "Putrajaya"]
REGIONS = [
    ("dv", "blue", dict(adm1={"VNM": DAIVIET})),                                  # ไดเวียด (โดยประมาณ ใช้เขตจังหวัดปัจจุบัน)
    ("c1", "gold", dict(adm1={"VNM": ["Quảng Bình", "Quảng Trị"]})),              # เสียราว 1069
    ("c2", "gold", dict(adm1={"VNM": ["Thừa Thiên Huế"]})),                       # แคว้นโอ/รี 1306 (Wikipedia: ราวกว๋างจิ-เว้-ดานัง ปัจจุบัน แผนที่ใช้เว้เป็นตัวแทน)
    ("c3", "gold", dict(adm1={"VNM": ["Da Nang", "Quảng Nam", "Quảng Ngãi", "Bình Định"]})),   # ผนวก 1471 (เส้นแบ่งจริงไม่นิ่ง: บางแหล่งว่าถึงช่องเขาด่าก๋า · ฟู้เอียนผนวกจริง 1611)
    ("c4", "gold", dict(adm1={"VNM": ["Phú Yên", "Khánh Hòa", "Ninh Thuận", "Bình Thuận"]})),  # ทางใต้ทยอยเสีย (เกาฐาระ 1653) ส่วนสุดท้าย 1832 — แผนที่รวบเป็นก้อนเดียว
    ("khm", "purple", dict(adm0=["KHM"])),
    ("tha", "teal", dict(adm0=["THA"])),
    ("mly", "orange", dict(adm1={"MYS": PENINSULA})),
]
TOKENS = [
    ("chamship", "a cute chibi 13th-century Cham trading ship from Champa, wooden hull with carved prow, one big woven rectangular "
                 "sail, bundles of fragrant agarwood logs and ivory on deck, calm sea spray, full body side view facing right"),
    ("chamfamily", "a cute chibi Cham family of three walking together, father in a white headcloth and sarong carrying a cloth bundle "
                   "on a pole, mother in a long dress and headscarf holding a child's hand, hopeful brave faces, "
                   "full body side view facing right"),
    ("dvsoldier", "a cute chibi 15th-century Dai Viet Vietnamese foot soldier in a simple brown tunic and conical hat, carrying a "
                  "wooden spear and a round rattan shield, no flags, marching, determined but friendly face, no blood, "
                  "full body side view facing right"),
    ("chamboat", "a cute chibi small Cham wooden sailing boat with a patched square sail, a few chibi Cham families with bundles "
                 "on board looking ahead, gentle waves, full body side view facing right"),
]
SCENES = {
    "myson": "a lush green valley in central Vietnam in the 10th century with tall red brick Cham temple towers of My Son sanctuary, "
             "chibi Cham people in white and red cloth bringing flowers, a river below with Cham trading ships carrying agarwood "
             "and ivory toward the sea, warm golden afternoon light, peaceful prosperous mood, no king, no royalty",
    "weave": "present day, a small wooden house by a canal in Bangkok, a chibi Cham Muslim weaver woman in a headscarf working a "
             "wooden hand loom, bright shiny Thai silk in jewel colors hanging on bamboo poles, a small mosque dome and a canal "
             "boat in the background, warm friendly afternoon, peaceful mood",
}
# พิกัด
VIJAYA = "109.10 13.89"     # ป้อมจาบ่าน/โด่บ่าน (วิชัย) อานเญิน บิ่ญดิ่ญ
MYSON = "108.12 15.76"      # หมี่เซิน
HOIAN = "108.33 15.88"      # ฮอยอาน (เมืองท่า)
THANGLONG = "105.85 21.03"  # ทังลอง (ฮานอย)
HUE = "107.58 16.46"        # เว้ (แคว้นโอ/รี)
PANDU = "108.99 11.57"      # ปาณฑุรังคะ (ฟานราง)
PNOMPENH = "104.92 11.56"
BANKHRUA = "100.53 13.75"   # บ้านครัว ราชเทวี กรุงเทพฯ
MALACCA = "102.25 2.19"
TRADE = "112.8,21.4 111.2,18.6 109.6,16.6 108.45,15.90"
DV_SOUTH = "105.85,21.03 105.75,19.2 106.55,17.5 107.55,16.45 108.25,15.55 108.85,14.6 109.10,13.89"
TO_KHM = "108.95,11.65 107.7,11.85 106.4,11.75 104.92,11.56"
TO_MLK = "109.10,11.30 107.6,9.0 105.6,6.8 103.9,4.0 102.40,2.35"
TO_SIAM = "arrow sm 104.9,11.7 102.6,12.9 100.65,13.75"

LINES = [
    # ── HOOK
    ("อาณาจักรที่อยู่มากว่าพันปี {หายไปจากแผนที่}", "อาณาจักรที่อยู่มากว่าพันปี หายไปจากแผนที่",
     ["cam 107.5 14.5 9 0", "title อยู่มากว่าพันปี|แล้วหายไปไหน?|อาณาจักรจามปา", "show c1", "show c2", "show c3", "show c4",
      "sprite cs chamship 111.0 18.0 150", "flash", "sfx whoosh"]),
    ("แต่ลูกหลาน {ยังอยู่กลางกรุงเทพฯ}", "แต่ลูกหลาน ยังอยู่กลางกรุงเทพฯ",
     ["whip 100.53 13.75 3", "pin bk " + BANKHRUA, "icon ic0 100.9 14.3 🧵", "sfx gasp"]),
    # ── บท 1 ที่มา
    ("{จามปา} คือชายฝั่งเวียดนามตอนกลาง", "จามปา คือชายฝั่งเวียดนามตอนกลาง",
     ["clear", "chapter 1 เจ้าแห่งชายฝั่ง", "cam 107.5 15.5 11 1.2", "show c1", "show c2", "show c3", "show c4", "pulse c3",
      "source Wikipedia (Champa, Chams) · ศิลปวัฒนธรรม · UNESCO", "sfx waves"]),
    ("เรือจีนกับอินเดีย{แวะค้าที่นี่}", "เรือจีนกับอินเดีย แวะค้าที่นี่",
     ["sprite cs chamship 112.8 21.4 150", "route tr 4 " + TRADE, "sail cs 4 " + TRADE, "pin ha " + HOIAN, "sfx waves"]),
    ("จามเลย{รวยจากไม้หอม งาช้าง}", "จามเลยรวย จากไม้หอม งาช้าง",
     ["scene myson", "sfx coin"]),
    ("แต่ทางเหนือมี{ไดเวียด}ที่โตเร็ว", "แต่ทางเหนือ มีไดเวียดที่โตเร็ว",
     ["endscene", "clear", "cam 106.8 17.5 12 1.2", "show c1", "show c2", "show c3", "show c4", "show dv", "pin tl " + THANGLONG,
      "label tll 105.85 21.9 ทังลอง", "sfx march"]),
    ("{ชายแดนสองฝ่ายติดกัน}", "ชายแดนสองฝ่ายติดกัน",
     ["pulse dv", "icon ic1 106.6 20.4 ⚔️"]),
    ("ไดเวียด{ค่อยๆ ขยายลงใต้}", "ไดเวียดค่อยๆ ขยายลงใต้",
     ["sprite dv1 dvsoldier 105.85 21.03 150", "walk dv1 4 " + DV_SOUTH, "route dvr 4 " + DV_SOUTH, "sfx steps"]),
    # ── บท 2 ชักเย่อ
    ("จาม{เสียแดนเหนือไปทีละแคว้น}", "จามเสียแดนเหนือไปทีละแคว้น",
     ["clear", "chapter 2 ชักเย่อหลายร้อยปี", "cam 107.6 16.8 7 1.0", "show dv", "show c1", "show c2", "show c3", "show c4",
      "recolor c1 blue", "label q1 106.2 17.9 ราว 1069", "sfx boom"]),
    ("บางแคว้น{ยกให้ แลกการอภิเษกสมรส}", "บางแคว้นยกให้ แลกการอภิเษกสมรส",
     ["recolor c2 blue", "pin hu " + HUE, "label hul 106.9 16.9 เว้ · 1306", "icon ic2 108.2 16.9 💍", "sfx bell"]),
    ("แต่จามก็ไม่ยอม {ยกทัพเรือตีถึงทังลอง}", "แต่จามก็ไม่ยอม ยกทัพเรือตีถึงทังลอง",
     ["cam 106.8 18.0 10 1.0", "arrow cb 108.4,15.9 107.6,18.2 106.5,20.3 105.9,20.95", "pin tl " + THANGLONG,
      "shake .4", "sfx cannon"]),
    ("จนปี 1471 {เมืองหลวงวิชัยแตก}", "จนปีหนึ่งพันสี่ร้อยเจ็ดสิบเอ็ด เมืองหลวงวิชัยแตก",
     ["cam 108.8 14.6 5 0.8", "pin vj " + VIJAYA, "ring vjr 109.10 13.89 70",
      "card ค.ศ. 1471|เมืองหลวงวิชัยแตก|ดินแดนตอนเหนือถูกผนวกเข้าไดเวียด", "recolor c3 blue", "flash", "shake .8", "sfx boom"]),
    ("ผู้คน{ถูกกวาดต้อนไปจำนวนมาก}", "ผู้คนถูกกวาดต้อนไปจำนวนมาก", ["sfx gasp"]),
    # ── บท 3 ปม → ผลที่ไม่มีใครคาด
    ("แต่เชื่อไหม {จามปายังไม่หาย}", "แต่เชื่อไหม... จามปายังไม่หาย",
     ["clear", "chapter 3 ไม่ได้หาย แค่ย้ายบ้าน", "cam 108.6 12.6 6 1.0", "show c4", "pulse c4", "pin pd " + PANDU,
      "label pdl 108.2 11.0 ปาณฑุรังคะ", "sfx riser"]),
    ("ทางใต้อยู่ต่อ {อีกกว่า 360 ปี}", "ทางใต้อยู่ต่อ อีกกว่าสามร้อยหกสิบปี",
     ["card ค.ศ. 1832|ถูกรวมเข้าเวียดนาม|ส่วนสุดท้ายของจามปา", "recolor c4 blue", "sfx tick"]),
    ("ระหว่างนั้น {ชาวจามทยอยย้ายบ้าน}", "ระหว่างนั้น ชาวจามทยอยย้ายบ้าน",
     ["cam 105.5 10.5 11 1.2", "show khm", "sprite fm chamfamily 108.95 11.65 150", "walk fm 3.5 " + TO_KHM,
      "route kr 3.5 " + TO_KHM, "pin pp " + PNOMPENH, "sfx steps"]),
    ("วันนี้จามในกัมพูชา {มากกว่าในเวียดนาม}", "วันนี้ จามในกัมพูชา มากกว่าในเวียดนาม",
     ["bars กัมพูชา:300000:purple เวียดนาม:179000:blue", "sfx pop"]),
    ("บางส่วนมาสยาม {สมัยรัชกาลที่ 1}", "บางส่วนมาสยาม สมัยรัชกาลที่หนึ่ง",
     ["clear", "cam 102.8 12.8 9 1.0", "show khm", "show tha", TO_SIAM, "pin bk " + BANKHRUA, "sfx march"]),
    ("ได้รับพระราชทานที่ดิน {ตั้งบ้านครัว}", "ได้รับพระราชทานที่ดิน ตั้งบ้านครัว",
     ["scene weave", "sfx bell"]),
    # ── ปิดพลิกฮุก + ตอนหน้า
    ("ชาวจามไม่ได้หาย {แค่ย้ายบ้าน}", "ชาวจามไม่ได้หาย... แค่ย้ายบ้าน",
     ["endscene", "clear", "cam 104.5 11.5 13 1.4", "show khm", "show tha", "show mly", "show c4", "recolor c4 gold",
      "pin bk " + BANKHRUA, "pin pp " + PNOMPENH, "pin ml " + MALACCA, "sfx whoosh"]),
    ("เล่ากันว่า เจ้าชายจาม{พาคนหนีไปมะละกา}", "เล่ากันว่า เจ้าชายจามพาคนหนีไปมะละกา",
     ["sprite bt chamboat 109.10 11.30 150", "sail bt 3.5 " + TO_MLK, "route mr 3.5 " + TO_MLK,
      "label mll 102.25 1.4 มะละกา", "sfx waves"]),
    ("{ติดตามตอนหน้า}", "ติดตามตอนหน้า", ["outro อาณาจักรจามปา|ตอนหน้า: มะละกา ท่าเรือที่ทุกชาติแย่ง", "sfx chime"]),
]

COVER = ("อาณาจักรที่หายไป", "จามปา หายไปไหน?",
         "a glowing gold coastal kingdom along central Vietnam on a dark muted relief map of Southeast Asia, tall red brick Cham "
         "temple towers on a green hill, a chibi Cham trading ship with a woven sail leaving the coast, the gold light fading "
         "and drifting as small boats toward Cambodia and Bangkok, no flags, no national symbols, no kings or royalty, not violent",
         ["chamship.png", "chamfamily.png", "scene_myson.png"])
