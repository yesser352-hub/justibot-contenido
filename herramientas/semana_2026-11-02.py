"""Semana del lunes 2 al domingo 8 de noviembre de 2026.
Uso: python3 semana_2026-11-02.py [slides] [reels] [tutorial] [historias]
"""
import sys, json, shutil, subprocess, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import HEAD, page, CTA, shot_slides, render_reel, OUT, LOGO
from playwright.sync_api import sync_playwright
import demo  # escenas con capturas (ventana de navegador + cámara)

def cta_pulse(line, sub):
    return CTA(line, sub).replace('class="cta a"', 'class="cta a pulse"')

# ---------- Jueves 5: carrusel educativo (6 láminas) ----------
TERMINOS = [
 page("glow", '<div class="eyebrow">Art. 118 · Código General del Proceso</div><div class="rule"></div>'
      '<div class="h1">¿Desde cuándo <span class="b">corre</span> tu término?</div>'
      '<div class="body2">4 reglas para contarlo bien.</div>') + '<div class="foot">DESLIZA →</div>',
 page("flat", '<div class="eyebrow">01 / 04 · Inicio</div><div class="rule"></div>'
      '<div class="h2">Corre desde el <span class="b">día siguiente</span> a la notificación.</div>'
      '<div class="body2">Así pasa con el término concedido fuera de audiencia. Si se concede en audiencia, corre desde que se otorga para quienes debían asistir.</div>'
      '<div class="src">Art. 118, Código General del Proceso</div>'),
 page("glow", '<div class="eyebrow">02 / 04 · Días</div><div class="rule"></div>'
      '<div class="h2">En los términos de días <span class="b">no cuentan</span> la vacancia ni los días con el juzgado cerrado.</div>'
      '<div class="body2">Tampoco los fines de semana ni los festivos: se cuentan días hábiles.</div>'
      '<div class="src">Art. 118 CGP · Art. 62, Ley 4 de 1913</div>'),
 page("flat", '<div class="eyebrow">03 / 04 · Meses y años</div><div class="rule"></div>'
      '<div class="h2">Vencen el <span class="b">mismo día</span> del mes o del año.</div>'
      '<div class="box"><div style="font-weight:600;font-size:42px;line-height:1.35;color:var(--ink)">Ejemplo: si empezó a correr el 10 de noviembre, un término de un mes vence el 10 de diciembre.</div></div>'
      '<div class="body2" style="font-size:40px">Si ese día no existe, vence el último del mes. Si cae en día inhábil, pasa al primer día hábil siguiente.</div>'),
 page("glow", '<div class="eyebrow">04 / 04 · Al despacho</div><div class="rule"></div>'
      '<div class="h2">Con el expediente <span class="b">al despacho</span>, el término no corre.</div>'
      '<div class="body2">Se reanuda al día siguiente de la notificación de la providencia que se dicte. Si es de «cúmplase», desde el tercer día siguiente a su fecha.</div>'
      '<div class="src">Art. 118, Código General del Proceso</div>'),
 page("flat", CTA("Cuenta tus términos en segundos.",
      "La calculadora de JustiBot cuenta en días hábiles, con festivos y vacancia. Y tu reporte llega al correo todos los días.")),
]

# ---------- Lunes 2 (festivo): Reel de humor ----------
REEL_FESTIVO_HUMOR = [
 (3000, page("glow", '<div class="eyebrow a">Lunes festivo · 2 de noviembre</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:118px">El litigante <span class="b">descansando</span> en festivo.</div>')),
 (3000, page("glow-tr", '<div class="eyebrow a">9:00 a. m.</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">El plan del día:</div>'
             '<div class="bubble in a pop">Hoy no abro ningún portal.</div>')),
 (3000, page("glow-tr", '<div class="eyebrow a">9:07 a. m.</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Siete minutos después:</div>'
             '<div class="bubble in a pop">Bueno… solo reviso un proceso.</div>')),
 (3400, page("glow-tr", '<div class="eyebrow a">11:40 a. m.</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Dos horas y media después:</div>'
             '<div class="bubble in a pop">Catorce procesos, tres pestañas abiertas y el tinto frío.</div>')),
 (4200, page("glow", cta_pulse("Descansa de verdad.",
             "JustiBot vigila tus procesos y te envía el reporte al correo todos los días, haya o no novedades."))),
]

# ---------- Sábado 7: pregunta a la comunidad (este o ese) ----------
def opcion(n, a, b):
    return (2800, page("glow", f'<div class="eyebrow a">{n} / 4 · Escoge uno</div><div class="rule a"></div>'
            f'<div class="h2 a" style="font-size:100px">{a}</div>'
            f'<div class="h2 a" style="font-size:64px;font-weight:600;margin:40px 0;color:var(--mute)">o</div>'
            f'<div class="h2 a b" style="font-size:100px">{b}</div>'))
REEL_ESTE_O_ESE = [
 (3000, page("glow", '<div class="eyebrow a">Sábado · este o ese</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:124px">Versión <span class="b">litigante.</span></div>'
             '<div class="body2 a">Escoge rápido, sin pensarlo mucho.</div>')),
 opcion(1, "Radicar a las 7&nbsp;a.&nbsp;m.", "a las 11:58&nbsp;p.&nbsp;m."),
 opcion(2, "Audiencia virtual", "presencial"),
 opcion(3, "Procesos en Excel", "en cuaderno"),
 opcion(4, "Tinto", "café con leche"),
 (4400, page("glow", cta_pulse("¿Cuáles escogiste? Cuéntanos en los comentarios.",
             "Y mientras decides, JustiBot vigila tus procesos y te envía el reporte al correo todos los días."))),
]

# ---------- Domingo 8: humor ligero ----------
REEL_DOMINGO = [
 (3000, page("glow", '<div class="eyebrow a">Domingo · 6:30 p. m.</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:118px">Tu cerebro, un domingo a las <span class="b">6:30 p. m.</span></div>')),
 (3300, page("glow-tr", '<div class="eyebrow a">Tu cerebro</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Sin que nadie le pregunte:</div>'
             '<div class="bubble in a pop">¿Y si mañana salió algo en algún proceso?</div>')),
 (3800, page("glow-tr", '<div class="eyebrow a">Tú</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Tú, que ya sabes cómo arranca tu lunes:</div>'
             '<div class="bubble out a pop">Mañana lo veo en el reporte, con el café.</div>')),
 (4200, page("glow", cta_pulse("Que el domingo sea domingo.",
             "JustiBot te envía el reporte al correo todos los días, haya o no novedades."))),
]

# ---------- Viernes 6: Reel tutorial con capturas ----------
TUTORIAL = [
 dict(dur=3000, html=page("glow", '<div class="eyebrow a">Tutorial · JustiBot</div><div class="rule a"></div>'
      '<div class="h1 a" style="font-size:118px">Calcula un término en <span class="b">días hábiles.</span></div>'
      '<div class="body2 a">Sin contar con los dedos en el calendario.</div>')),
 dict(dur=4200, eb="Paso 1", cap="Escribe qué hay que hacer y desde cuándo cuenta.", imgs=[("10_terminos.jpg",1536,695,None)],
      cf=(300,60,1100), ct=(390,200,800), ring=(410,311,446,36,1900)),
 dict(dur=4200, eb="Paso 2", cap="Elige cuántos días y si descuentas la vacancia.", imgs=[("10_terminos.jpg",1536,695,None)],
      cf=(390,200,800), ct=(700,220,700), ring=(872,311,428,36,1600)),
 dict(dur=4400, eb="Paso 3", cap="Te da la fecha: salta fines de semana y festivos.", imgs=[("10_terminos.jpg",1536,695,None)],
      cf=(700,220,700), ct=(395,300,700), ring=(475,382,245,52,1500)),
 dict(dur=4400, eb="Paso 4", cap="Guárdalo y sigue su cuenta regresiva.", imgs=[("18_terminos_activos.jpg",1536,695,None)],
      cf=(380,200,1010), ct=(390,330,1000), ring=(400,532,975,70,1900)),
 dict(dur=4400, html=page("glow", cta_pulse("Tus términos, en orden.",
      "Calculadora en días hábiles con festivos y vacancia, y el reporte al correo todos los días."))),
]

def tut_html(S):
    if "html" in S:
        cfg = json.dumps({"dur": S["dur"]})
        return HEAD.replace("var(--w)","1080px").replace("var(--h)","1920px") + demo.EXTRA_CSS + S["html"] + \
               f"<script>window.S={cfg};{demo.JS}</script></body></html>"
    return demo.scene_html(S)

def render_tutorial(b, name, scenes, fps=30):
    tmp = OUT/f"_{name}"; shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(parents=True)
    pg = b.new_page(viewport={"width":1080,"height":1920}); n = 0
    def load(S):
        hf = tmp/"scene.html"; hf.write_text(tut_html(S))
        pg.goto(hf.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
    # Portada: primera escena completa en los primeros fotogramas
    load(scenes[0]); pg.evaluate(f"setT({scenes[0]['dur']-200})")
    pg.screenshot(path=str(tmp/"cover.png"))
    for _ in range(3): shutil.copy(tmp/"cover.png", tmp/f"f{n:05d}.png"); n += 1
    for S in scenes:
        load(S)
        for k in range(int(S["dur"]*fps/1000)):
            pg.evaluate(f"setT({k*1000/fps})"); pg.screenshot(path=str(tmp/f"f{n:05d}.png")); n += 1
    pg.close()
    out = OUT/f"{name}.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-i",str(tmp/"f%05d.png"),
        "-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest","-c:v","libx264","-pix_fmt","yuv420p",
        "-crf","18","-preset","medium","-c:a","aac","-movflags","+faststart",str(out)], check=True)
    shutil.rmtree(tmp); return out

# ---------- Historias de Instagram 1080x1920 (libre: 250 px arriba, ~400 px abajo) ----------
STORY_CSS = """<style>
.story{position:absolute;left:96px;right:96px;top:300px;bottom:470px;display:flex;flex-direction:column;justify-content:center}
.ask{position:absolute;left:96px;right:96px;bottom:440px;font-weight:800;font-size:52px;color:var(--soft);letter-spacing:-.01em}
.mini{position:absolute;left:96px;top:300px;width:300px;height:auto}
</style>"""
HISTORIAS = {
 "historia_encuesta": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Pregunta de la semana</div><div class="rule"></div>'
     '<div class="h1" style="font-size:118px">¿Cuántos procesos <span class="b">llevas</span> hoy en día?</div>'
     '<div class="body2">Queremos conocer a nuestra comunidad litigante.</div></div>'
     '<div class="ask">Responde aquí ↓</div>',
 "historia_festivo16": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Calendario judicial</div><div class="rule"></div>'
     '<div class="h2" style="font-size:72px;color:var(--ink2)">Próximo festivo:</div>'
     '<div class="big b" style="font-size:150px;margin-top:24px">Lunes 16</div>'
     '<div class="big" style="font-size:110px;margin-top:10px">de noviembre</div>'
     '<div class="body2">Independencia de Cartagena. Ese día no cuenta en tus términos de días.</div></div>'
     '<div class="ask">Calcula tus términos ↓</div>',
 "historia_nuevo_reel": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Nuevo Reel</div><div class="rule"></div>'
     '<div class="h1" style="font-size:112px">Calcula un término en <span class="b">días hábiles.</span></div>'
     '<div class="body2">Paso a paso, en 25 segundos. Festivos y vacancia incluidos.</div></div>'
     '<div class="ask">Míralo aquí ↓</div>',
}

def shot_stories(b, items):
    d = OUT/"historias"; d.mkdir(parents=True, exist_ok=True)
    pg = b.new_page(viewport={"width":1080,"height":1920}); files = []
    for name, html in items.items():
        hf = d/"_s.html"; hf.write_text(HEAD.replace("var(--w)","1080px").replace("var(--h)","1920px")+STORY_CSS+html+"</body></html>")
        pg.goto(hf.as_uri()); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        f = d/f"{name}.png"; pg.screenshot(path=str(f)); files.append(f); hf.unlink()
    pg.close(); return files

if __name__ == "__main__":
    what = sys.argv[1:] or ["slides","reels","tutorial","historias"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        if "slides" in what: shot_slides(b, "terminos", TERMINOS)
        if "reels" in what:
            render_reel(b, "reel_festivo_humor", REEL_FESTIVO_HUMOR)
            render_reel(b, "reel_este_o_ese", REEL_ESTE_O_ESE)
            render_reel(b, "reel_domingo", REEL_DOMINGO)
        if "tutorial" in what: render_tutorial(b, "reel_tutorial_terminos", TUTORIAL)
        if "historias" in what: shot_stories(b, HISTORIAS)
        b.close()
    print("ok")
