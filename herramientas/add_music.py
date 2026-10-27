"""Uso: python3 add_music.py video.mp4 cancion.mp3 salida.mp4 [inicio_seg|auto]
Pone música de fondo: arranca donde la canción ya suena llena, fade in/out, volumen normalizado (-16 LUFS)."""
import sys, subprocess, numpy as np
vid, song, out = sys.argv[1:4]; start = sys.argv[4] if len(sys.argv) > 4 else "auto"
dur = float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",vid]))
if start == "auto":
    raw = subprocess.check_output(["ffmpeg","-v","error","-i",song,"-ac","1","-ar","8000","-f","s16le","-"])
    x = np.frombuffer(raw, np.int16).astype(float); w = 4000
    rms = np.sqrt(np.array([np.mean(x[i:i+w]**2) for i in range(0, len(x)-w, w)]))
    thr = 0.75*np.median(rms); s = next(i for i,r in enumerate(rms) if r >= thr)
    start = max(0, s*0.5 - 0.5)
start = float(start); fo = max(0, dur-1.5)
af = f"[1:a]atrim={start}:{start+dur},asetpts=PTS-STARTPTS,loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.4,afade=t=out:st={fo}:d=1.5[a]"
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",vid,"-i",song,"-filter_complex",af,"-map","0:v","-map","[a]",
    "-c:v","copy","-c:a","aac","-b:a","192k","-ar","44100","-t",str(dur),"-movflags","+faststart",out], check=True)
print(f"{out}  (música desde {start:.1f}s, {dur:.1f}s)")
