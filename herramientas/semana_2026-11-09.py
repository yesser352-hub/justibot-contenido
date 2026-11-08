"""Semana del lunes 9 al domingo 15 de noviembre de 2026.
Uso: python3 semana_2026-11-09.py [slides] [reels] [historias]
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import HEAD, page, CTA, shot_slides, render_reel, OUT, LOGO
from playwright.sync_api import sync_playwright

def cta_pulse(line, sub):
    return CTA(line, sub).replace('class="cta a"', 'class="cta a pulse"')

# ---------- Lunes 9 · 12:15: Reel de dato (ética profesional) ----------
REEL_EXCLIENTE = [
 (3200, page("glow", '<div class="eyebrow a">Ética profesional</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:120px">¿Puedes litigar contra un <span class="b">excliente?</span></div>')),
 (4200, page("glow", '<div class="eyebrow a">Depende</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:80px">Si tienen <span class="b">intereses contrapuestos</span>, es una falta de lealtad con el cliente.</div>'
             '<div class="src a">Art. 34, literal e), Ley 1123 de 2007</div>')),
 (4600, page("glow-tr", '<div class="eyebrow a">Un caso de este año</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:70px">Un abogado asesoró a dos inversionistas.</div>'
             '<div class="h2 a" style="font-size:70px;margin-top:36px;color:var(--ink2)">Después demandó a uno de ellos, usando lo que supo en esa asesoría.</div>')),
 (4600, page("glow", '<div class="eyebrow a">La decisión</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:66px">La Comisión Nacional de Disciplina Judicial dejó en firme la sanción.</div>'
             '<div class="box a"><div style="font-weight:700;font-size:54px;line-height:1.25">«El deber de lealtad y confidencialidad <span class="b">no caduca</span>».</div></div>'
             '<div class="src a">Fuente: El Tiempo, 2 de agosto de 2026</div>')),
 (4400, page("glow", cta_pulse("Tu ética, impecable. Tus procesos, vigilados.",
             "JustiBot consulta fuentes oficiales y te envía el reporte al correo todos los días."))),
]

# ---------- Martes 10 · 12:15: carrusel educativo (6 láminas) ----------
NOTIFICACION = [
 page("glow", '<div class="eyebrow">Art. 8 · Ley 2213 de 2022</div><div class="rule"></div>'
      '<div class="h1">¿Notificaste <span class="b">por correo?</span></div>'
      '<div class="body2">4 reglas para que la notificación personal quede bien hecha.</div>') + '<div class="foot">DESLIZA →</div>',
 page("flat", '<div class="eyebrow">01 / 04 · La dirección</div><div class="rule"></div>'
      '<div class="h2">Afirmas <span class="b">bajo juramento</span> que ese correo es el que usa la persona.</div>'
      '<div class="body2">Además, informas cómo lo obtuviste y aportas evidencias, en especial las comunicaciones que le has enviado.</div>'
      '<div class="src">Art. 8, Ley 2213 de 2022</div>'),
 page("glow", '<div class="eyebrow">02 / 04 · Cuándo queda notificada</div><div class="rule"></div>'
      '<div class="big b" style="font-size:230px">2 días</div>'
      '<div class="h2" style="font-size:72px;margin-top:16px">hábiles siguientes al envío del mensaje.</div>'
      '<div class="body2">Pasados esos dos días, la notificación personal se entiende realizada.</div>'),
 page("flat", '<div class="eyebrow">03 / 04 · Los términos</div><div class="rule"></div>'
      '<div class="h2">Empiezan a contarse con el <span class="b">acuse de recibo.</span></div>'
      '<div class="body2">O cuando se pueda constatar por otro medio que el destinatario accedió al mensaje. Puedes usar sistemas de confirmación de recibo de correos.</div>'
      '<div class="src">Art. 8, Ley 2213 de 2022</div>'),
 page("glow", '<div class="eyebrow">04 / 04 · Si hay discrepancia</div><div class="rule"></div>'
      '<div class="h2">Quien alegue que no se enteró pide la <span class="b">nulidad</span>, bajo juramento.</div>'
      '<div class="body2">Debe afirmar que no se enteró de la providencia y cumplir lo previsto en los artículos 132 a 138 del CGP.</div>'
      '<div class="src">Art. 8, Ley 2213 de 2022</div>'),
 page("flat", CTA("Notificado el auto, empieza la cuenta.",
      "La calculadora de JustiBot cuenta tus términos en días hábiles, con festivos y vacancia. Y tu reporte llega al correo todos los días.")),
]

# ---------- Miércoles 11 · 18:30: Reel de humor ----------
def frase(n, dice, real):
    return (3600, page("glow-tr", f'<div class="eyebrow a">{n} / 3 · Lo que le dices al cliente</div>'
            f'<div class="bubble out a pop" style="margin:40px 0 70px">{dice}</div>'
            f'<div class="eyebrow a" style="color:var(--mute)">Lo que de verdad pasa</div>'
            f'<div class="h2 a" style="font-size:70px;margin-top:24px">{real}</div>'))
REEL_FRASES = [
 (3000, page("glow", '<div class="eyebrow a">Diccionario del litigante</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:116px">Lo que le dices al cliente <span class="b">vs.</span> lo que de verdad pasa.</div>')),
 frase(1, "Ya está al despacho.", "Y ahí puede quedarse un buen rato."),
 frase(2, "Estamos pendientes.", "Revisas el estado todos los días, como un ritual."),
 frase(3, "Le aviso cualquier novedad.", "Aunque sea un domingo a las 9&nbsp;p.&nbsp;m."),
 (4400, page("glow", cta_pulse("Para la número 2, hay una forma más fácil.",
             "JustiBot vigila tus procesos y te envía el reporte al correo todos los días, haya o no novedades."))),
]

# ---------- Viernes 13 · 18:30: humor ligero ----------
def tipo(n, quien, desc, last=False):
    return (3200, page("glow-tr" if not last else "glow", f'<div class="eyebrow a">Tipo {n} / 4</div><div class="rule a"></div>'
            f'<div class="h1 a" style="font-size:108px">{quien}</div>'
            f'<div class="body2 a" style="font-size:52px">{desc}</div>'))
REEL_TIPOS = [
 (3000, page("glow", '<div class="eyebrow a">Viernes · humor</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:118px">Tipos de litigante <span class="b">revisando procesos.</span></div>')),
 tipo(1, "El del Excel.", "Cuarenta columnas, colores y una pestaña que se llama «NO BORRAR»."),
 tipo(2, "El del cuaderno.", "Todo a mano, con resaltador y mucha fe."),
 tipo(3, "El de las pestañas.", "Doce portales abiertos y la contraseña en un pósit."),
 tipo(4, 'El que ya tiene <span class="b">JustiBot.</span>', "Se toma el café y lee su reporte en el correo.", last=True),
 (4400, page("glow", cta_pulse("¿Cuál eres tú? Cuéntanos en los comentarios.",
             "JustiBot vigila tus procesos en fuentes oficiales y te envía el reporte al correo todos los días."))),
]

# ---------- Sábado 14 · 11:00: reto rápido (calendario judicial) ----------
REEL_RETO = [
 (3000, page("glow", '<div class="eyebrow a">Reto del sábado</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:130px">¿Cuándo <span class="b">vence?</span></div>'
             '<div class="body2 a">Pon pausa y responde en los comentarios.</div>')),
 (4200, page("glow-tr", '<div class="eyebrow a">El caso</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:76px">Te notifican por estado el <span class="b">viernes 13 de noviembre.</span></div>'
             '<div class="h2 a" style="font-size:76px;margin-top:40px">Término: <span class="b">3 días.</span></div>')),
 (3200, page("glow-tr", '<div class="eyebrow a">Pista</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:84px">El lunes 16 es <span class="b">festivo.</span></div>'
             '<div class="body2 a">Independencia de Cartagena.</div>')),
 (5000, page("glow", '<div class="eyebrow a">Respuesta</div><div class="rule a"></div>'
             '<ul class="list a" style="margin-top:10px"><li>Martes 17: día 1</li><li>Miércoles 18: día 2</li><li>Jueves 19: día 3</li></ul>'
             '<div class="big b a" style="font-size:150px;margin-top:20px">Jueves 19</div>'
             '<div class="h2 a" style="font-size:64px;margin-top:16px">de noviembre.</div>'
             '<div class="src a">Corre desde el día siguiente a la notificación y solo cuentan días hábiles (art. 118 CGP).</div>')),
 (4400, page("glow", cta_pulse("¿Acertaste?",
             "La calculadora de JustiBot cuenta tus términos en días hábiles, con festivos y vacancia."))),
]

# ---------- Historias de Instagram 1080x1920 (libre: 250 px arriba, ~400 px abajo) ----------
STORY_CSS = """<style>
.story{position:absolute;left:96px;right:96px;top:300px;bottom:470px;display:flex;flex-direction:column;justify-content:center}
.ask{position:absolute;left:96px;right:96px;bottom:440px;font-weight:800;font-size:52px;color:var(--soft);letter-spacing:-.01em}
</style>"""
HISTORIAS = {
 "historia_encuesta_portal": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Pregunta de la semana</div><div class="rule"></div>'
     '<div class="h1" style="font-size:118px">¿Qué portal te saca <span class="b">más canas?</span></div>'
     '<div class="body2">Rama Judicial, SAMAI o SIUGJ. Sin miedo, aquí todos te entendemos.</div></div>'
     '<div class="ask">Vota aquí ↓</div>',
 "historia_reel_excliente": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Nuevo Reel</div><div class="rule"></div>'
     '<div class="h1" style="font-size:112px">¿Puedes litigar contra un <span class="b">excliente?</span></div>'
     '<div class="body2">Un caso de este año y lo que dice la Ley 1123 de 2007.</div></div>'
     '<div class="ask">Míralo aquí ↓</div>',
 "historia_puente16": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Calendario judicial</div><div class="rule"></div>'
     '<div class="h2" style="font-size:72px;color:var(--ink2)">Este lunes es festivo:</div>'
     '<div class="big b" style="font-size:150px;margin-top:24px">Lunes 16</div>'
     '<div class="body2">No cuenta en tus términos de días. Si te notificaron el viernes 13, tu término arranca el martes 17.</div></div>'
     '<div class="ask">Calcula tus términos ↓</div>',
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
    what = sys.argv[1:] or ["slides","reels","historias"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        if "slides" in what: shot_slides(b, "notificacion", NOTIFICACION)
        if "reels" in what:
            render_reel(b, "reel_excliente", REEL_EXCLIENTE)
            render_reel(b, "reel_frases", REEL_FRASES)
            render_reel(b, "reel_tipos", REEL_TIPOS)
            render_reel(b, "reel_reto", REEL_RETO)
        if "historias" in what: shot_stories(b, HISTORIAS)
        b.close()
    print("ok")
