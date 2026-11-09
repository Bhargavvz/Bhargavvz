"""Generate the custom SVG assets for Bhargav's GitHub profile README.

Every asset is produced in a dark and a light variant so README <picture>
elements can follow the viewer's GitHub theme. No external fonts or images:
GitHub's image proxy blocks them inside SVGs, so system font stacks only.
"""
import os
import random
from xml.sax.saxutils import escape

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

SERIF = "'Iowan Old Style','Palatino Linotype',Palatino,'Book Antiqua',Georgia,serif"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'JetBrains Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(bg="#0b0a09", panel="#141210", fg="#efe8dc", mid="#b7aea1", muted="#7d756b",
                 line="#2a2622", accent="#ff7a45", accent2="#ffb38a", ok="#5ad48a", noise=(40, 235)),
    "light": dict(bg="#f7f4ee", panel="#fffdf9", fg="#171411", mid="#4a443d", muted="#8a8278",
                  line="#e3ddd3", accent="#d9480f", accent2="#f08a5d", ok="#1f9d55", noise=(20, 215)),
}


def t(x, y, s, size, fill, family=SANS, weight=400, anchor="start", extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(s)}</text>')


def svg(w, h, body, style=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<style>{style}</style>{body}</svg>')


def save(name, theme, content):
    with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w", encoding="utf-8") as f:
        f.write(content)



BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def dither(x0, y0, cols, rows, cell, color, cls="", power=1.6, gap=4):
    """Ordered (Bayer) dither that fades from empty on the left to dense on the right."""
    out = []
    for r in range(rows):
        for q in range(cols):
            f = (q + 0.5) / cols
            if (BAYER[r % 4][q % 4] + 0.5) / 16 < f ** power:
                op = round(0.18 + 0.82 * f, 2)
                out.append(f'<rect {cls} x="{x0+q*cell+gap/2}" y="{y0+r*cell+gap/2}" width="{cell-gap}" '
                           f'height="{cell-gap}" rx="2" fill="{color}" opacity="{op}"/>')
    return "".join(out)

# ───────────────────────────────── HERO ─────────────────────────────────
def hero(theme):
    c = THEMES[theme]
    W, H, cell = 1200, 450, 20
    rng = random.Random(7)
    cols, rows = W // cell, H // cell
    lo, hi = c["noise"]
    rects = []
    for r in range(rows):
        for q in range(cols):
            g = rng.randint(lo, hi)
            col = f"#{g:02x}{g:02x}{g:02x}"
            # pixels further from the centre-left clear later, so the image "denoises" toward the name
            d = abs(q - 18) / cols + abs(r - 9) / rows
            b = min(9, int((d * 0.9 + rng.random() * 0.6) * 9))
            rects.append(f'<rect class="n b{b}" x="{q*cell}" y="{r*cell}" width="{cell}" height="{cell}" fill="{col}"/>')
    # a few accent pixels that survive the denoise, like a signature
    keep = ['<g class="k">' + dither(720, 40, 22, 11, cell, c["accent"]) + '</g>']
    buckets = "".join(f".b{i}{{animation:clear .9s ease-in {0.25+i*0.22:.2f}s forwards}}" for i in range(10))
    steps = ["1000", "0750", "0500", "0250", "0000"]
    tsteps = "".join(
        f".s{i}{{opacity:0;animation:blink 0.01s linear {0.2+i*0.55:.2f}s forwards{', hide 0.01s linear %.2fs forwards' % (0.2+(i+1)*0.55) if i < 4 else ''}}}"
        for i in range(5))
    style = f"""
      .n{{opacity:.92}} {buckets}
      @keyframes clear{{to{{opacity:0}}}}
      @keyframes blink{{to{{opacity:1}}}}
      @keyframes hide{{to{{opacity:0}}}}
      @keyframes rise{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
      @keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}
      .k{{opacity:0;animation:blink .01s linear 2.3s forwards}}
      .r1{{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) 1.7s forwards}}
      .r2{{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) 2.1s forwards}}
      .r3{{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) 2.5s forwards}}
      .dot{{animation:pulse 1.6s ease-in-out infinite}}
      {tsteps}
      @media (prefers-reduced-motion:reduce){{.n{{display:none}}.r1,.r2,.r3,.k,.s4{{opacity:1;animation:none}}}}
    """
    counters = "".join(t(64, 62, f"t = {s}", 18, c["muted"], MONO, 500, extra=f'class="s{i}"') for i, s in enumerate(steps))
    body = f"""
      <rect width="{W}" height="{H}" fill="{c['bg']}"/>
      {''.join(keep)}
      <g class="r1">
        {t(62, 205, "Bhargav Adepu", 104, c['fg'], SERIF, 500, extra='letter-spacing="-1.5"')}
      </g>
      <g class="r2">
        {t(66, 262, "I train models and ship the software around them.", 30, c['mid'], SERIF, 400, extra='font-style="italic"')}
      </g>
      <g class="r3">
        <line x1="66" y1="308" x2="1136" y2="308" stroke="{c['line']}"/>
        {t(66, 350, "ROLE", 15, c['muted'], MONO, 600, extra='letter-spacing="2"')}
        {t(66, 382, "AI/ML · Full-Stack", 22, c['fg'], SANS, 500)}
        {t(336, 350, "NOW", 15, c['muted'], MONO, 600, extra='letter-spacing="2"')}
        <circle class="dot" cx="343" cy="375" r="6" fill="{c['ok']}"/>
        {t(358, 382, "AI Intern, Infosys", 22, c['fg'], SANS, 500)}
        {t(626, 350, "OPEN SOURCE", 15, c['muted'], MONO, 600, extra='letter-spacing="2"')}
        {t(626, 382, "GSoC '25, VideoLAN", 22, c['fg'], SANS, 500)}
        {t(906, 350, "BASED IN", 15, c['muted'], MONO, 600, extra='letter-spacing="2"')}
        {t(906, 382, "Warangal · Hyd", 22, c['fg'], SANS, 500)}
        {t(1136, 420, "xₜ = √ᾱ · x₀ + √(1 − ᾱ) · ε", 15, c['muted'], MONO, 400, anchor="end")}
      </g>
      <g>{''.join(rects)}</g>
      <rect x="52" y="40" width="128" height="32" rx="6" fill="{c['bg']}"/>
      {counters}
    """
    save("hero", theme, svg(W, H, body, style))


# ─────────────────────────────── PROJECT CARDS ───────────────────────────────
PROJECTS = [
    dict(slug="vlc", code="S.01", cat="OPEN SOURCE", year="2025", status="GSoC 2025",
         name="VLC × GSoC", sub=["An AI media recommender built natively into", "VLC's decades-old C/C++ and Qt codebase."],
         metrics=[("C/C++", "native module"), ("Qt/QML", "UI layer"), ("CMake", "build integration")],
         stack="C · C++ · Qt/QML · CMake · GitLab CI"),
    dict(slug="aquasafe", code="S.02", cat="MACHINE LEARNING", year="2026", status="IEEE 2026",
         name="AquaSafe", sub=["Five models for waterborne-disease risk,", "behind a Flask API and a 19-screen app."],
         metrics=[("95.19%", "disease"), ("99.25%", "water safety"), ("0.9997", "outbreak AUC")],
         stack="XGBoost · LightGBM · Flask · Flutter"),
    dict(slug="medgpt", code="S.03", cat="MACHINE LEARNING", year="2026", status="active",
         name="MedGPT", sub=["Medical visual QA: Qwen3-VL-8B fine-tuned", "with LoRA across five imaging modalities."],
         metrics=[("78.5%", "overall accuracy"), ("87.1%", "yes / no"), ("81.2%", "token F1")],
         stack="PyTorch · LoRA · Grad-CAM · FastAPI"),
    dict(slug="photonqr", code="S.04", cat="SYSTEMS", year="2026", status="active",
         name="PhotonQR", sub=["Moving files across an air gap,", "one screenful of QR frames at a time."],
         metrics=[("AES-256", "GCM per packet"), ("0", "network perms"), ("~4 KB/s", "QR v15 @ 12 fps")],
         stack="Flutter · Dart · CRC-32 · Reed–Solomon"),
    dict(slug="skinguard", code="S.05", cat="MACHINE LEARNING", year="2026", status="shipped",
         name="SkinGuard AI", sub=["A three-backbone ensemble for dermoscopic", "lesion classification, fused by attention."],
         metrics=[("25,331", "ISIC 2019 images"), ("589M", "parameters"), ("7 hr", "on a single H100")],
         stack="PyTorch · EVA-02 · ConvNeXt-V2 · ONNX"),
    dict(slug="meridian", code="S.06", cat="AGENTS", year="2026", status="active",
         name="Meridian", sub=["A supply-chain decision agent that recalls,", "simulates and recommends with evidence."],
         metrics=[("14 / 14", "holdout decisions"), ("Recall", "past precedents"), ("Cited", "evidence")],
         stack="FastAPI · React · TypeScript · SQLite · Docker"),
]


def card(p, theme):
    c = THEMES[theme]
    W, H = 600, 380
    live = p["status"] == "active"
    dot_col = c["ok"] if live else c["accent"]
    style = """@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}} .dot{animation:pulse 1.8s ease-in-out infinite}
               @keyframes draw{from{stroke-dashoffset:540}to{stroke-dashoffset:0}} .bar{stroke-dasharray:540;animation:draw 1.4s cubic-bezier(.2,.7,.2,1) .2s both}"""
    mx = ""
    for i, (v, l) in enumerate(p["metrics"]):
        x = 34 + i * 182
        mx += t(x, 262, v, 34, c["accent"] if i == 0 else c["fg"], MONO, 600, extra='letter-spacing="-1"')
        mx += t(x, 290, l, 16, c["muted"], SANS, 400)
    sw = len(p["status"]) * 9.6
    body = f"""
      <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{c['panel']}" stroke="{c['line']}" stroke-width="2"/>
      <line class="bar" x1="34" y1="2" x2="566" y2="2" stroke="{c['accent']}" stroke-width="3"/>
      {t(34, 52, f"{p['code']} · {p['cat']}", 15, c['muted'], MONO, 600, extra='letter-spacing="1"')}
      <circle class="dot" cx="{W-34-sw-14}" cy="47" r="5.5" fill="{dot_col}"/>
      {t(W-34, 52, p['status'], 16, c['mid'], MONO, 500, anchor="end")}
      {t(34, 118, p['name'], 50, c['fg'], SERIF, 500, extra='letter-spacing="-0.8"')}
      {t(W-34, 116, "↗", 30, c['muted'], SANS, 400, anchor="end")}
      {t(34, 156, p['sub'][0], 19, c['mid'], SANS, 400)}
      {t(34, 182, p['sub'][1], 19, c['mid'], SANS, 400)}
      <line x1="34" y1="210" x2="{W-34}" y2="210" stroke="{c['line']}" stroke-width="2"/>
      {mx}
      <line x1="34" y1="318" x2="{W-34}" y2="318" stroke="{c['line']}" stroke-width="2"/>
      {t(34, 351, p['stack'], 15.5, c['muted'], MONO, 400)}
    """
    save(f"card-{p['slug']}", theme, svg(W, H, body, style))


# ───────────────────────────────── TIMELINE ─────────────────────────────────
MILESTONES = [
    ("2023", ("Intinta", "Innovator"), "Govt. of Telangana"),
    ("2024", ("2nd Runner-Up", "HackByte"), "VIT-AP · 300+ teams"),
    ("2024", ("Hon. Mention", "SDG 11"), "IIT Hyderabad"),
    ("2025", ("Google Summer", "of Code"), "VideoLAN · VLC"),
    ("2026", ("IEEE IC-SIT", "paper"), "published Sep 2026"),
    ("NOW", ("AI Intern", "Infosys"), "since Oct 2026"),
]


def timeline(theme):
    c = THEMES[theme]
    W, H = 1200, 260
    n = len(MILESTONES)
    x0, x1, y = 140, 1060, 116
    step = (x1 - x0) / (n - 1)
    style = """@keyframes draw{from{stroke-dashoffset:920}to{stroke-dashoffset:0}}
               .ln{stroke-dasharray:920;animation:draw 2.2s cubic-bezier(.3,.6,.2,1) .2s both}
               @keyframes pop{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
               @keyframes ring{0%{r:7;opacity:.7}100%{r:22;opacity:0}}
               .ring{animation:ring 1.8s ease-out infinite}""" + "".join(
        f".m{i}{{opacity:0;animation:pop .6s ease-out {0.35+i*0.33:.2f}s forwards}}" for i in range(n))
    nodes = ""
    for i, (yr, a, b) in enumerate(MILESTONES):
        x = x0 + i * step
        last = i == n - 1
        col = c["ok"] if last else c["accent"]
        ring = f'<circle class="ring" cx="{x:.0f}" cy="{y}" r="7" fill="none" stroke="{col}" stroke-width="2"/>' if last else ""
        nodes += f"""<g class="m{i}">
          {t(x, 68, yr, 16, c['accent'] if not last else c['ok'], MONO, 700, "middle", 'letter-spacing="2"')}
          {ring}<circle cx="{x:.0f}" cy="{y}" r="7" fill="{c['bg']}" stroke="{col}" stroke-width="2.5"/>
          <circle cx="{x:.0f}" cy="{y}" r="3" fill="{col}"/>
          {t(x, 166, a[0], 18, c['fg'], SANS, 600, "middle")}
          {t(x, 190, a[1], 18, c['fg'], SANS, 600, "middle")}
          {t(x, 216, b, 15, c['muted'], SANS, 400, "middle")}
        </g>"""
    body = f"""
      <rect width="{W}" height="{H}" fill="{c['bg']}" rx="16"/>
      <line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{c['line']}" stroke-width="2"/>
      <line class="ln" x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{c['accent']}" stroke-width="2"/>
      {nodes}
    """
    save("timeline", theme, svg(W, H, body, style))


# ─────────────────────────────────── STACK ───────────────────────────────────
STACK = [
    ("AI / ML", "most of the last two years",
     ["PyTorch", "Transformers", "LoRA / PEFT", "timm", "scikit-learn", "XGBoost", "ONNX"]),
    ("LANGUAGES", "C/C++ I had to earn",
     ["Python", "C · C++", "Java", "TypeScript", "JavaScript", "Dart", "SQL"]),
    ("WEB & MOBILE", "REST first, always",
     ["React · Next.js", "Vue 3", "Spring Boot", "FastAPI · Flask", "Flutter", "Qt / QML", "Socket.IO"]),
    ("INFRA & DATA", "enough to ship it myself",
     ["Docker", "GitHub Actions", "AWS · Oracle Cloud", "NVIDIA CUDA", "Linux", "PostgreSQL", "Redis · SQLite"]),
]
LANGS = [("TypeScript", 34, "#3178c6"), ("Python", 28, "#e5b62b"), ("JavaScript", 9, "#c9b52d"),
         ("Dart", 9, "#00a3c4"), ("HTML", 6, "#e34c26"), ("Java", 4, "#b07219")]


def stack(theme):
    c = THEMES[theme]
    W, H = 1200, 560
    colw = (1200 - 128) / 4
    style = "@keyframes grow{from{width:0}to{width:1072px}} .cr{animation:grow 1.6s cubic-bezier(.2,.7,.2,1) .3s both}"
    cols = ""
    for i, (h, note, items) in enumerate(STACK):
        x = 64 + i * colw
        cols += t(x, 66, h, 16, c["accent"], MONO, 700, extra='letter-spacing="2"')
        cols += t(x, 94, note, 16, c["muted"], SERIF, 400, extra='font-style="italic"')
        for j, it in enumerate(items):
            cols += t(x, 140 + j * 33, it, 20, c["fg"], SANS, 500)
    total = sum(n for _, n, _ in LANGS)
    bx, bw, by = 64, 1072, 450
    seg, leg, cur = "", "", bx
    for k, (name, n, col) in enumerate(LANGS):
        w = bw * n / total
        seg += f'<rect x="{cur:.1f}" y="{by}" width="{max(w-3,1):.1f}" height="14" rx="4" fill="{col}"/>'
        cur += w
    lx = bx
    for name, n, col in LANGS:
        leg += f'<circle cx="{lx+6}" cy="{by+50}" r="6" fill="{col}"/>'
        leg += t(lx + 20, by + 56, f"{name} {n}", 16, c["mid"], MONO, 400)
        lx += 20 + (len(name) + len(str(n)) + 1) * 9.7 + 30
    body = f"""
      <rect width="{W}" height="{H}" fill="{c['bg']}" rx="16"/>
      {cols}
      <line x1="64" y1="390" x2="1136" y2="390" stroke="{c['line']}"/>
      {t(64, 428, "106 PUBLIC REPOS · BY MAIN LANGUAGE", 15, c['muted'], MONO, 600, extra='letter-spacing="1.5"')}
      <clipPath id="cp"><rect class="cr" x="64" y="{by-2}" width="1072" height="20"/></clipPath><g clip-path="url(#cp)">{seg}</g>
      {leg}
    """
    save("stack", theme, svg(W, H, body, style))


# ─────────────────────────────────── FOOTER ───────────────────────────────────
def footer(theme):
    c = THEMES[theme]
    W, H = 1200, 220
    px = dither(760, 18, 29, 13, 14, c["accent"], gap=3, power=1.4)
    style = "@keyframes blink{50%{opacity:0}} .cur{animation:blink 1.1s steps(1) infinite}"
    body = f"""
      <rect width="{W}" height="{H}" fill="{c['bg']}" rx="16"/>
      {px}
      {t(64, 58, "t = 0000 / the clean sample", 16, c['muted'], MONO, 500)}
      {t(62, 128, "Say something.", 62, c['fg'], SERIF, 500, extra='letter-spacing="-1"')}
      {t(64, 176, "bhargavadepu@outlook.com", 24, c['accent'], MONO, 500)}
      <rect class="cur" x="418" y="156" width="13" height="25" fill="{c['accent']}"/>
    """
    save("footer", theme, svg(W, H, body, style))


for th in THEMES:
    hero(th)
    for p in PROJECTS:
        card(p, th)
    timeline(th)
    stack(th)
    footer(th)
print("wrote", len(os.listdir(OUT)), "files")
