"""Paso 1 para encuadrar: dibuja una cuadrícula con coordenadas sobre la foto original
para medir la caja exacta de la prenda. Uso: python3 _herramientas/cuadricula.py FOTO salida.jpg"""
import sys
from PIL import Image, ImageDraw, ImageOps
im=ImageOps.exif_transpose(Image.open(sys.argv[1])).convert('RGB');W,H=im.size;sc=0.4
sm=im.resize((int(W*sc),int(H*sc)));d=ImageDraw.Draw(sm)
for x in range(0,W,100):
    X=int(x*sc);d.line([(X,0),(X,sm.height)],fill=(255,0,0) if x%500==0 else (0,255,255))
    if x%200==0:d.text((X+2,2),str(x),fill=(255,255,0))
for y in range(0,H,100):
    Y=int(y*sc);d.line([(0,Y),(sm.width,Y)],fill=(255,0,0) if y%500==0 else (0,255,255))
    if y%200==0:d.text((2,Y+2),str(y),fill=(255,255,0))
sm.save(sys.argv[2],quality=80);print(W,H)
