# Guía de la tarea semanal de contenido JustiBot

Esta guía la sigue la tarea automática de los domingos. Todo lo necesario está en este repositorio.

## Preparar el entorno (cada vez)
```bash
git clone https://github.com/yesser352-hub/justibot-contenido.git /home/claude/justibot-contenido   # si no existe
cd /home/claude/justibot-contenido/herramientas && npm install --silent
```
- `build.py`: estilos de marca (HEAD con tokens), `page()`, `CTA()`, `shot_slides()` (carruseles 1080x1350 PNG) y `render_reel()` (Reels 1080x1920 MP4 con animación `ANIM_JS`). Úsalo como plantilla: importa `HEAD, page, CTA, shot_slides, render_reel, OUT, LOGO` desde un script nuevo de la semana y define ahí las láminas/escenas nuevas. No cambies el estilo.
- `add_music.py video.mp4 ../musica/<canción>.mp3 salida.mp4`: pone música (-16 LUFS, fade).
- `slideshow.py carpeta_png salida.mp4 4.5`: convierte un carrusel en video 1080x1920 para TikTok.
- `../musica/CATALOGO.md`: canciones por tipo de pieza y registro de las ya usadas (no repetir la misma en dos piezas seguidas; anota las nuevas).
- `logo.png`: logo blanco oficial. Siempre en el cierre.
- Las fuentes Inter vienen del sistema; IBM Plex Mono por npm. No uses emojis dentro de imágenes o videos (no se ven).

## Reglas de marca y contenido (no negociables)
- Estilo: fondo azul marino #0a1525 con brillo azul, acento #3b82f6, tipografía Inter gruesa. Que no se vea "hecho con IA": sobrio, profesional, nada de imágenes generadas.
- Cierre: logo + "Pruébalo gratis · www.justibot.com.co" (siempre con www).
- Nunca inventar funciones. Hechos confirmados: JustiBot consulta fuentes oficiales (Rama Judicial, SAMAI, SIUGJ, SIC, Supersociedades, Supersalud, Superfinanciera, Contraloría, Fiscalía, Policía); envía el reporte por correo TODOS los días haya o no novedades (nunca decir "solo te escribe cuando pasa algo"); envía fecha y descripción de cada actuación, NO el auto escaneado; no cobra por radicado; calculadora de términos en días hábiles con festivos y vacancia; pantalla "Tu día"; importar procesos desde Excel; planes Starter (1 mes gratis), Municipal $19.900, Circuito $39.900, Distrito $64.900.
- El reporte NO se puede reenviar al cliente (trae procesos de varios clientes).
- El tema "perder una actuación/término" está quemado: no usarlo. Sí gusta el humor del día a día del litigio.
- Nunca mostrar datos reales de clientes (radicados, partes, juzgados): usar las capturas pixeladas de `capturas/` o ejemplos claramente ficticios.
- Español de Colombia, trato de "tú" al público; "Dr./Dra." solo en mensajes a embajadores.

## Formatos por red (Metricool, blogId 6544004, zona America/Bogota)
- Cada pieza va en DOS publicaciones de Metricool:
  1. Instagram + TikTok: texto termina en "Pruébalo gratis 👉 enlace en el perfil".
  2. Facebook sola: el mismo texto pero con "Pruébalo gratis 👉 https://www.justibot.com.co/".
- Carruseles: Instagram (POST con las PNG) y Facebook (POST) como carrusel; para TikTok, publicación aparte solo TikTok con el video de `slideshow.py` + música.
- Reels: con música de la biblioteca; Instagram REEL, Facebook REEL, TikTok con `tiktokData.title` obligatorio.
- Medios: sube los archivos a este repo en `AAAA-MM/...`, haz push y usa la URL raw fijada al commit: `https://raw.githubusercontent.com/yesser352-hub/justibot-contenido/<sha>/<ruta>`.
- Crea todo con `draft: true` (Carol revisa y aprueba). Horarios que funcionan: 12:15 y 18:30; 7:00 para piezas de "mañana".
- 4 a 8 hashtags: #abogadoscolombia #litigio #ramajudicial #derechocolombia #justibot + 1 o 2 del tema.

## Tablero de pendientes
URL: https://claude.ai/artifact/L82r9TG3Lbd3yghzpQaH2C (ArtifactData; colecciones `posts` y `tasks`).
- `posts`: {date "AAAA-MM-DD", time, title, format, status "borrador"|"programada"}. Agrega las piezas nuevas con status "borrador". Puedes borrar las de hace más de 3 semanas.
- `tasks`: {title, note, area contenido|embajadoras|ventas|producto|web|otros, col tuyo|claude|espera|hecho, order}. Agrega en `tuyo` una tarjeta "Revisar y aprobar las piezas de la semana del …". Lee siempre antes de escribir y usa if_version.
