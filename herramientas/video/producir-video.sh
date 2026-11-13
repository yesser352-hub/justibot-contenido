#!/usr/bin/env bash
# Produce un video del robot de JustiBot de principio a fin, con la voz oficial (es-CO-GonzaloNeural).
# Uso (Git Bash, desde la carpeta videos/):
#   bash producir-video.sh 08            -> todo: voz, música, imagen, unión, portada, revisión y archivos finales
#   bash producir-video.sh 08 unir       -> no repite voz ni render: solo une, portada, revisión y archivos finales
#   bash producir-video.sh 08 todo piper -> voz provisional sin internet (solo pruebas)
# El video debe estar en videos.conf (una línea por video) y tener sus carpetas voiceN/, audioN/ y src/<carpeta>/.
# Necesita: Node 22 (npm install hecho), Python con numpy scipy pillow edge-tts, FFmpeg y Chrome.
set -euo pipefail
trap 'echo "ERROR: el paso falló en la línea $LINENO (código $?). Copia este mensaje y envíaselo a Claude."' ERR
cd "$(dirname "$0")"
NN="${1:?Falta el número del video, por ejemplo: bash producir-video.sh 08}"
DESDE="${2:-todo}"
ENGINE="${3:-edge}"
LINEA=$(grep -E "^${NN}\|" videos.conf || true)
[[ -n "$LINEA" ]] || { echo "El video $NN no está en videos.conf. Agrega su línea primero."; exit 1; }
IFS='|' read -r _ SLUG SRC COMP PRE POR_CFG <<< "$LINEA"
N=$((10#$NN))
VOICE=voice$N; AUDIO=audio$N
PY=python; command -v python >/dev/null || PY=python3
if [[ "${OS:-}" == "Windows_NT" && -d "D:/" ]]; then export REMOTION_TMP=D:/remotion-tmp TEMP=D:/remotion-tmp TMP=D:/remotion-tmp; mkdir -p D:/remotion-tmp; fi
mkdir -p out/portada out/listos
echo "### Video $NN · $SLUG ($COMP)"

if [[ "$DESDE" != "unir" ]]; then
echo "== 1. Voz ($ENGINE), pista y subtítulos"
( cd "$VOICE"
  if [[ "$ENGINE" == "edge" ]]; then $PY gen_voice.py edge "+6%"; else $PY gen_voice.py piper 0.95; fi
  $PY -X utf8 assemble.py
  $PY -X utf8 subs.py > /dev/null
  cp words.json subs.json meta.json "../src/$SRC/" )

echo "== 2. Música, efectos y mezcla (-14 LUFS)"
( cd "$AUDIO" && $PY -X utf8 "score$N.py" )

echo "== 3. Imagen (1080x1920, H.264)"
if [[ "${OS:-}" == "Windows_NT" ]]; then
  npx remotion render src/index.ts "$COMP" "out/${PRE}_raw.mp4" --codec h264 --crf 16 --gl angle --concurrency 3
else
  npx remotion render src/index.ts "$COMP" "out/${PRE}_raw.mp4" --codec h264 --crf 16 --gl swangle --concurrency 2 \
    --browser-executable "${CHROME:-/usr/bin/google-chrome}" --props '{"draft":true,"dpr":0.6667}'
fi
fi

echo "== 4. Unir imagen y sonido"
for intento in 1 2 3; do sleep 2; ffmpeg -nostdin -y -v warning -i "out/${PRE}_raw.mp4" -i "$AUDIO/mix.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 256k -movflags +faststart -shortest "out/${PRE}_final.mp4" && break; echo "reintentando la unión ($intento)..."; done
test -s "out/${PRE}_final.mp4"
cp "$VOICE/subtitulos.srt" "out/${PRE}_subtitulos.srt"

echo "== 5. Portada (sin subtítulos)"
if [[ "$POR_CFG" == palabra:* ]]; then
  P="${POR_CFG#palabra:}"
  POR=$($PY -c "import json,sys;W=json.load(open('$VOICE/words.json',encoding='utf-8'));print(round([x for x in W if x['scene']==1 and x['w'].lower().startswith('$P')][0]['t0']*30)-14)")
else POR="$POR_CFG"; fi
COMP="$COMP" node scripts/stills.mjs "out/portada/${PRE}_" "$POR" 1 '{"subs":false}'

echo "== 6. Revisión de calidad"
$PY -X utf8 scripts/short_qa.py "out/${PRE}_final.mp4" "out/qa$N" || true

echo "== 7. Archivos finales para justibot-contenido"
FIN="out/listos/justibot-$NN-$SLUG"
BYTES=$(stat -c %s "out/${PRE}_final.mp4" 2>/dev/null || wc -c < "out/${PRE}_final.mp4")
if (( BYTES > 90000000 )); then
  echo "Pesa más de 90 MB: recomprimiendo (CRF 21)"
  ffmpeg -nostdin -y -v warning -i "out/${PRE}_final.mp4" -c:v libx264 -crf 21 -preset veryfast -c:a copy -movflags +faststart "$FIN.mp4"
else cp "out/${PRE}_final.mp4" "$FIN.mp4"; fi
cp "out/portada/${PRE}_${POR}.jpg" "$FIN.jpg"
echo "Listo: $FIN.mp4 y $FIN.jpg (revisión en out/qa$N). Avísale a Claude para revisarlo y, con tu aprobación, subirlo."
