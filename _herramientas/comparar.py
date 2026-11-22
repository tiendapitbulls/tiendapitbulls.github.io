"""Paso 3: compara fotos ya encuadradas con líneas guía (altura de cuello/pretina y ruedo, y centro).
Uso: python3 _herramientas/comparar.py salida.jpg fotos/productos/a.jpg fotos/productos/b.jpg ...
Incluir siempre 1-2 fotos ya publicadas de la misma categoría como referencia."""
import sys
from PIL import Image, ImageDraw
fs=sys.argv[2:];a=[]
for f in fs:
    im=Image.open(f).resize((240,300));d=ImageDraw.Draw(im)
    for y in (30,270): d.line([(0,y),(240,y)],fill=(255,0,0))
    d.line([(120,0),(120,300)],fill=(0,200,255));a.append(im)
s=Image.new('RGB',(250*len(a),300),(255,255,255))
for i,im in enumerate(a): s.paste(im,(i*250,0))
s.save(sys.argv[1])
