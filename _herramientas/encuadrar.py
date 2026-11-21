"""Encuadra una foto de producto: detecta la prenda (tela de color) y la deja siempre del mismo tamaño y centrada.
Uso: python3 _herramientas/encuadrar.py ORIGEN DESTINO x0,y0,x1,y1 [alto_prenda=0.80] [debug.jpg]
La caja x0,y0,x1,y1 es la prenda en píxeles de la foto original (de la pretina al ruedo, sin el gancho).
La detección automática por color existe pero falla con fondos azules o tela clara: es mejor pasar la caja."""
import sys, cv2, numpy as np
from PIL import Image, ImageOps
def caja_prenda(rgb):
    h,w=rgb.shape[:2];s=600/max(h,w)
    sm=cv2.resize(rgb,None,fx=s,fy=s,interpolation=cv2.INTER_AREA)
    hsv=cv2.cvtColor(sm,cv2.COLOR_RGB2HSV)
    H,S,V=hsv[...,0].astype(int),hsv[...,1].astype(int),hsv[...,2].astype(int)
    m=((H>=90)&(H<=130)&(S>=35)&(V>=45)).astype(np.uint8)          # tela azul (jean)
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(m)
    k=1+np.argmax(st[1:,cv2.CC_STAT_AREA]);x,y,bw,bh=st[k][:4]
    return np.array([x,y,x+bw,y+bh])/s
def encuadrar(src,dst,alto=0.80,cw=1000,ch=1250,debug=None,caja=None):
    im=ImageOps.exif_transpose(Image.open(src)).convert('RGB');rgb=np.array(im)
    x0,y0,x1,y1=caja if caja else caja_prenda(rgb)
    gw,gh=x1-x0,y1-y0
    sc=min(ch*alto/gh,cw*0.88/gw)
    cx,cy=(x0+x1)/2,(y0+y1)/2
    W,H=cw/sc,ch/sc
    left,top=cx-W/2,cy-H/2+H*0.015
    # si la ventana se sale de la foto, rellenar con bordes estirados y desenfocados
    pad=int(max(0,-left,-top,left+W-rgb.shape[1],top+H-rgb.shape[0]))+2
    if pad>2:
        big=cv2.copyMakeBorder(rgb,pad,pad,pad,pad,cv2.BORDER_REPLICATE)
        blur=cv2.GaussianBlur(big,(0,0),25);mask=np.zeros(big.shape[:2],np.float32);mask[pad:-pad,pad:-pad]=1
        mask=cv2.GaussianBlur(mask,(0,0),8)[...,None];rgb=(big*mask+blur*(1-mask)).astype(np.uint8);left+=pad;top+=pad
    crop=Image.fromarray(rgb).crop((int(left),int(top),int(left+W),int(top+H))).resize((cw,ch),Image.LANCZOS)
    crop.save(dst,quality=85,optimize=True,progressive=True)
    if debug:
        d=rgb.copy();cv2.rectangle(d,(int(x0+(pad if pad>2 else 0)),int(y0+(pad if pad>2 else 0))),(int(x1+(pad if pad>2 else 0)),int(y1+(pad if pad>2 else 0))),(255,0,0),8)
        Image.fromarray(d).resize((d.shape[1]//5,d.shape[0]//5)).save(debug)
    return (x0,y0,x1,y1)
if __name__=='__main__':
    a=sys.argv;caja=[float(v) for v in a[3].split(',')]
    print(encuadrar(a[1],a[2],float(a[4]) if len(a)>4 else 0.80,debug=a[5] if len(a)>5 else None,caja=caja))
