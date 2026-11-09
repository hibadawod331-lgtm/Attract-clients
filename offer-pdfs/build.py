"""Arabic offer PDFs: turns each .md under ar/ into a branded RTL HTML file.
Usage: python3 build.py [path/to/file.md ...]   (no args = all)
Then: node pdf.js <html files...>
Markup:
  @kind lesson|worksheet, @module, @title, @subtitle   header fields
  ## heading        ### small heading
  - bullet          [] checkbox line      > callout (consecutive lines = one box)
  ___ (line alone)  writing lines (___3 = 3 lines)
  | a | b |         table (first row = header)
  **bold** inline
"""
import base64, glob, html, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(ROOT, "fonts")


def font(w, latin=False):
    n = f"ibm-plex-sans-arabic-{'latin-' if latin else ''}{w}.woff2"
    b = base64.b64encode(open(os.path.join(F, n), "rb").read()).decode()
    rng = ";unicode-range:U+0000-00FF,U+2000-206F" if latin else ""
    return f"@font-face{{font-family:P;font-weight:{w};src:url(data:font/woff2;base64,{b}){rng}}}"


FONTS = "".join(font(w, l) for w in (400, 500, 700) for l in (False, True))

CSS = FONTS + """
@page{size:A4;margin:24mm 20mm 22mm}
*{box-sizing:border-box}
html{font-family:P;color:#1d1d1f;font-size:11.5pt;line-height:1.85}
body{margin:0}
.cover{height:251mm;display:flex;flex-direction:column;justify-content:center;align-items:flex-start;page-break-after:always;position:relative}
.cover .tag{background:#F2531E;color:#fff;font-weight:500;font-size:10pt;padding:4px 14px;border-radius:20px}
.cover .mod{font-weight:500;color:#F2531E;font-size:15pt;margin-top:34px}
.cover h1{font-weight:700;font-size:38pt;line-height:1.25;margin:6px 0 18px}
.cover .sub{font-size:13pt;color:#555;border-top:3px solid #F2531E;padding-top:14px;max-width:120mm}
.cover .by{position:absolute;bottom:0;font-size:10.5pt;color:#888;direction:ltr}
h2{font-weight:700;font-size:17pt;line-height:1.4;margin:30px 0 12px;padding-bottom:8px;border-bottom:2px solid #F2531E;page-break-after:avoid}
h2:first-child{margin-top:0}
h3{font-weight:700;font-size:12.5pt;margin:22px 0 6px;color:#F2531E;page-break-after:avoid}
p{margin:0 0 10px}
ul{margin:0 0 12px;padding:0 22px 0 0}
li{margin:0 0 4px}
li::marker{color:#F2531E}
.box{line-height:2.2;background:#FEF0EA;border-right:4px solid #F2531E;padding:12px 18px;margin:12px 0 16px;border-radius:4px;page-break-inside:avoid}
.box p{margin:0 0 8px}.box p:last-child{margin:0}
.lines{margin:4px 0 16px;page-break-inside:avoid}
.lines i{display:block;height:30px;border-bottom:1px solid #cfcfcf}
.chk{margin:0 0 6px;padding-right:26px;position:relative}
.cb{display:inline-block;width:12px;height:12px;border:1.5px solid #F2531E;border-radius:3px;vertical-align:-1px;margin-left:5px}
.chk:before{content:"";position:absolute;right:0;top:6px;width:13px;height:13px;border:1.5px solid #F2531E;border-radius:3px}
table{width:100%;border-collapse:collapse;margin:8px 0 18px;font-size:10pt;line-height:1.6}
th{background:#F2531E;color:#fff;font-weight:500;text-align:right;padding:7px 9px}
td{border:1px solid #e3e3e3;padding:7px 9px;vertical-align:top;height:34px}
tr{page-break-inside:avoid}
.kv td:first-child{width:45%;font-weight:500;background:#FEF0EA}
tr:nth-child(even) td{background:#fafafa}
b,strong{font-weight:700}
.ws-head{border-bottom:3px solid #F2531E;padding-bottom:12px;margin-bottom:22px}
.ws-head .k{color:#F2531E;font-weight:500;font-size:10pt}
.ws-head h1{font-size:24pt;margin:2px 0 0;line-height:1.35}
.ws-head .sub{color:#666;font-size:10.5pt}
"""


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = s.replace("☐", '<span class="cb"></span>')
    return s.replace("_______________", '<span style="display:inline-block;min-width:120px;border-bottom:1px solid #999"></span>')


def render(md):
    md = re.sub("[\u064B-\u0652]", "", md)  # no tashkeel
    meta, body, i = {}, [], 0
    L = md.split("\n")
    while i < len(L) and L[i].startswith("@"):
        k, _, v = L[i][1:].partition(" ")
        meta[k] = v.strip()
        i += 1
    while i < len(L):
        ln = L[i].rstrip()
        if not ln:
            i += 1; continue
        if ln.startswith("### "):
            body.append(f"<h3>{inline(ln[4:])}</h3>")
        elif ln.startswith("## "):
            body.append(f"<h2>{inline(ln[3:])}</h2>")
        elif ln.startswith(">"):
            ps = []
            while i < len(L) and L[i].startswith(">"):
                t = L[i][1:].strip()
                if t: ps.append(f"<p>{inline(t)}</p>")
                i += 1
            body.append('<div class="box">' + "".join(ps) + "</div>"); continue
        elif ln.startswith("- "):
            it = []
            while i < len(L) and L[i].startswith("- "):
                it.append(f"<li>{inline(L[i][2:])}</li>"); i += 1
            body.append("<ul>" + "".join(it) + "</ul>"); continue
        elif ln.startswith("[] "):
            body.append(f'<p class="chk">{inline(ln[3:])}</p>')
        elif re.fullmatch(r"___(\d*)", ln):
            n = int(ln[3:] or 2)
            body.append('<div class="lines">' + "<i></i>" * n + "</div>")
        elif ln.startswith("|"):
            rows = []
            while i < len(L) and L[i].startswith("|"):
                rows.append([c.strip() for c in L[i].strip().strip("|").split("|")]); i += 1
            if not any(rows[0]):
                b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
                body.append(f'<table class="kv"><tbody>{b}</tbody></table>'); continue
            h = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            body.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"); continue
        else:
            body.append(f"<p>{inline(ln)}</p>")
        i += 1
    if meta.get("kind") == "worksheet":
        top = (f'<div class="ws-head"><div class="k">ورقة عمل · {inline(meta.get("module",""))}</div>'
               f'<h1>{inline(meta["title"])}</h1><div class="sub">{inline(meta.get("subtitle",""))}</div></div>')
    else:
        top = (f'<section class="cover"><span class="tag">برنامج الإرشاد الفردي</span>'
               f'<div class="mod">{inline(meta.get("module",""))}</div><h1>{inline(meta["title"])}</h1>'
               f'<div class="sub">{inline(meta.get("subtitle",""))}</div><div class="by">@itscoachhiba</div></section>')
    head = html.escape(f'{meta.get("module","")} · {meta["title"]}')
    return (f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
            f'<meta name="running-head" content="{head}"><title>{html.escape(meta["title"])}</title>'
            f"<style>{CSS}</style></head><body>{top}{''.join(body)}</body></html>")


files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, "ar", "**", "*.md"), recursive=True))
for f in files:
    out = f[:-3] + ".html"
    open(out, "w", encoding="utf-8").write(render(open(f, encoding="utf-8").read()))
    print(out)
