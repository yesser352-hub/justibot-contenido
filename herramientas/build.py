import os, sys, subprocess, shutil, pathlib
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent.resolve()
OUT = ROOT / "out"
NM = ROOT / "node_modules/@fontsource"
LOGO = (ROOT / "logo.png").as_uri()

HEAD = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="{(NM/'ibm-plex-mono/500.css').as_uri()}">
<link rel="stylesheet" href="{(NM/'noto-color-emoji/index.css').as_uri()}">
<style>
:root{{--bg:#0a1525;--bg2:#0f1f35;--ink:#f1f5f9;--ink2:#cbd5e1;--mute:#94a3b8;--acc:#3b82f6;--soft:#8fbaff;--line:#2a3f78}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:var(--w);height:var(--h);overflow:hidden;background:var(--bg)}}
body{{font-family:Inter,'Noto Color Emoji',sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}}
.page{{position:absolute;inset:0;padding:0 96px;display:flex;flex-direction:column;justify-content:center}}
.glow{{background:radial-gradient(ellipse 60% 45% at 50% 48%,#1d4ed8 0%,rgba(29,78,216,.35) 35%,rgba(10,21,37,0) 75%),var(--bg)}}
.glow-tr{{background:radial-gradient(ellipse 70% 50% at 88% 6%,#1d4ed8 0%,rgba(29,78,216,.25) 40%,rgba(10,21,37,0) 75%),var(--bg)}}
.flat{{background:var(--bg)}}
.eyebrow{{font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:30px;letter-spacing:.18em;text-transform:uppercase;color:var(--soft)}}
.rule{{width:120px;height:6px;background:var(--acc);margin:34px 0 40px}}
.h1{{font-weight:800;letter-spacing:-.03em;line-height:1;font-size:104px}}
.h2{{font-weight:800;letter-spacing:-.025em;line-height:1.04;font-size:88px}}
.term{{font-weight:800;letter-spacing:-.04em;line-height:.92;font-size:200px;color:var(--acc)}}
.body{{font-weight:600;font-size:50px;line-height:1.3;color:var(--ink);margin-top:44px}}
.body2{{font-weight:500;font-size:46px;line-height:1.35;color:var(--ink2);margin-top:40px}}
.src{{font-family:'IBM Plex Mono',monospace;font-size:24px;color:var(--mute);margin-top:44px}}
.foot{{position:absolute;left:96px;bottom:110px;font-family:'IBM Plex Mono',monospace;font-size:28px;letter-spacing:.2em;color:var(--mute)}}
.b{{color:var(--acc)}}
.box{{border:2px solid var(--line);background:var(--bg2);padding:44px;margin-top:48px}}
ul.list{{list-style:none;margin-top:44px}}
ul.list li{{position:relative;padding-left:44px;font-weight:600;font-size:46px;line-height:1.3;color:var(--ink2);margin-bottom:34px}}
ul.list li:before{{content:"";position:absolute;left:0;top:24px;width:16px;height:16px;background:var(--acc)}}
.logo{{width:430px;height:auto;margin-left:-24px;display:block}}
.cta{{display:inline-block;align-self:flex-start;background:var(--acc);color:#fff;font-weight:700;font-size:38px;padding:34px 52px;border-radius:999px;margin-top:52px}}
.bubble{{font-weight:600;font-size:56px;line-height:1.25;padding:44px 48px;max-width:840px}}
.in{{background:#e2e8f0;color:#0a1525;border-radius:48px 48px 48px 10px;align-self:flex-start}}
.out{{background:var(--acc);color:#fff;border-radius:48px 48px 10px 48px;align-self:flex-end}}
.big{{font-weight:800;letter-spacing:-.045em;line-height:.9}}
</style></head><body>"""

def page(cls, inner):
    return f'<div class="page {cls}">{inner}</div>'

CTA = lambda line, sub: f'<img class="logo a" src="{LOGO}"><div class="h2 a" style="font-size:70px;margin-top:40px">{line}</div><div class="body2 a">{sub}</div><div class="cta a">Pruébalo gratis · www.justibot.com.co</div>'

GLOSARIO = [
 page("glow", '<div class="eyebrow">Glosario judicial</div><div class="rule"></div><div class="h1"><span class="b">4 palabras</span> del juzgado que nadie te explica bien.</div>') + '<div class="foot">DESLIZA →</div>',
 page("flat", '<div class="eyebrow">01 / 04</div><div class="rule"></div><div class="term">Auto</div><div class="body">Decisión del juez que no es sentencia: impulsa el proceso o resuelve un asunto dentro de él.</div>'),
 page("glow", '<div class="eyebrow">02 / 04</div><div class="rule"></div><div class="term">Estado</div><div class="body">Listado que publica la secretaría del despacho para notificar los autos a las partes.</div>'),
 page("flat", '<div class="eyebrow">03 / 04</div><div class="rule"></div><div class="term" style="font-size:176px">Traslado</div><div class="body">Plazo que se le da a una parte para conocer un escrito o decisión y pronunciarse sobre él.</div>'),
 page("glow", '<div class="eyebrow">04 / 04</div><div class="rule"></div><div class="term" style="font-size:156px">Ejecutoria</div><div class="body">Cuando la providencia queda en firme. Por regla general, 3 días después de notificada si no se interpuso recurso.</div><div class="src">Art. 302, Código General del Proceso</div>'),
 page("flat", CTA("Los estados salen todos los días. Tu reporte también.", "JustiBot vigila tus procesos en fuentes oficiales y te envía el reporte al correo, sin cobrar por radicado.")),
]

VACANCIA = [
 page("glow", '<div class="eyebrow">Diciembre · Rama Judicial</div><div class="rule"></div><div class="h1">Llega la <span class="b">vacancia judicial.</span> Revisa esto antes del 20.</div>') + '<div class="foot">DESLIZA →</div>',
 page("flat", '<div class="eyebrow">01 · Cuándo</div><div class="rule"></div><div class="big b" style="font-size:180px">20 dic</div><div class="h2" style="font-size:64px;color:var(--mute);margin:26px 0">hasta el</div><div class="big" style="font-size:180px">10 ene</div><div class="body2">Vacancia judicial colectiva, días inclusive. Algunos despachos atienden por turnos.</div><div class="src">Art. 146, Ley 270 de 1996</div>'),
 page("glow", '<div class="eyebrow">02 · Términos</div><div class="rule"></div><div class="h2">Los días de vacancia <span class="b">no se cuentan</span> en tus términos.</div><div class="box"><div style="font-weight:500;font-size:40px;line-height:1.38;color:var(--ink2)">En los términos de días no se toman en cuenta los de vacancia judicial ni los días en que el despacho esté cerrado.</div></div><div class="src">Art. 118, Código General del Proceso</div>'),
 page("flat", '<div class="eyebrow">03 · Antes del 20</div><div class="rule"></div><div class="h2">Tu checklist de cierre</div><ul class="list"><li>Revisa con calma los estados de los últimos días hábiles.</li><li>Radica memoriales con tiempo, no el último día.</li><li>Anota en qué va cada término al cierre del despacho.</li></ul>'),
 page("glow", '<div class="eyebrow">04 · En enero</div><div class="rule"></div><div class="h2">Retoma el conteo en el <span class="b">primer día hábil.</span></div><div class="body2">Ojo: en 2027 el festivo de Reyes se corre al lunes 11 de enero. Revisa el calendario antes de contar.</div>'),
 page("flat", CTA("No se va de vacaciones.", "Vigila tus procesos en fuentes oficiales y te envía el reporte al correo todos los días, sin cobrar por radicado.")),
]

# Reels: scenes = (duration_ms, html). Elements with class "a" rise in staggered; [data-count] counts up.
REEL_CUENTA = [
 (3000, page("glow", '<div class="eyebrow a">Haz la cuenta</div><div class="rule a"></div><div class="h1 a" style="font-size:124px">50 procesos.</div><div class="h2 a" style="font-size:72px;color:var(--ink2);margin-top:36px">2 minutos revisando cada uno.</div><div class="h2 a b" style="font-size:72px;margin-top:36px">Todos los días hábiles.</div>')),
 (3400, page("glow", '<div class="eyebrow a">Al mes</div><div class="rule a"></div><div class="h2 a" style="font-size:66px;color:var(--ink2)">50 × 2 min × 22 días</div><div class="big b a" style="font-size:270px;margin-top:30px" data-count="2200" data-from="500" data-dur="1500">2200</div><div class="h2 a" style="font-size:76px;margin-top:20px">minutos.</div>')),
 (3200, page("glow", '<div class="eyebrow a">En horas</div><div class="rule a"></div><div class="h2 a" style="font-size:72px;color:var(--ink2)">Más de</div><div class="big a pulse" style="font-size:310px;margin-top:10px">36 h</div><div class="h2 a b" style="font-size:66px;margin-top:30px">al mes entrando a portales. Casi una semana de trabajo.</div>')),
 (4200, page("glow", CTA("Vigila tus procesos en fuentes oficiales.", "Te manda el reporte al correo todos los días, sin cobrar por radicado.").replace('class="cta a"','class="cta a pulse"'))),
]

REEL_HUMOR = [
 (3200, page("glow-tr", '<div class="eyebrow a">Cliente · 10:47 p. m.</div><div class="h2 a" style="font-size:72px;margin:30px 0 70px">Te escribe un cliente:</div><div class="bubble in a pop">Doctora, ¿cómo va mi proceso?</div>')),
 (4400, page("glow-tr", '<div class="eyebrow a">Tú · desde las 7 a. m.</div><div class="h2 a" style="font-size:66px;margin:30px 0 70px">Tú, que ya leíste el reporte de JustiBot en el desayuno:</div><div class="bubble out a pop">Hoy salió auto en su proceso. Ya lo revisé y mañana le cuento con calma.</div>')),
 (4200, page("glow", CTA("Tu reporte llega al correo todos los días.", "Haya o no novedades. Sin cobrar por radicado.").replace('class="cta a"','class="cta a pulse"'))),
]

ANIM_JS = r"""
window.setT = function(t){
  const els=[...document.querySelectorAll('.a')];
  els.forEach((el,i)=>{
    const start = el.classList.contains('pop') ? 700 : i*160;
    let p=Math.min(1,Math.max(0,(t-start)/520)); const e=1-Math.pow(1-p,3);
    if(el.classList.contains('pop')){ const s=0.85+0.15*(1-Math.pow(1-p,3)) + (p<1?0.04*Math.sin(p*Math.PI):0);
      el.style.transform=`scale(${s})`; el.style.transformOrigin=el.classList.contains('out')?'right bottom':'left bottom'; }
    else el.style.transform=`translateY(${40*(1-e)}px)`;
    el.style.opacity=e;
    if(el.classList.contains('pulse') && t>1400){ const k=1+0.035*Math.sin((t-1400)/1200*2*Math.PI); el.style.transform+=` scale(${k})`; }
    if(el.dataset.count){ const f=+el.dataset.from, d=+el.dataset.dur, n=+el.dataset.count; const q=Math.min(1,Math.max(0,(t-f)/d)); el.textContent=Math.round(n*(1-Math.pow(1-q,3))).toLocaleString('es-CO'); }
  });
};
"""

def shot_slides(b, name, slides):
    d = OUT / name; d.mkdir(parents=True, exist_ok=True)
    pg = b.new_page(viewport={"width":1080,"height":1350})
    files=[]
    for i,s in enumerate(slides,1):
        hf = d / f"_{i}.html"; hf.write_text(HEAD.replace("var(--w)","1080px").replace("var(--h)","1350px")+s+"</body></html>")
        pg.goto(hf.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        f = d / f"{name}_{i}.png"; pg.screenshot(path=str(f)); files.append(f); hf.unlink()
    pg.close(); return files

def render_reel(b, name, scenes, fps=30):
    tmp = OUT / f"_{name}"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(parents=True)
    pg = b.new_page(viewport={"width":1080,"height":1920})
    n=0
    # Portada: los primeros fotogramas muestran la primera escena ya completa,
    # para que Instagram, TikTok y Facebook no tomen un cuadro vacío como portada.
    dur0, html0 = scenes[0]
    hf = tmp / "scene.html"; hf.write_text(HEAD.replace("var(--w)","1080px").replace("var(--h)","1920px")+html0+f"<script>{ANIM_JS}</script></body></html>")
    pg.goto(hf.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
    pg.evaluate(f"setT({max(2500, dur0-200)})")
    pg.screenshot(path=str(tmp/"cover.png"), type="png")
    for _ in range(3):
        shutil.copy(tmp/"cover.png", tmp/f"f{n:05d}.png"); n+=1
    for dur, html in scenes:
        hf = tmp / "scene.html"; hf.write_text(HEAD.replace("var(--w)","1080px").replace("var(--h)","1920px")+html+f"<script>{ANIM_JS}</script></body></html>")
        pg.goto(hf.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        for k in range(int(dur*fps/1000)):
            pg.evaluate(f"setT({k*1000/fps})")
            pg.screenshot(path=str(tmp/f"f{n:05d}.png"), type="png"); n+=1
    pg.close()
    out = OUT / f"{name}.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",str(tmp/"f%05d.png"),
                    "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest",
                    "-c:v","libx264","-pix_fmt","yuv420p","-crf","18","-preset","medium","-c:a","aac","-movflags","+faststart",str(out)],check=True)
    shutil.copy(tmp/"f00060.png", OUT/f"{name}_preview1.png")
    shutil.copy(tmp/f"f{n-30:05d}.png", OUT/f"{name}_previewEnd.png")
    shutil.rmtree(tmp); return out

if __name__=="__main__":
    what = sys.argv[1:] or ["slides","reels"]
    with sync_playwright() as p:
        b=p.chromium.launch()
        if "slides" in what:
            shot_slides(b,"glosario",GLOSARIO); shot_slides(b,"vacancia",VACANCIA)
        if "reels" in what:
            render_reel(b,"reel_cuenta",REEL_CUENTA); render_reel(b,"reel_humor",REEL_HUMOR)
        b.close()
    print("done")
