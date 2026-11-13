# Agente: Productor de video

**Cuándo:** viernes, en el PC de Carol (`C:\Users\carol\Justibot`), con la voz oficial es-CO-GonzaloNeural.
**Entrega:** videos terminados → aviso a Carol → con su aprobación, a `animados/listos/`.

## Dónde está todo

- Proyecto Remotion: repo `yesser352-hub/Justibot`, carpeta `videos/` (en el PC: `C:\Users\carol\Justibot\videos`).
  Lee `videos/README.md`, `videos/COMO-HACER-UN-VIDEO-NUEVO.md` (copia en `agentes/referencia-como-hacer-un-video.md`)
  y el LEEME del último video. El video 07 (`src/aprendices/`, `voice7/`, `audio7/`) es la plantilla más reciente.
- Comando único: `bash producir-video.sh NN` desde `videos/` (ver abajo). Hace voz, sonido, render, unión,
  portada y revisión de calidad, y deja todo en `videos/out/`.

## Pasos por video

1. Guion `aprobado` en `guiones/videos/NN-slug.md`.
2. Código del video (en una rama `videos/short-NN-slug` de Justibot, nunca en main): copia la estructura del 07 a
   `src/<slug>/`, `voiceN/`, `audioN/`; registra la composición en `src/Root.tsx`; agrega una entrada en
   `videos/videos.conf` (número, carpeta, composición, prefijo de salida y palabra de la portada).
3. En el PC: `cd ~/Justibot/videos && bash producir-video.sh NN` (≈5-10 min por video).
4. Revisión: mira la hoja de contacto y el informe de `out/qaNN/`: textos legibles, nada cortado, JustiBot
   no tapado, subtítulos en sincronía, datos en pantalla iguales a los verificados, -14 LUFS.
5. Avísale a Carol con los MP4 y las portadas. **Espera su aprobación.**
6. Aprobado: sube a `justibot-contenido/animados/listos/` `justibot-NN-slug.mp4` (menos de 90 MB; si pesa más,
   recomprime CRF 20-22), `.jpg` (portada) y `.txt` (caso, fuentes y rama, como `justibot-04-…txt`). Commit y push.
   Actualiza la pieza en el Centro de mando a `listo para programar`.

## Cómo se ejecuta desde una sesión de Claude

- Con el PC conectado (herramientas `device_*`): corre el comando en el PC con `device_bash`, lee resultados con
  `device_stage_files` y sube los aprobados a GitHub desde la nube (el PC no puede hacer push desde la sesión).
- Si el PC no está conectado: deja el código del video en su rama y pídele a Carol que corra en Git Bash:
  `cd ~/Justibot && git fetch && git checkout videos/short-NN-slug && cd videos && bash producir-video.sh NN`.
- Nada de render en la nube ni en GitHub Actions (decisión de Carol).
