#!/usr/bin/env python3
"""ภาพดาวเทียม + เขตแดน สำหรับ topic:  python3 tools/mapgen.py topics/<slug>
อ่าน MAP / REGIONS / LINES_GEO จาก topics/<slug>/script.py → assets/map.jpg + regions.js

MAP = dict(lon0=, lon1=, lat0=, lat1=, ppd=)   # lon เกิน ±180 ได้ (แผนที่วนรอบโลก)
REGIONS = [("key", "red", dict(adm0=["THA"], adm1={"LAO": "*"}, adm1_not={"LAO": ["Sainyabuli"]}, poly=[[(lon,lat),...]])), ...]
LINES_GEO = {"mekong": dict(river="Mekong")}
"""
import os, sys, math, json, re, runpy, urllib.request
import numpy as np, shapefile
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(HERE, "assets", "src")
NASA = "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73776/world.topo.bathy.200408.3x"

def fetch(name, url):
    p = os.path.join(SRC, name)
    if not os.path.exists(p):
        print("download", name); urllib.request.urlretrieve(url, p + ".part"); os.rename(p + ".part", p)
    return p

def source_crop(lon0, lon1, lat0, lat1, sppd):
    """Crop [lon0,lon1]x[lat0,lat1] at sppd px/deg from NASA Blue Marble, wrapping longitude."""
    out = Image.new("RGB", (round((lon1 - lon0) * sppd), round((lat1 - lat0) * sppd)))
    for o in (-360, 0, 360):  # world copies
        a, b = max(lon0, -180 + o), min(lon1, 180 + o)
        if a >= b: continue
        if sppd == 60:
            world = Image.open(fetch("bmng60_world.jpg", NASA + "21600x10800.jpg"))
            box = (round((a - o + 180) * 60), round((90 - lat1) * 60), round((b - o + 180) * 60), round((90 - lat0) * 60))
            out.paste(world.crop(box), (round((a - lon0) * 60), 0))
        else:  # 240 ppd tiles A1..D2 (90° x 90°)
            for ci, col in enumerate("ABCD"):
                for ri, row in enumerate("12"):
                    tl_lon, tl_lat = -180 + ci * 90, 90 - ri * 90
                    ta, tb = max(a - o, tl_lon), min(b - o, tl_lon + 90)
                    tc, td = max(lat0, tl_lat - 90), min(lat1, tl_lat)
                    if ta >= tb or tc >= td: continue
                    tile = Image.open(fetch(f"bmng240_{col}{row}.jpg", NASA + f"21600x21600.{col}{row}.jpg"))
                    box = (round((ta - tl_lon) * 240), round((tl_lat - td) * 240), round((tb - tl_lon) * 240), round((tl_lat - tc) * 240))
                    out.paste(tile.crop(box), (round((ta + o - lon0) * 240), round((lat1 - td) * 240)))
                    del tile
    return out

def grade(im):
    """Vivid azure ocean + slightly richer land (the reference reel look)."""
    a = np.asarray(im).astype(np.float32); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    ocean = (np.clip(((b - r) - 25) / 30, 0, 1) * np.clip(((b - g) - 5) / 20, 0, 1))[..., None]
    lum = (0.3 * r + 0.59 * g + 0.11 * b) / 255
    deep = np.clip(np.stack([10 + 132 * lum, 60 + 300 * lum, 140 + 280 * lum], -1), 0, 255)
    m = a.mean(-1, keepdims=True); land = np.clip(m + (a - m) * 1.25, 0, 255); land = np.clip((land - 128) * 1.08 + 132, 0, 255)
    return Image.fromarray((land * (1 - ocean) + (0.25 * a + 0.75 * deep) * ocean).astype(np.uint8))

def muted(im):
    """Hillshade look (ref: เหตุผลบนแผนที่): brown relief land, dark navy ocean — lets glowing regions carry the colour."""
    a = np.asarray(im).astype(np.float32); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    # ponytail: looser than grade()'s mask so the very dark deep ocean (b-r < 25) still counts as sea
    ocean = (np.clip(((b - r) - 6) / 14, 0, 1) * np.clip(((b - g) + 8) / 14, 0, 1))[..., None]
    lum = ((0.3 * r + 0.59 * g + 0.11 * b) / 255)[..., None]
    lum = np.clip((lum - lum.mean()) * 1.6 + 0.5, 0, 1)  # stretch relief contrast
    land = np.array([70, 54, 38]) + lum * np.array([110, 90, 66])
    sea = np.array([12, 26, 48]) + lum * np.array([18, 26, 40])
    return Image.fromarray(np.clip(land * (1 - ocean) + sea * ocean, 0, 255).astype(np.uint8))

NE = "https://naciscdn.org/naturalearth/10m/"
def natural_earth():
    """ดาวน์โหลดเส้นเขตแดน/แม่น้ำ Natural Earth (public domain) ครั้งแรกครั้งเดียว"""
    import zipfile
    for d, url in [("adm0", NE + "cultural/ne_10m_admin_0_countries.zip"), ("adm1", NE + "cultural/ne_10m_admin_1_states_provinces.zip"),
                   ("rivers", NE + "physical/ne_10m_rivers_lake_centerlines.zip")]:
        if os.path.isdir(os.path.join(SRC, d)): continue
        z = fetch(d + ".zip", url); zipfile.ZipFile(z).extractall(os.path.join(SRC, d))

def main(topic):
    os.makedirs(SRC, exist_ok=True); natural_earth()
    cfg = runpy.run_path(os.path.join(topic, "script.py"))
    M = cfg["MAP"]; lon0, lon1, lat0, lat1, ppd = M["lon0"], M["lon1"], M["lat0"], M["lat1"], M["ppd"]
    k = math.cos(math.radians((lat0 + lat1) / 2))
    W, H = round((lon1 - lon0) * ppd * k), round((lat1 - lat0) * ppd)
    assert W <= 9000 and H <= 9000, f"map {W}x{H} too big, lower ppd"
    X = lambda lon: (lon - lon0) * ppd * k
    Y = lambda lat: (lat1 - lat) * ppd
    os.makedirs(os.path.join(topic, "assets"), exist_ok=True)
    mp = os.path.join(topic, "assets", "map.jpg")
    if not os.path.exists(mp):
        sppd = 240 if ppd > 60 else 60
        look = muted if cfg.get("STYLE") == "muted" else grade
        look(source_crop(lon0, lon1, lat0, lat1, sppd).resize((W, H), Image.LANCZOS)).save(mp, quality=86)
    print(f"map {W}x{H} k={k:.3f}")
    hires = None
    if "hires" in M:  # HIRES inset: Sentinel-2 cloudless 2016 (EOX, CC BY 4.0) for close zoom; credit shown on screen
        h = M["hires"]; hp = os.path.join(topic, "assets", "hires.jpg")
        hw, hh = round((h["lon1"] - h["lon0"]) * h["ppd"] * k), round((h["lat1"] - h["lat0"]) * h["ppd"])
        assert hw <= 6000 and hh <= 6000, f"hires {hw}x{hh} too big"
        if not os.path.exists(hp):
            im = Image.new("RGB", (hw, hh)); T = 2000
            for y0 in range(0, hh, T):
                for x0 in range(0, hw, T):
                    w, ht = min(T, hw - x0), min(T, hh - y0)
                    bb = (h["lon0"] + x0 / hw * (h["lon1"] - h["lon0"]), h["lat1"] - (y0 + ht) / hh * (h["lat1"] - h["lat0"]),
                          h["lon0"] + (x0 + w) / hw * (h["lon1"] - h["lon0"]), h["lat1"] - y0 / hh * (h["lat1"] - h["lat0"]))
                    def wms(layer):
                        url = ("https://tiles.maps.eox.at/wms?service=WMS&request=GetMap&version=1.1.1&layers=" + layer + "&styles=&srs=EPSG:4326"
                               f"&bbox={bb[0]},{bb[1]},{bb[2]},{bb[3]}&width={w}&height={ht}&format=image/jpeg")
                        tp = hp + f".{layer}.{x0}_{y0}.part"; urllib.request.urlretrieve(url, tp); t = Image.open(tp).convert("RGB"); t.load(); os.remove(tp); return t
                    tile = wms("s2cloudless")
                    if h.get("shade"):  # multiply EOX hillshade so white snow/cloud keeps its relief (Everest)
                        sh = np.asarray(wms("terrain").convert("L")).astype(np.float32)[..., None] / 255
                        tile = Image.fromarray((np.asarray(tile).astype(np.float32) * (0.3 + 0.7 * sh)).clip(0, 255).astype(np.uint8))
                    im.paste(tile, (x0, y0))
            if h.get("tone"):  # tone=1.6 etc: compress blown-out snow/cloud so relief shows (Everest)
                im = Image.fromarray((255 * (np.asarray(im).astype(np.float32) / 255) ** h["tone"]).astype(np.uint8))
            (muted if cfg.get("STYLE") == "muted" else grade)(im).save(hp, quality=88)
        hires = dict(shade=bool(h.get("shade")), x=round(X(h["lon0"]), 2), y=round(Y(h["lat1"]), 2), w=round(X(h["lon1"]) - X(h["lon0"]), 2), h=round(Y(h["lat0"]) - Y(h["lat1"]), 2))
        print(f"hires {hw}x{hh}")

    def ring(pts, sh):
        d, last, n = "", None, 0
        for lo, la in pts:
            x, y = X(lo + sh), Y(la)
            if last and abs(x - last[0]) + abs(y - last[1]) < 2: continue
            d += ("L" if n else "M") + f"{x:.1f} {y:.1f}"; last = (x, y); n += 1
        return d + "Z" if n > 2 else ""
    def shape_d(shp):
        parts = list(shp.parts) + [len(shp.points)]; out = ""
        xs = [p[0] for p in shp.points]
        for sh in (-360, 0, 360):  # emit copies that land inside the (possibly >180°) map
            if max(xs) + sh < lon0 - 5 or min(xs) + sh > lon1 + 5: continue
            if min(p[1] for p in shp.points) > lat1 + 5 or max(p[1] for p in shp.points) < lat0 - 5: continue
            out += "".join(ring(shp.points[parts[i]:parts[i + 1]], sh) for i in range(len(parts) - 1))
        return out
    clean = lambda s: (s or "").replace("\0", "").strip()

    adm0 = shapefile.Reader(os.path.join(SRC, "adm0", "ne_10m_admin_0_countries.shp"), encoding="utf-8")
    adm1 = shapefile.Reader(os.path.join(SRC, "adm1", "ne_10m_admin_1_states_provinces.shp"), encoding="utf-8")
    f0 = [(clean(r["ADM0_A3"]), s) for r, s in zip(adm0.iterRecords(fields=["ADM0_A3"]), adm0.iterShapes())]
    f1 = [(clean(r["adm0_a3"]), clean(r["name_en"]), clean(r["name"]), s)
          for r, s in zip(adm1.iterRecords(fields=["adm0_a3", "name_en", "name"]), adm1.iterShapes())]
    regions = {}
    for key, color, spec in cfg.get("REGIONS", []):
        d = ""
        for a3, s in f0:
            if a3 in spec.get("adm0", []): d += shape_d(s)
        for a3, ne, nm, s in f1:
            want, skip = spec.get("adm1", {}).get(a3), spec.get("adm1_not", {}).get(a3, [])
            if want and (want == "*" or ne in want or nm in want) and ne not in skip and nm not in skip: d += shape_d(s)
        for poly in spec.get("poly", []): d += ring(poly, 0)
        if not d: print("WARN empty region", key)
        regions[key] = {"color": color, "d": d}
    lines = {}
    lg = cfg.get("LINES_GEO", {})
    if any("river" in v for v in lg.values()):
        rv = shapefile.Reader(os.path.join(SRC, "rivers", "ne_10m_rivers_lake_centerlines.shp"), encoding="utf-8")
        recs = [(clean(r["name"]), s) for r, s in zip(rv.iterRecords(fields=["name"]), rv.iterShapes())]
    for key, v in lg.items():
        if "river" in v:
            lines[key] = "".join("".join(("L" if i else "M") + f"{X(lo):.1f} {Y(la):.1f}" for i, (lo, la) in enumerate(s.points))
                                 for nm, s in recs if re.search(v["river"], nm, re.I))
        if "pts" in v:
            lines[key] = "".join(("L" if i else "M") + f"{X(lo):.1f} {Y(la):.1f}" for i, (lo, la) in enumerate(v["pts"]))
    js = (f"window.MAP = {json.dumps(dict(W=W, H=H, lon0=lon0, lat1=lat1, ppd=ppd, k=round(k, 5), hires=hires))};\n"
          f"window.REGIONS = {json.dumps(regions)};\nwindow.LINES_GEO = {json.dumps(lines)};\n")
    open(os.path.join(topic, "regions.js"), "w").write(js)
    print("regions", {k: len(v["d"]) for k, v in regions.items()}, "lines", {k: len(v) for k, v in lines.items()})

if __name__ == "__main__":
    main(sys.argv[1].rstrip("/"))
