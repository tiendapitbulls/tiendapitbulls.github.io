// Genera p/<id>.html para cada producto: páginas con vista previa (foto, nombre y precio)
// para los links que van en el mensaje de WhatsApp. Uso: node _herramientas/generar-paginas.js
const fs=require('fs'),path=require('path');
const root=path.join(__dirname,'..');
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const src=html.match(/const P = (\[[\s\S]*?\n\]);/)[1];
const P=Function('return '+src)();
const SITE='https://tiendapitbulls.github.io/';
const esc=s=>String(s).replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
const money=v=>'$'+v.toLocaleString('es-CO').replace(/,/g,'.');
const dir=path.join(root,'p');fs.mkdirSync(dir,{recursive:true});
for(const f of fs.readdirSync(dir))if(f.endsWith('.html'))fs.unlinkSync(path.join(dir,f));
for(const p of P){
  const img=SITE+(p.img||'fotos/portada.jpg');
  const title=`${p.n} · ${money(p.p)}`;
  const desc=[p.col,p.c,'PITBULLS · Fundación, Magdalena'].filter(Boolean).join(' · ');
  const go=`../#p-${p.id}`;
  fs.writeFileSync(path.join(dir,`${p.id}.html`),`<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)} · PITBULLS</title>
<meta name="description" content="${esc(desc)}">
<meta property="og:type" content="product">
<meta property="og:site_name" content="PITBULLS">
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:image" content="${esc(img)}">
<meta property="og:url" content="${SITE}p/${p.id}.html">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../fotos/favicon.png">
<meta http-equiv="refresh" content="0; url=${go}">
<script>location.replace(${JSON.stringify(go)})</script>
</head><body style="background:#000;color:#fff;font-family:system-ui;text-align:center;padding:40px">
<p><a href="${go}" style="color:#d9b768">Ver ${esc(p.n)} en PITBULLS</a></p>
</body></html>
`);
}
console.log('Páginas generadas:',P.length);
