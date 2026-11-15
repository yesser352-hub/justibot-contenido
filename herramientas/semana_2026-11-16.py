"""Semana del lunes 16 al domingo 22 de noviembre de 2026 (piezas ligeras del diseñador).
Uso: python3 semana_2026-11-16.py [reels] [historias]
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import HEAD, page, CTA, render_reel, OUT
from playwright.sync_api import sync_playwright

def cta_pulse(line, sub):
    return CTA(line, sub).replace('class="cta a"', 'class="cta a pulse"')

MONO = "font-family:'IBM Plex Mono',monospace;font-weight:500"

# ---------- Lunes 16 (festivo) · 11:00: reto de humor ----------
def intento(n, rad, remate):
    return (3000, page("glow-tr", f'<div class="eyebrow a">Intento {n}</div><div class="rule a"></div>'
            f'<div class="box a" style="margin-top:10px"><div style="{MONO};font-size:50px;letter-spacing:.04em;color:var(--ink)">{rad}</div></div>'
            f'<div class="h2 a" style="font-size:78px;margin-top:56px">{remate}</div>'))
REEL_23 = [
 (3200, page("glow", '<div class="eyebrow a">Lunes festivo · reto</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:112px">Nadie escribe un radicado de <span class="b">23 dígitos</span> bien a la primera.</div>')),
 intento(1, "11001 31 03 0XX 2025 XXXX 00", 'Te faltó un <span class="b">dígito.</span>'),
 intento(2, "11001 31 03 0XX 2025 XXXXXX 00", 'Ahora te <span class="b">sobra</span> uno.'),
 intento(3, "11001 31 03 0XX 2026 XXXXX 00", 'Y era 2025, <span class="b">no 2026.</span>'),
 (4600, page("glow", cta_pulse("¿En qué intento lo logras tú?",
             "En JustiBot lo escribes una vez, o importas tus procesos desde Excel, y te llega el reporte al correo todos los días."))),
]

# ---------- Miércoles 18 · 12:15: humor (el Excel heredado) ----------
REEL_EXCEL = [
 (3000, page("glow", '<div class="eyebrow a">Miércoles · humor</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:130px">Todos tenemos <span class="b">ese Excel.</span></div>')),
 (3600, page("glow-tr", '<div class="eyebrow a">El archivo</div><div class="rule a"></div>'
             f'<div class="box a"><div style="{MONO};font-size:46px;line-height:1.35;color:var(--ink)">PROCESOS FINAL final v3 (este sí).xlsx</div></div>'
             '<div class="h2 a" style="font-size:70px;margin-top:56px">Heredado de tres judicantes.</div>')),
 (4400, page("glow-tr", '<div class="eyebrow a">Lo que trae</div><div class="rule a"></div>'
             '<ul class="list a"><li>Colores que nadie sabe qué significan.</li><li>Celdas combinadas que nadie se atreve a tocar.</li>'
             '<li>Una columna «revisado» con fecha de hace dos años.</li></ul>')),
 (3800, page("glow", '<div class="eyebrow a">La buena noticia</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:84px">JustiBot <span class="b">importa tus procesos</span> desde ese mismo Excel.</div>')),
 (4400, page("glow", cta_pulse("¿Cómo se llama el tuyo?",
             "Súbelo una vez y recibe el reporte de tus procesos al correo todos los días."))),
]

# ---------- Jueves 19 · 12:15: el correo más aburrido ----------
REEL_CORREO = [
 (3200, page("glow", '<div class="eyebrow a">Jueves</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:116px">El correo más aburrido del día <span class="b">es mi favorito.</span></div>')),
 (3600, page("glow-tr", '<div class="eyebrow a">Mi reporte de hoy</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:84px">Dice que hoy <span class="b">no pasó nada</span> en mis procesos.</div>'
             '<div class="body2 a">Y saberlo también me ahorra la mañana.</div>')),
 (4400, page("glow", '<div class="eyebrow a">Así funciona</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:76px">Llega <span class="b">todos los días</span>, haya o no novedades.</div>'
             '<div class="body2 a">Cuando las hay, trae la fecha y la descripción de cada actuación.</div>')),
 (4400, page("glow", cta_pulse("¿Cuál es tu correo favorito del día?",
             "JustiBot consulta fuentes oficiales y te envía el reporte al correo, sin cobrar por radicado."))),
]

# ---------- Sábado 21 · 11:00: POV Doctor F5 ----------
REEL_F5 = [
 (3200, page("glow", '<div class="eyebrow a">POV</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:118px">Tu proceso lleva <span class="b">ocho meses</span> al despacho.</div>')),
 (3000, page("glow-tr", '<div class="big b a pop" style="font-size:360px">F5</div>'
             '<div class="h2 a" style="font-size:80px;margin-top:30px">Y tú sigues refrescando.</div>')),
 (3400, page("glow-tr", '<div class="eyebrow a">Refresco número 47</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:92px">Mismo estado.<br>Misma fecha.<br><span class="b">Misma fe.</span></div>')),
 (4000, page("glow", '<div class="eyebrow a">Respira</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:78px">El día que se mueva, lo ves en tu <span class="b">reporte.</span></div>'
             '<div class="body2 a">JustiBot revisa tus procesos cada día y te envía el reporte al correo.</div>')),
 (4400, page("glow", cta_pulse("¿Cuántas veces refrescas al día?",
             "Pruébalo con tus procesos: el primer mes del plan Starter es gratis."))),
]

# ---------- Domingo 22 · 18:30: etiqueta al colega ----------
REEL_COLEGA = [
 (3400, page("glow", '<div class="eyebrow a">Domingo · etiqueta</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:108px">Tú sabes quién <span class="b">revisa todo a mano</span> a las 6 a. m.</div>')),
 (4600, page("glow-tr", '<div class="eyebrow a">Ese colega</div><div class="rule a"></div>'
             '<ul class="list a"><li>Café en una mano, radicados en la otra.</li><li>Un portal tras otro, antes de que amanezca.</li>'
             '<li>Y aun así llega puntual a la audiencia.</li></ul>')),
 (3200, page("glow", '<div class="eyebrow a">Se lo merece</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:112px">Dormir <span class="b">un rato más.</span></div>')),
 (4400, page("glow", cta_pulse("¿A quién vas a etiquetar?",
             "JustiBot consulta fuentes oficiales y envía el reporte al correo todos los días."))),
]

# ---------- Historias 1080x1920 (libre: 250 px arriba, ~400 px abajo) ----------
STORY_CSS = """<style>
.story{position:absolute;left:96px;right:96px;top:300px;bottom:470px;display:flex;flex-direction:column;justify-content:center}
.ask{position:absolute;left:96px;right:96px;bottom:440px;font-weight:800;font-size:52px;color:var(--soft);letter-spacing:-.01em}
</style>"""
HISTORIAS = {
 "historia_encuesta_refrescar": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Pregunta de la semana</div><div class="rule"></div>'
     '<div class="h1" style="font-size:112px">¿Cuántas veces al día entras a <span class="b">revisar tus procesos?</span></div>'
     '<div class="body2">Sin juzgar. Aquí todos hemos refrescado de más.</div></div>'
     '<div class="ask">Vota aquí ↓</div>',
 "historia_robot05": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Nuevo video</div><div class="rule"></div>'
     '<div class="h1" style="font-size:104px">Burlarse en redes del cuerpo de una mujer <span class="b">puede ser violencia.</span></div>'
     '<div class="body2">Lo explicó la Corte Constitucional en la sentencia T-348 de 2026.</div></div>'
     '<div class="ask">Míralo aquí ↓</div>',
 "historia_vacancia_un_mes": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Calendario judicial</div><div class="rule"></div>'
     '<div class="h2" style="font-size:72px;color:var(--ink2)">En un mes empieza la vacancia:</div>'
     '<div class="big b" style="font-size:170px;margin-top:24px">20 dic</div>'
     '<div class="body2">Va hasta el 10 de enero. Como el lunes 11 es festivo, los despachos vuelven el martes 12 de enero de 2027.</div></div>'
     '<div class="ask">Cuenta regresiva ↓</div>',
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
    what = sys.argv[1:] or ["reels","historias"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        if "reels" in what:
            render_reel(b, "reel_23digitos", REEL_23)
            render_reel(b, "reel_excel", REEL_EXCEL)
            render_reel(b, "reel_correo", REEL_CORREO)
            render_reel(b, "reel_f5", REEL_F5)
            render_reel(b, "reel_colega", REEL_COLEGA)
        if "historias" in what: shot_stories(b, HISTORIAS)
        b.close()
    print("ok")
