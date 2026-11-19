"""Semana del lunes 23 al domingo 29 de noviembre de 2026 (piezas de marca del diseñador).
Guiones aprobados en guiones/piezas/2026-11-2*.md.
Uso: python3 semana_2026-11-23.py [reels] [carrusel]
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build import HEAD, page, CTA, render_reel, shot_slides, OUT
from playwright.sync_api import sync_playwright

def cta_pulse(line, sub):
    return CTA(line, sub).replace('class="cta a"', 'class="cta a pulse"')

MONO = "font-family:'IBM Plex Mono',monospace;font-weight:500"

# ---------- Lunes 23 · 6:30 p. m.: Objeción ep. 1 «La Rama es gratis» ----------
SELLO = ('<div class="a" style="align-self:flex-start;margin-top:56px;border:6px solid var(--acc);color:var(--acc);'
         f'{MONO};font-size:58px;letter-spacing:.22em;padding:16px 34px;transform:rotate(-4deg)">OBJECIÓN</div>')
COMENTARIO = ('<div class="box a" style="border-radius:28px;margin-top:20px">'
              '<div style="display:flex;align-items:center;gap:22px;margin-bottom:26px">'
              '<div style="width:64px;height:64px;border-radius:50%;background:var(--line)"></div>'
              f'<div style="{MONO};font-size:28px;color:var(--mute);letter-spacing:.08em">Comentario</div></div>'
              '<div style="font-weight:700;font-size:62px;line-height:1.2">¿Para qué pago si la consulta de la Rama es gratis?</div></div>')
REEL_OBJECION = [
 (3600, page("glow", '<div class="eyebrow a">Objeción #1</div><div class="rule a"></div>' + COMENTARIO + SELLO)),
 (3000, page("glow-tr", '<div class="eyebrow a">Respuesta</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:112px">Tienes razón: <span class="b">es gratis.</span></div>'
             '<div class="h2 a" style="font-size:80px;margin-top:40px;color:var(--ink2)">Y funciona.</div>')),
 (3600, page("glow-tr", '<div class="eyebrow a">Pero</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:86px">Lo que no hace es entrar por ti, proceso por proceso, <span class="b">cada día.</span></div>')),
 (4600, page("glow", '<div class="eyebrow a">JustiBot</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:72px">Revisa tus procesos en la Rama, SAMAI, SIUGJ y más,</div>'
             '<div class="body a">y te manda el reporte al correo <span class="b">todos los días, haya o no novedades.</span></div>')),
 (4800, page("glow", cta_pulse("¿Cuántas pestañas abres para revisar? Dinos un número.",
             "Tus procesos en fuentes oficiales, en un solo reporte diario."))),
]

# ---------- Martes 24 · 12:15 p. m.: Traductor de la Rama ep. 1 ----------
def tarjeta(n, frase, dice, entiendes, size=104):
    return (4200, page("glow-tr", f'<div class="eyebrow a">{n} / 03</div><div class="rule a"></div>'
            f'<div class="big b a" style="font-size:{size}px;letter-spacing:-.03em">{frase}</div>'
            f'<div class="a" style="{MONO};font-size:28px;letter-spacing:.16em;color:var(--mute);margin-top:56px">LO QUE DICE</div>'
            f'<div class="body2 a" style="margin-top:14px">{dice}</div>'
            f'<div class="a" style="{MONO};font-size:28px;letter-spacing:.16em;color:var(--soft);margin-top:52px">LO QUE ENTIENDES</div>'
            f'<div class="h2 a" style="font-size:76px;margin-top:14px">«{entiendes}»</div>'))
REEL_TRADUCTOR = [
 (3000, page("glow", '<div class="eyebrow a">Traductor de la Rama · ep. 1</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:120px">Lo que dice la Rama <span class="b">vs. lo que entiendes.</span></div>')),
 tarjeta("01", "AL DESPACHO", "El expediente pasó al juez para decidir.", "Nos vemos en unos meses."),
 tarjeta("02", "FIJACIÓN EN ESTADO", "Salió una providencia y quedó notificada.", "Mañana empieza a correr. Respira.", 92),
 tarjeta("03", "CONSTANCIA SECRETARIAL", "El secretario dejó algo por escrito en el proceso.", "¿A favor o en contra? Abre ya.", 84),
 (3800, page("glow", '<div class="eyebrow a">Tu reporte</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:76px">El reporte de JustiBot te dice cada día <span class="b">qué actuación salió y en qué fecha.</span></div>'
             '<div class="body2 a">La traducción… sigue siendo tuya.</div>')),
 (4600, page("glow", cta_pulse("¿Cuál te saca más canas? 1, 2 o 3.",
             "JustiBot revisa tus procesos en fuentes oficiales y te envía el reporte al correo todos los días."))),
]

# ---------- Miércoles 25 · 6:30 p. m.: Sin novedad, doctor ep. 1 ----------
def parte(eyebrow, rotulo, texto, extra=""):
    return page("glow-tr", f'<div class="eyebrow a">{eyebrow}</div><div class="rule a"></div>'
                f'<div class="h2 a" style="font-size:64px;color:var(--ink2)">{rotulo}</div>'
                '<div class="box a" style="border-radius:24px">'
                f'<div style="{MONO};font-size:28px;color:var(--mute);letter-spacing:.06em">Bandeja de entrada · 7:00 a. m.</div>'
                '<div style="font-weight:700;font-size:44px;margin-top:18px">Reporte del día</div>'
                f'<div style="font-weight:600;font-size:52px;line-height:1.3;margin-top:30px">{texto}</div>{extra}</div>')
NOVEDAD = ('<div style="border-left:6px solid var(--acc);padding:6px 0 6px 26px;margin-top:30px">'
           f'<div style="{MONO};font-size:30px;color:var(--soft)">24-nov-2026</div>'
           '<div style="font-weight:600;font-size:42px;margin-top:8px;color:var(--ink)">Auto que corre traslado</div></div>')
REEL_SIN_NOVEDAD = [
 (3400, parte("Sin novedad, doctor · ep. 1", "Llega el parte.",
              'Parte del día: cuarenta procesos revisados. <span class="b">Sin novedad, doctor.</span>')),
 (2600, parte("Sin novedad, doctor · ep. 1", "Al día siguiente…", 'Parte del día: <span class="b">sin novedad, doctor.</span>')),
 (4200, parte("Sin novedad, doctor · ep. 1", "Y un día…",
              'Parte del día: <span class="b">una novedad.</span> Lo demás, sin novedad, doctor.', NOVEDAD)),
 (3000, page("glow", '<div class="eyebrow a">Así llega</div><div class="rule a"></div>'
             '<div class="h1 a" style="font-size:100px">Haya o no novedades, el reporte llega <span class="b">todos los días.</span></div>')),
 (4400, page("glow", cta_pulse("¿Hoy hubo novedad? Sí o no.",
             "Y el día que sí hay, te dice qué actuación salió y en qué fecha."))),
]

# ---------- Sábado 28 · 11:00 a. m.: Reto del sábado #2 ----------
def cuenta(n):
    return (1000, page("glow", '<div class="h2 a" style="font-size:60px;color:var(--ink2)">Escribe tu respuesta antes de ver la solución.</div>'
            f'<div class="big b a" style="font-size:520px;margin-top:40px">{n}</div>'))
DIA = lambda d, r, hi=False: (f'<li style="color:{"var(--acc)" if hi else "var(--ink2)"};margin-bottom:26px">'
                              f'<span style="color:var(--ink)">{d}</span> → {r}</li>')
REEL_RETO = [
 (3600, page("glow", '<div class="eyebrow a">Reto del sábado #2</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:80px">Te notifican por estado el <span class="b">jueves 3 de diciembre.</span></div>'
             '<div class="h2 a" style="font-size:80px;margin-top:36px">Término: <span class="b">3 días.</span></div>'
             '<div class="h1 a" style="font-size:110px;margin-top:50px">¿Cuándo vence?</div>')),
 cuenta(3), cuenta(2), cuenta(1),
 (5000, page("glow-tr", '<div class="eyebrow a">Solución, día por día</div><div class="rule a"></div>'
             '<ul class="list a" style="margin-top:10px">' + DIA("Vie 4", "día 1") + DIA("Sáb 5 y dom 6", "no cuentan")
             + DIA("Lun 7", "día 2") + DIA("Mar 8", "festivo", True) + DIA("Mié 9", "día 3") + '</ul>')),
 (3800, page("glow", '<div class="eyebrow a">Respuesta</div><div class="rule a"></div>'
             '<div class="h2 a" style="font-size:80px">Vence el</div>'
             '<div class="h1 a b" style="font-size:118px;margin-top:20px">miércoles 9 de diciembre.</div>'
             '<div class="src a">CGP, art. 118: corre desde el día siguiente a la notificación.<br>Supuestos: despacho que trabaja normal, términos en días hábiles.</div>')),
 (4400, page("glow", cta_pulse("¿Acertaste? Cuéntanos.",
             "La calculadora de términos de JustiBot cuenta festivos y vacancia."))),
]

# ---------- Jueves 26 · 12:15 p. m.: carrusel Diciembre en 4 fechas (1080x1350) ----------
def fecha(n, num, dia, titulo, texto, src=""):
    s = f'<div class="src">{src}</div>' if src else ""
    return page("flat" if n % 2 else "glow",
        f'<div class="eyebrow">0{n} / 05</div><div class="rule"></div>'
        f'<div style="display:flex;align-items:baseline;gap:30px"><div class="big b" style="font-size:260px">{num}</div>'
        f'<div class="h2" style="font-size:56px;color:var(--ink2)">{dia}</div></div>'
        f'<div class="h2" style="font-size:72px;margin-top:20px">{titulo}</div><div class="body2">{texto}</div>{s}')
CARRUSEL_DIC = [
 page("glow", '<div class="eyebrow">Calendario judicial · diciembre 2026</div><div class="rule"></div>'
      '<div class="h1"><span class="b">8, 18, 20 y 12:</span> las 4 fechas que todo litigante debe tener a mano.</div>') + '<div class="foot">DESLIZA →</div>',
 fecha(1, "8", "de diciembre · martes", "Festivo (Inmaculada Concepción).", "No se pasa al lunes. Cuéntalo al calcular términos."),
 fecha(2, "18", "de diciembre · viernes", "Último día hábil antes de la vacancia.", "Lo urgente, antes de esta fecha."),
 fecha(3, "20", "de diciembre", "Empieza la vacancia judicial (hasta el 10 de enero).", "En términos de días, la vacancia no cuenta.", "CGP, art. 118"),
 page("glow", '<div class="eyebrow">04 / 05</div><div class="rule"></div>'
      '<div class="h2">Ojo: la vacancia <span class="b">no para todo.</span></div>'
      '<ul class="list"><li>Siguen, entre otros, los juzgados penales municipales y los de ejecución de penas.</li>'
      '<li>Tutelas y hábeas corpus no paran.</li></ul>'),
 fecha(5, "12", "de enero · martes", "Si no hay cambios, vuelven los despachos.", "El lunes 11 es festivo de Reyes."),
 page("flat", CTA("Guárdalo y mándaselo a tu colega.",
      "¿Trabajas en vacancia? Sí o no.<br>La calculadora de términos de JustiBot ya cuenta festivos y vacancia.")),
]

if __name__ == "__main__":
    what = sys.argv[1:] or ["reels", "carrusel"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        if "reels" in what:
            render_reel(b, "reel_objecion_rama_gratis", REEL_OBJECION)
            render_reel(b, "reel_traductor_rama_ep1", REEL_TRADUCTOR)
            render_reel(b, "reel_sin_novedad_ep1", REEL_SIN_NOVEDAD)
            render_reel(b, "reel_reto_cuando_vence_2", REEL_RETO)
        if "reto" in what:
            render_reel(b, "reel_reto_cuando_vence_2", REEL_RETO)
        if "carrusel" in what:
            shot_slides(b, "diciembre_4_fechas", CARRUSEL_DIC)
        b.close()
    print("ok")
