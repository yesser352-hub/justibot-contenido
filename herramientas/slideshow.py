"""Uso: python3 slideshow.py carpeta_png salida.mp4 [seg_por_slide]  -> video 1080x1920 para TikTok"""
import sys, glob, subprocess
from PIL import Image
d, out = sys.argv[1:3]; per = float(sys.argv[3]) if len(sys.argv)>3 else 4.0
files = sorted(glob.glob(f"{d}/*.png")); x = 0.4
c = Image.open(files[0]).convert("RGB").getpixel((5,1345)); col = "0x%02x%02x%02x" % c
inp = []; fl = []
for i,f in enumerate(files):
    inp += ["-loop","1","-t",str(per+x),"-i",f]
    fl.append(f"[{i}:v]scale=1080:1350,pad=1080:1920:0:285:color={col},fps=30,format=yuv420p,setsar=1[v{i}]")
prev = "v0"
for i in range(1,len(files)):
    fl.append(f"[{prev}][v{i}]xfade=transition=slideleft:duration={x}:offset={i*per}[x{i}]"); prev=f"x{i}"
subprocess.run(["ffmpeg","-y","-loglevel","error",*inp,"-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-filter_complex",";".join(fl),
  "-map",f"[{prev}]","-map",f"{len(files)}:a","-t",str(per*len(files)+x),"-c:v","libx264","-crf","18","-pix_fmt","yuv420p","-c:a","aac","-movflags","+faststart",out],check=True)
print(out)
