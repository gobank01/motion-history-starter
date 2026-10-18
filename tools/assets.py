#!/usr/bin/env python3
"""ภาพประกอบต่อเรื่อง: python3 tools/assets.py topics/<slug>
TOKENS = [("name", "description"), ...]  -> sticker sheet แถวเดียว -> ตัดพื้นหลัง (Vision) -> assets/<name>.png
SCENES = {"name": "prompt"}               -> assets/scene_<name>.png (9:16 ฉากจำลอง)
สไตล์อ้างอิง engine/style_ref.png (มาสคอต) ทุกภาพ · ใช้ OpenRouter Gemini (~฿2.3/ภาพ)"""
import os, sys, runpy, subprocess
import numpy as np
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.abspath(sys.argv[1]); A = os.path.join(T, "assets"); G = os.path.join(T, "gen"); os.makedirs(A, exist_ok=True); os.makedirs(G, exist_ok=True)
cfg = runpy.run_path(os.path.join(T, "script.py"))
REF = os.path.join(HERE, "engine", "style_ref.png")
STYLE = ("Match the exact art style, outline weight and soft cel shading of the attached reference character sheet "
         "(cute modern chibi sticker style, thick smooth dark-brown outlines), but do NOT draw that reference character. ")

BACKEND = os.environ.get("IMG_BACKEND", "openrouter")  # openrouter (เร็ว ขนานได้ ~฿2.3) | codex (ฟรีผ่าน ChatGPT แต่ช้า ~8 นาที ต้องทีละภาพ)
WORKERS = 1 if BACKEND == "codex" else 4

def gen(prompt, out, aspect):
    pf = out + ".txt"; open(pf, "w").write(prompt + (f" Aspect ratio {aspect}." if BACKEND == "codex" else ""))
    if BACKEND == "codex":
        subprocess.run(["python3", os.path.expanduser("~/.claude/skills/gpt-image-gen/scripts/gen_image.py"), "--prompt-file", pf,
                        "--out", out, "--verbatim", "--ref", REF], check=True)
    else:
        subprocess.run(["python3", os.path.join(HERE, "tools", "img.py"), pf, out, aspect, REF], check=True)

jobs = []
tok = cfg.get("TOKENS", [])
need_tok = tok and not all(os.path.exists(os.path.join(A, n + ".png")) for n, _ in tok)
if need_tok and not os.path.exists(os.path.join(G, "tokens.png")):
    desc = " ".join(f"{i + 1}) {d}." for i, (_, d) in enumerate(tok))
    p = (STYLE + f"Sticker sheet of exactly {len(tok)} separate chibi game-token illustrations in ONE horizontal row, left to right in this order, "
         f"evenly spaced with wide gaps, not overlapping, each full body/whole object, on a plain flat light-grey background (#DDDDDD), "
         f"no text, no labels, no ground shadows. {desc}")
    jobs.append(("tokens", p, os.path.join(G, "tokens.png"), "21:9" if len(tok) > 3 else "16:9"))
for n, sp in cfg.get("SCENES", {}).items():
    out = os.path.join(A, f"scene_{n}.png")
    if not os.path.exists(out):
        jobs.append((n, STYLE + "Vertical 9:16 illustration for a history explainer, warm detailed painted background, cinematic but not gory, "
                     "no blood, no text, no letters. Leave the top 20% calm and simple (space for captions). Scene: " + sp, out, "9:16"))
def split(cut, names):
    """Cut sticker sheet into objects by connected blobs (weapons may overlap columns).
    Largest len(names) blobs = objects (left→right); small blobs (smoke, flags) join the nearest object."""
    from collections import deque
    im = Image.open(cut); A = np.asarray(im)[..., 3] > 20
    f = 4; m = A[: A.shape[0] // f * f, : A.shape[1] // f * f].reshape(A.shape[0] // f, f, A.shape[1] // f, f).any((1, 3))
    d = m.copy()
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):  # dilate 1 cell to glue thin parts
        d |= np.roll(np.roll(m, dy, 0), dx, 1)
    lab = np.zeros(d.shape, int); cur = 0
    for y, x in zip(*np.nonzero(d)):
        if lab[y, x]: continue
        cur += 1; q = deque([(y, x)]); lab[y, x] = cur
        while q:
            cy, cx = q.popleft()
            for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                if 0 <= ny < d.shape[0] and 0 <= nx < d.shape[1] and d[ny, nx] and not lab[ny, nx]:
                    lab[ny, nx] = cur; q.append((ny, nx))
    ids = range(1, cur + 1); area = {i: (lab == i).sum() for i in ids}
    cen = {i: np.argwhere(lab == i).mean(0) for i in ids}
    big = sorted(sorted(ids, key=lambda i: -area[i])[: len(names)], key=lambda i: cen[i][1])
    if len(big) != len(names): print(f"WARN {len(big)} blobs for {len(names)} tokens — check {cut}")
    owner = {i: min(big, key=lambda b: np.hypot(*(cen[i] - cen[b]))) for i in ids}
    for n, b in zip(names, big):
        keep = np.isin(lab, [i for i in ids if owner[i] == b]).repeat(f, 0).repeat(f, 1)
        full = np.zeros(A.shape, bool); full[: keep.shape[0], : keep.shape[1]] = keep
        rgba = np.asarray(im).copy(); rgba[..., 3] = np.where(full, rgba[..., 3], 0)
        o = Image.fromarray(rgba); o.crop(o.getbbox()).save(os.path.join(A_DIR, n + ".png"))

A_DIR = A
with ThreadPoolExecutor(WORKERS) as ex:
    list(ex.map(lambda j: gen(j[1], j[2], j[3]), jobs))

if need_tok:
    cut = os.path.join(G, "tokens_cut.png")
    if not os.path.exists(cut):
        subprocess.run(["swift", os.path.join(HERE, "tools", "cutout.swift"), os.path.join(G, "tokens.png"), cut], check=True)
    split(cut, [n for n, _ in tok])
print(os.path.basename(T), "assets:", sorted(os.listdir(A)))
