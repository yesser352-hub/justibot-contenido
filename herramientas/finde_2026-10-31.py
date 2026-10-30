import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import page, CTA, render_reel
from playwright.sync_api import sync_playwright

# Sábado 31 de octubre: Halloween del litigante (humor, sin el tema de "perder un término")
REEL_HALLOWEEN = [
 (3000, page("glow", '<div class="eyebrow a">Halloween · 31 de octubre</div><div class="rule a"></div><div class="h1 a" style="font-size:118px">Lo que de verdad asusta a un <span class="b">litigante.</span></div>')),
 (3300, page("glow-tr", '<div class="eyebrow a">Miedo n.º 1</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Consultas el proceso y aparece:</div><div class="bubble in a pop">«Al despacho»… desde hace cuatro meses.</div>')),
 (3300, page("glow-tr", '<div class="eyebrow a">Miedo n.º 2</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Entras al portal a las 8 a. m.:</div><div class="bubble in a pop">«La plataforma se encuentra en mantenimiento».</div>')),
 (3300, page("glow-tr", '<div class="eyebrow a">Miedo n.º 3</div><div class="h2 a" style="font-size:66px;margin:30px 0 60px">Audiencia virtual, minuto uno:</div><div class="bubble in a pop">«¿Me escuchan? ¿Me escuchan? Doctor, está en silencio».</div>')),
 (4200, page("glow", CTA("Lo que no asusta: saber cada mañana qué se movió.", "Tu reporte llega al correo todos los días, haya o no novedades.").replace('class="cta a"','class="cta a pulse"'))),
]

# Domingo 1 de noviembre: mañana es festivo
REEL_FESTIVO = [
 (3000, page("glow", '<div class="eyebrow a">Ojo con los términos</div><div class="rule a"></div><div class="h1 a" style="font-size:118px">Mañana lunes <span class="b">2 de noviembre</span> es festivo.</div>')),
 (3600, page("glow", '<div class="eyebrow a">Días hábiles</div><div class="rule a"></div><div class="h2 a">Los términos en días se cuentan en <span class="b">días hábiles.</span></div><div class="body2 a">El festivo no cuenta: si tu término vencía el lunes, vence el martes 3.</div><div class="src a">Art. 118, Código General del Proceso</div>')),
 (3400, page("glow", '<div class="eyebrow a">Próximos festivos</div><div class="rule a"></div><div class="h2 a" style="font-size:80px">Lunes <span class="b">16 de noviembre</span></div><div class="body2 a" style="margin-top:20px">Independencia de Cartagena</div><div class="h2 a" style="font-size:80px;margin-top:56px">Martes <span class="b">8 de diciembre</span></div><div class="body2 a" style="margin-top:20px">Inmaculada Concepción</div>')),
 (4200, page("glow", CTA("Calcula tus términos con festivos incluidos.", "JustiBot cuenta en días hábiles y te envía el reporte al correo todos los días.").replace('class="cta a"','class="cta a pulse"'))),
]

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        render_reel(b, "reel_halloween", REEL_HALLOWEEN)
        render_reel(b, "reel_festivo", REEL_FESTIVO)
        b.close()
    print("ok")
