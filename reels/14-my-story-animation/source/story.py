"""Animatic for the story reel: Ken Burns on Gemini stills, captions, voices, music.
Usage: python3 story.py plan | render"""
import json, sys, subprocess, os
V = "/home/user/Attract-clients/reels/14-my-story-animation/voice"
FPS, W, H = 30, 1080, 1920
O = lambda t: f"<b>{t}</b>"
# (image, duration, motion, caption, [(voice, offset)], extras)
S = [
 ("s01", 2.6, "in",   "كنت كاشيرة بسوبرماركت بهولندا", [], []),
 ("s02", 2.6, "out",  "وبنفس الوقت عم ادرس مساعدة طبيب اسنان", [], []),
 ("s03", 3.0, "in",   "وكل ليلة كنت شوف بنات عايشين الحياة اللي بحلم فيها", [], []),
 ("s04", 107/30, "clip:s04", "ماما… بدي اترك الشغل والمدرسة كمان", [], []),
 ("s05", 136/30, "clip:s05", "شو؟! هاد دخلك الوحيد يا ماما! كيف بدك تعيشي؟", [], []),
 ("s06", 156/30, "clip:s06", "اعطوني ست شهور بس… بوعدك انا قدها|واذا ما نجحت برجع عالمدرسة", [], []),
 ("s07", 2.8, "panr", "تركت الشغل والمدرسة… وبلشت من الصفر", [], []),
 ("s08", 2.4, "in",   "كل يوم عم ابني حالي", [], []),
 ("s09", 2.2, "out",  "سهر… وتعب", [], []),
 ("s10", 2.8, "in",   f"خلال {O('6 شهور')}", [], []),
 ("s11", 2.4, "in", None, [], []),
 ("s11", 122/30, "clip:s11", "يلا نعلّم البنات كيف يعملوا نفس الشي!", [], []),
 ("s12", 3.6, "out",  "وصرت علّم البنات", [], ["badges"]),
 ("s13", 10.6, "panl", None, [("6-woman1", 0.3), ("7-woman2", 3.5), ("8-woman3", 7.3)], []),
 ("s14", 3.0, "in",   "وبعدها تزوجت شريك حياتي", [], []),
 ("s15", 3.8, "in",   "وانتقلنا عبلد احلامنا|ومننتظر بنوتتنا", [], []),
 ("s16", 166/30+1.2, "clip:s16", "من كاشيرة بالسوبرماركت… لهون|وهلق دورك انتي", [], []),
]
CAP13 = [("شكرا كتير الك… كتير استفدنا", 0.3, 3.4), ("والله غيرتيلي حياتي… ما بعرف كيف بدي اشكرك", 3.5, 7.2),
         (f"يا الله!! عملت اول {O('عشر آلاف دولار')} بفضلك!!", 7.3, 10.6)]

def starts():
    t, out = 0.0, []
    for s in S: out.append(t); t += s[1]
    return out, t

def plan():
    st, dur = starts()
    caps = []  # (text, t0, t1)
    for (img, d, mv, cap, vs, ex), t0 in zip(S, st):
        if cap: caps.append((cap, t0 + 0.15, t0 + d - 0.05))
        if img == "s13":
            for c, a, b in CAP13: caps.append((c, t0 + a, t0 + b))
    badges = []
    t12 = st[[s[0] for s in S].index("s12")]
    for i, (n, a) in enumerate([("10K", 0.5), ("20K", 1.3), ("30K", 2.1)]):
        badges.append((n, t12 + a, t12 + 3.6, i))
    json.dump({"caps": caps, "badges": badges, "dur": dur}, open("plan.json", "w"), ensure_ascii=False)
    print("duration", round(dur, 2))

def render():
    import numpy as np
    from PIL import Image
    st, dur = starts()
    pl = json.load(open("plan.json"))
    N = int(round(dur * FPS))
    capimg = [Image.open(f"caps/c{i:02d}.png") for i in range(len(pl["caps"]))]
    badimg = [Image.open(f"caps/b{i}.png") for i in range(3)]
    srcs = {s[0]: Image.open(f"img/{s[0]}.jpg") for s in S}
    NF = {c: len(os.listdir(f"clips/fr_{c}")) for c in ["s04","s05","s06","s11","s16"]}
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "video.mp4"], stdin=subprocess.PIPE)
    ease = lambda x: x * x * (3 - 2 * x)
    for f in range(N):
        t = f / FPS
        k = max(i for i, a in enumerate(st) if a <= t + 1e-9)
        img, d, mv = S[k][0], S[k][1], S[k][2]
        p = ease(min(1, (t - st[k]) / d))
        if mv.startswith("clip:"):
            c = mv[5:]; fi = min(int((t - st[k]) * FPS) + 1, NF[c])
            fr = Image.open(f"clips/fr_{c}/{fi:04d}.jpg").convert("RGBA")
        else:
          src = srcs[img]; sw, sh = src.size
          z0, z1, x0, x1 = {"in": (1.0, 1.12, .5, .5), "out": (1.12, 1.0, .5, .5), "panl": (1.18, 1.18, .62, .38), "panr": (1.15, 1.15, .4, .6)}[mv]
          z = z0 + (z1 - z0) * p; cx = x0 + (x1 - x0) * p
          cw, ch = sw / z, sh / z
          left = min(max(cx * sw - cw / 2, 0), sw - cw); top = (sh - ch) / 2
          fr = src.resize((W, H), Image.BICUBIC, box=(left, top, left + cw, top + ch)).convert("RGBA")
        if t - st[k] < 0.12:  # quick fade from previous cut feel
            pass
        for i, (txt, a, b) in enumerate(pl["caps"]):
            if a <= t < b:
                im = capimg[i]; al = min(1, (t - a) / 0.18, (b - t) / 0.12)
                if al < 1: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * al)))
                fr.alpha_composite(im)
        for (n, a, b, i) in pl["badges"]:
            if a <= t < b:
                q = ease(min(1, (t - a) / 0.25)); im = badimg[i]
                if q < 1: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * q)))
                fr.alpha_composite(im, (0, int((1 - q) * 40)))
        enc.stdin.write(fr.convert("RGB").tobytes())
    enc.stdin.close(); enc.wait()
    # audio
    ins, flt, lab = ["-i", "music.mp3"], [], []
    flt.append(f"[1:a]volume=0.22,afade=t=in:d=1,afade=t=out:st={dur-2.5}:d=2.5,atrim=0:{dur}[m]")
    j = 2
    for (img, d, mv, cap, vs, ex), t0 in zip(S, st):
        if mv.startswith("clip:"):
            ins += ["-i", f"clips/n_{mv[5:]}.mp4"]; ms = int(t0 * 1000)
            flt.append(f"[{j}:a]adelay={ms}|{ms},volume=1.0[v{j}]"); lab.append(f"[v{j}]"); j += 1
        for v, off in vs:
            ins += ["-i", f"{V}/{v}.mp3"]
            ms = int((t0 + off) * 1000)
            flt.append(f"[{j}:a]adelay={ms}|{ms},volume=1.0[v{j}]"); lab.append(f"[v{j}]"); j += 1
    flt.append(f"[m]{''.join(lab)}amix=inputs={1+len(lab)}:duration=first:normalize=0,alimiter=limit=0.95[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "video.mp4"] + ins + ["-filter_complex", ";".join(flt),
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", "story_v1.mp4"], check=False)

if __name__ == "__main__":
    {"plan": plan, "render": render}[sys.argv[1]]()
