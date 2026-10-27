import sys, shutil, subprocess, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import HEAD, OUT, LOGO
from playwright.sync_api import sync_playwright

CAP = (pathlib.Path(__file__).parent / "capturas").resolve()
def img(name): return (CAP / name).as_uri()

EXTRA_CSS = """<style>
.top{position:absolute;left:96px;right:96px;top:250px}
.cap{font-weight:800;letter-spacing:-.025em;line-height:1.06;font-size:76px;color:var(--ink)}
.win{position:absolute;left:60px;width:960px;top:760px;height:700px;border-radius:28px;overflow:hidden;
     background:#0b1730;box-shadow:0 30px 80px rgba(0,0,0,.55),0 0 0 2px #1e3a6e}
.bar{height:46px;background:#13213d;display:flex;align-items:center;gap:12px;padding:0 22px}
.dot{width:14px;height:14px;border-radius:50%;background:#2a3f78}
.url{margin-left:18px;font-family:'IBM Plex Mono',monospace;font-size:22px;color:#94a3b8}
.view{position:absolute;left:0;top:46px;right:0;bottom:0;overflow:hidden}
.cam{position:absolute;left:0;top:0;transform-origin:0 0}
.cam img{position:absolute;left:0;top:0;display:block}
.ring{position:absolute;border:6px solid #3b82f6;border-radius:18px;box-shadow:0 0 0 9999px rgba(10,21,37,.45);opacity:0}
</style>"""

# Each scene: dur, eyebrow, caption, images [(file,w,h, fade_in_ms or None)], cam_from (x,y,w), cam_to (x,y,w), ring (x,y,w,h, start_ms) or None
SCENES = [
 dict(dur=3000, hook=True),
 dict(dur=4200, eb="Paso 1", cap="Entra a www.justibot.com.co", imgs=[("01_inicio.jpg",1568,744,None)],
      cf=(150,30,1000), ct=(220,330,600), ring=(245,588,282,48,1900)),
 dict(dur=5200, eb="Paso 2", cap="Crea tu cuenta: 1 mes gratis, sin tarjeta.",
      imgs=[("03_registro_arriba.jpg",1568,744,None),("05_registro_lleno_arriba.jpg",1568,744,1500)],
      cf=(540,30,500), ct=(560,300,470), ring=None),
 dict(dur=3800, eb="Paso 2", cap="Un clic y listo.", imgs=[("06_registro_lleno_abajo.jpg",1568,744,None)],
      cf=(560,330,470), ct=(590,430,420), ring=(615,642,333,46,1300)),
 dict(dur=4600, eb="Paso 3", cap="Pega tus radicados, uno por línea.", imgs=[("07_panel_radicados.jpg",1536,695,None)],
      cf=(310,80,900), ct=(690,180,760), ring=(1232,563,208,42,2200)),
 dict(dur=4600, eb="Paso 4", cap="JustiBot consulta las fuentes oficiales por ti.", imgs=[("16_detalle_proceso.jpg",1536,639,None)],
      cf=(310,20,900), ct=(310,90,760), ring=None),
 dict(dur=4800, eb="Paso 4", cap="Y te muestra cada actuación, en orden.", imgs=[("17_actuaciones.jpg",1536,639,None)],
      cf=(310,0,900), ct=(330,20,860), ring=None),
 dict(dur=4800, eb="Extra", cap="Calcula términos en días hábiles, con festivos.", imgs=[("18_terminos_activos.jpg",1536,695,None)],
      cf=(380,8,1010), ct=(400,124,880), ring=(408,535,870,62,2000)),
 dict(dur=4800, eb="Cada mañana", cap="Ves qué vence y qué se movió.", imgs=[("19_tu_dia_lleno.jpg",1536,695,None)],
      cf=(360,8,1010), ct=(365,150,700), ring=(372,487,606,116,1900)),
 dict(dur=4600, cta=True),
]
JS = r"""
const lerp=(a,b,t)=>a+(b-a)*t, ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
window.setT=function(t){
  const S=window.S;
  document.querySelectorAll('.a').forEach((el,i)=>{const p=Math.min(1,Math.max(0,(t-i*150)/520)),e=1-Math.pow(1-p,3);
    el.style.opacity=e; el.style.transform=`translateY(${40*(1-e)}px)`+(el.classList.contains('pulse')&&t>1500?` scale(${1+0.035*Math.sin((t-1500)/1200*6.283)})`:'');});
  const win=document.querySelector('.win'); if(!win) return;
  const wi=Math.min(1,Math.max(0,(t-150)/600)),we=1-Math.pow(1-wi,3);
  win.style.opacity=we; win.style.transform=`translateY(${60*(1-we)}px)`;
  const p=ease(Math.min(1,Math.max(0,(t-500)/(S.dur-900))));
  const x=lerp(S.cf[0],S.ct[0],p), y=lerp(S.cf[1],S.ct[1],p), w=lerp(S.cf[2],S.ct[2],p), s=960/w;
  document.querySelector('.cam').style.transform=`scale(${s}) translate(${-x}px,${-y}px)`;
  document.querySelectorAll('.fade').forEach(el=>{const f=+el.dataset.f; el.style.opacity=Math.min(1,Math.max(0,(t-f)/500));});
  const r=document.querySelector('.ring'); if(r){const q=Math.min(1,Math.max(0,(t-S.ring[4])/400)); r.style.opacity=q;}
};
"""

def scene_html(S):
    if S.get("hook"):
        body = ('<div class="page glow">'
                '<div class="h1 a" style="font-size:120px">Así funciona <span class="b">JustiBot.</span></div>'
                '<div class="body2 a">Del registro a tu primer reporte.</div></div>')
    elif S.get("cta"):
        body = ('<div class="page glow">'
                f'<img class="logo a" src="{LOGO}" style="width:480px">'
                '<div class="h2 a" style="font-size:72px;margin-top:44px">Tu reporte llega al correo todos los días.</div>'
                '<div class="body2 a">Haya o no novedades. Sin cobrar por radicado.</div>'
                '<div class="cta a pulse">Pruébalo gratis · www.justibot.com.co</div></div>')
    else:
        imgs = "".join(
            f'<img src="{img(f)}" style="width:{w}px;height:{h}px" class="{"fade" if fi else ""}" data-f="{fi or 0}">'
            for f,w,h,fi in S["imgs"])
        ring = ""
        if S.get("ring"):
            x,y,w,h,_ = S["ring"]; pad=10
            ring = f'<div class="ring" style="left:{x-pad}px;top:{y-pad}px;width:{w+2*pad}px;height:{h+2*pad}px"></div>'
        body = (f'<div class="page glow-tr" style="justify-content:flex-start"></div>'
                f'<div class="top"><div class="eyebrow a">{S["eb"]}</div><div class="rule a" style="margin:28px 0 34px"></div>'
                f'<div class="cap a">{S["cap"]}</div></div>'
                f'<div class="win" style="opacity:0"><div class="bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span>'
                f'<span class="url">www.justibot.com.co</span></div><div class="view"><div class="cam">{imgs}{ring}</div></div></div>')
    import json
    cfg = json.dumps({k:S.get(k) for k in ("dur","cf","ct","ring")})
    return HEAD.replace("var(--w)","1080px").replace("var(--h)","1920px") + EXTRA_CSS + body + f"<script>window.S={cfg};{JS}</script></body></html>"

def render(fps=30, only=None):
    tmp = OUT/"_demo"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(parents=True)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width":1080,"height":1920})
        n = 0
        for i,S in enumerate(SCENES):
            if only is not None and i not in only: continue
            hf = tmp/"scene.html"; hf.write_text(scene_html(S))
            pg.goto(hf.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
            frames = int(S["dur"]*fps/1000) if only is None else 1
            for k in range(frames):
                t = k*1000/fps if only is None else S["dur"]*0.75
                pg.evaluate(f"setT({t})")
                pg.screenshot(path=str(tmp/f"f{n:05d}.jpg"), type="jpeg", quality=93); n+=1
        b.close()
    if only is not None: return tmp
    out = OUT/"Video_demo_JustiBot.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",str(tmp/"f%05d.jpg"),
        "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest","-c:v","libx264","-pix_fmt","yuv420p",
        "-crf","18","-preset","medium","-c:a","aac","-movflags","+faststart",str(out)],check=True)
    shutil.rmtree(tmp); return out

if __name__ == "__main__":
    if sys.argv[1:] == ["preview"]:
        print(render(only=list(range(len(SCENES)))))
    else:
        print(render())
