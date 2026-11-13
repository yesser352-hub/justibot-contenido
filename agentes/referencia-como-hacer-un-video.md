# Cómo hacer un video nuevo de JustiBot con el mismo estilo

Todo se genera con código en este equipo: imagen (three.js dentro de Remotion), voz (edge-tts), música y efectos
(numpy/scipy). No se usan generadores externos de video. Lo más rápido es copiar el video 03 (`src/ia/`), que ya usa
todos los módulos compartidos.

## 0. Preparar el equipo (una sola vez)
```bash
cd videos
npm install                 # Node 22; Remotion 4, three 0.169, @react-three/fiber 8
pip install numpy scipy pillow edge-tts
```
Se necesitan Chrome (renderiza con `--gl angle`) y FFmpeg en el PATH. En Windows, renderizar con
`export TEMP=D:/remotion-tmp TMP=D:/remotion-tmp` (cada render copia `public/` al temporal).

## 1. Guion y voz
1. Escribe el guion en `guiones/NN-titulo.md` (6 escenas, 60-65 s en total, unas 2,7 palabras por segundo).
   Verifica los datos con fuentes oficiales antes de grabar; no inventes sentencias, cifras ni nombres.
2. Copia `voice3/` a `voiceN/` y pon las 6 narraciones en `SCENES` de `gen_voice.py`.
3. `python gen_voice.py "+4%"` → `s1..s6.mp3` + tiempos por palabra (la velocidad ajusta la duración).
4. En `assemble.py`, `PLAN` = segundo en que empieza cada escena (deja ~0,7 s entre escenas y 3 s finales para el
   logo). `python -X utf8 assemble.py` → `voice.wav` (64,5 s) y `words.json` con tiempos absolutos.
5. `python -X utf8 subs.py` → `subs.json` y `subtitulos.srt` (bloques cortos sincronizados por palabra).
6. Copia `words.json` y `subs.json` a la carpeta del video en `src/`.

## 2. Escenografía, cámara y personaje (`src/<video>/`)
- `story.ts`: `K` = cuadros de las palabras clave (`wf(escena, "palabra")`), `SHOTS` (tomas: cuadros, lugar, luz),
  `XFADE` (fundidos), `CAMS` (cámaras: claves con `dolly`/`pushK`/`glide`), `DOF` (desenfoque), `TITLES` (textos).
  Cada reacción visual cae 0-3 cuadros antes de su palabra.
- `world.ts`: arma los lugares y anima hologramas por cuadro. Lugares listos en `src/abogado/build.ts`
  (pasillo del tribunal, sala de audiencias con balanza y bandera, biblioteca futurista, oficina con ventanal,
  fondo final con partículas) y `src/toga/build2.ts` (Palacio de Justicia con lluvia, red de expedientes).
- Hologramas: `src/abogado/holo.ts` (clase `Holo` + marco, textos e íconos), `src/toga/holo2.ts`, `src/ia/holo3.ts`.
- `cast.ts` → `botAt(toma, cuadro)`: posición y pose de JustiBot (brazos, manos, mirada, expresión, caminar).
  El dibujo está en `src/abogado/robot.ts`; la hoja de poses en `referencias/justibot-poses.png`.
- `lights.ts`: luz por ambiente (dos tonos, niebla, focos cálidos). Estilo de imagen: `src/abogado/ink.ts` (tinta),
  `lensblur.ts` (lente), `grade.ts` (color), `shade.ts` (sombreado de dos tonos), `paint.ts` (texturas pintadas).
- `Short.tsx`: compositor, títulos, subtítulos y logo. Registra la composición en `src/Root.tsx`.
- Revisa cuadros sueltos: `COMP=MiShort node scripts/stills.mjs out/prueba/x_ 60,300,900 0.5`
  y `python scripts/sheet.py out/prueba out/prueba/hoja.jpg`. Cuida que los títulos (arriba) no tapen hologramas
  y que JustiBot no quede cortado por los bordes.

## 3. Música y efectos (`audioN/`)
- Copia `audio3/`. En `make_scoreN.py` cambia la carpeta de voz, las palabras clave (`K`) y los límites de
  escena (`SCENES`); en `sfxN_part.py` la lista de efectos (cada `add(sonido, segundo, nivel, nombre)`).
- `python make_scoreN.py && python -X utf8 scoreN.py` → `mix.wav` (−14 LUFS, pico ≤ −1 dBTP, música unos 10 LU
  por debajo de la voz y baja 3 dB mientras se habla) + stems + `cues.md`.
- La música es original (re menor, 96 BPM, con un tiempo fuerte en el golpe del logo); los instrumentos están en
  `instruments.py` y los efectos base en `sfx_gen.py`.

## 4. Render, unión y revisión
```bash
npx remotion render src/index.ts MiShort out/mi_raw.mp4 --codec h264 --crf 16 --gl angle --concurrency 3
ffmpeg -y -i out/mi_raw.mp4 -i audioN/mix.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 256k -movflags +faststart -shortest out/mi_final.mp4
python -X utf8 scripts/short_qa.py out/mi_final.mp4 out/qa shotsN.json
```
`short_qa.py` revisa duración, volumen, cuadros negros/blancos/congelados y saltos bruscos. Miniatura: un cuadro a
escala 1 sin subtítulos, `COMP=MiShort node scripts/stills.mjs out/portada/c_ 150 1 '{"subs":false}'`.

## Reglas de marca y contenido
- Textos sin emojis; colores sólidos (azul acciones, verde éxito, ámbar advertencia, rojo error/alertas).
- No mencionar la API, ni cobros por radicado, ni prometer lo que una fuente no permite; de JustiBot solo se
  muestra lo que hace: vigilar procesos en las fuentes oficiales y avisar por correo de actuaciones nuevas.
- No mostrar personas reales ni recrear víctimas; los casos se cuentan con símbolos (expedientes, balanza, hologramas).
- Logo oficial del cierre: `public/logo-circular.png` (de `images/LogoCircular blanco.png`).
