"""Piezas ligeras que completan la semana del 23 al 29 de noviembre de 2026 (diseñador, domingo 22-nov).
Sin datos jurídicos: humor del día a día del litigio y funciones reales de JustiBot.
Uso: python3 finde_2026-11-27.py [reels] [historias]
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import HEAD, page, CTA, render_reel, OUT
from playwright.sync_api import sync_playwright

def cta_pulse(line, sub):
    return CTA(line, sub).replace('class="cta a"', 'class="cta a pulse"')

# ---------- Viernes 27 · 6:30 p. m.: Viernes, 4:59 p. m. (humor) ----------
REEL_VIERNES = [
 (3200, page("glow", '<div class="eyebrow a">Viernes · 4:59 p. m.</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:120px">Cierras el computador. <span class="b">Por fin.</span></div>')),
 (3400, page("glow-tr", '<div class="eyebrow a">Mientras tanto</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:84px">En algún despacho, alguien registra <span class="b">una actuación en tu proceso.</span></div>')),
 (3800, page("glow-tr", '<div class="eyebrow a">Tú · lunes, 8:00 a. m.</div>'
             '<div class="h2 a" style="font-size:66px;margin:30px 0 70px">Abres el portal, proceso por proceso:</div>'
             '<div class="bubble in a pop">¿Y esto cuándo salió?</div>')),
 (4000, page("glow", '<div class="eyebrow a">Con JustiBot</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:78px">Te llega en el reporte del correo, <span class="b">con la fecha y la descripción</span> de la actuación.</div>'
             '<div class="body2 a">El reporte llega todos los días, haya o no novedades.</div>')),
 (4600, page("glow", cta_pulse("¿A qué hora cierras el viernes?",
             "JustiBot revisa tus procesos en fuentes oficiales y te manda el reporte al correo."))),
]

# ---------- Domingo 29 · 6:30 p. m.: La lista mental del domingo (ligero) ----------
TACHA = ('<div class="a" style="position:relative;display:inline-block;align-self:flex-start;margin-top:10px">'
         '<span style="font-weight:700;font-size:54px;white-space:nowrap;color:var(--ink2)">Revisar 40 procesos, uno por uno</span>'
         '<span style="position:absolute;left:-6px;right:-6px;top:52%;height:8px;background:var(--acc)"></span></div>')
def lista(items):
    return '<ul class="list a">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
REEL_DOMINGO = [
 (3200, page("glow", '<div class="eyebrow a">Domingo · 7:00 p. m.</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:116px">La lista mental <span class="b">del lunes</span> ya empezó.</div>')),
 (4200, page("glow-tr", '<div class="eyebrow a">Lunes</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:80px">Pendientes</div>'
             + lista(["Audiencia a las 9:00", "Memorial para el miércoles", "Llamar al cliente que pregunta todo",
                      "Revisar 40 procesos, uno por uno"]))),
 (3800, page("glow-tr", '<div class="eyebrow a">Tacha esa última</div><div class="rule a"></div>' + TACHA +
             '<div class="h2 a" style="font-size:76px;margin-top:60px">El reporte de JustiBot te dice <span class="b">qué se movió</span> en tus procesos.</div>')),
 (4600, page("glow", cta_pulse("¿Cuántos procesos revisas el lunes?",
             "Tu reporte llega al correo todos los días, haya o no novedades."))),
]

# ---------- Historias 1080x1920 (libre: 250 px arriba, ~400 px abajo) ----------
STORY_CSS = """<style>
.story{position:absolute;left:96px;right:96px;top:300px;bottom:470px;display:flex;flex-direction:column;justify-content:center}
.ask{position:absolute;left:96px;right:96px;bottom:440px;font-weight:800;font-size:52px;color:var(--soft);letter-spacing:-.01em}
</style>"""
HISTORIAS = {
 "historia_encuesta_finde": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Pregunta de la semana</div><div class="rule"></div>'
     '<div class="h1" style="font-size:112px">¿Revisas tus procesos <span class="b">el fin de semana?</span></div>'
     '<div class="body2">Sin juzgar. Aquí nadie se desconecta del todo.</div></div>'
     '<div class="ask">Vota aquí ↓</div>',
 "historia_robot07": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Nuevo video</div><div class="rule"></div>'
     '<div class="h1" style="font-size:104px">¿Vuelve el período de prueba <span class="b">para los aprendices?</span></div>'
     '<div class="body2">El Consejo de Estado suspendió provisionalmente la prohibición del Decreto 223 de 2026.</div></div>'
     '<div class="ask">Míralo aquí ↓</div>',
 "historia_diciembre": '<div class="glow" style="position:absolute;inset:0"></div><div class="story">'
     '<div class="eyebrow">Nuevo carrusel</div><div class="rule"></div>'
     '<div class="h1" style="font-size:108px">Diciembre judicial <span class="b">en 4 fechas.</span></div>'
     '<div class="body2">8, 18, 20 y 12: guárdalo antes de la vacancia.</div></div>'
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
    what = sys.argv[1:] or ["reels", "historias"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        if "reels" in what:
            render_reel(b, "reel_viernes_459", REEL_VIERNES)
            render_reel(b, "reel_lista_domingo", REEL_DOMINGO)
        if "historias" in what:
            shot_stories(b, HISTORIAS)
        b.close()
    print("ok")
