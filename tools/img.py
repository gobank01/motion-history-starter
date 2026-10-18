#!/usr/bin/env python3
"""OpenRouter Gemini image: img.py prompt.txt out.png aspect [ref.png ...]"""
import sys, json, base64, urllib.request
p, out, aspect, refs = open(sys.argv[1]).read(), sys.argv[2], sys.argv[3], sys.argv[4:]
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))
from config import key
KEY = key("OPENROUTER_API_KEY")
content = [{"type": "text", "text": p}] + [{"type": "image_url", "image_url": {"url": "data:image/png;base64," + base64.b64encode(open(r, "rb").read()).decode()}} for r in refs]
body = json.dumps({"model": "google/gemini-3.1-flash-image", "modalities": ["image", "text"], "image_config": {"aspect_ratio": aspect},
                   "messages": [{"role": "user", "content": content}]}).encode()
d = json.loads(urllib.request.urlopen(urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", body,
    {"Authorization": "Bearer " + KEY, "content-type": "application/json"}), timeout=300).read())
open(out, "wb").write(base64.b64decode(d["choices"][0]["message"]["images"][0]["image_url"]["url"].split(",", 1)[1]))
print(out, d.get("usage", {}).get("cost"))
