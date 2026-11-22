# Tienda PITBULLS (tiendapitbulls.github.io)

- Todo el sitio está en `index.html` (HTML, CSS y JS en un solo archivo). Los productos están en el arreglo `const P = [...]` dentro del script.
- Fotos de productos en `fotos/productos/`. Portada: `fotos/portada.jpg` (computador) y `fotos/portada-movil.jpg` (celular). Video de fondo del local: `videos/local.mp4`.
- **Cada vez que se agregue, cambie o quite un producto**, ejecutar `node _herramientas/generar-paginas.js` para regenerar `p/<id>.html`. Esas páginas son las que muestran la foto, el nombre y el precio como vista previa en el mensaje de pedido de WhatsApp.
- Números de WhatsApp: constante `ASESORES` (Asesor 1 = 322 655 2041, Asesor 2 = 313 305 8948, formato 57 + celular). `WHATSAPP` = Asesor 1, se usa en el botón flotante, el menú y las preguntas.
- Probar en celular y computador antes de publicar.
- Fotos de producto: encuadrarlas con `python3 _herramientas/encuadrar.py ORIGEN fotos/productos/NOMBRE.jpg x0,y0,x1,y1` (caja de la prenda de la pretina al ruedo, sin gancho, en píxeles de la foto original). Así todas quedan del mismo tamaño y centradas (1000×1250, prenda al 80 % del alto). La usuaria prefiere fotos con el fondo del local, sin quitar fondo.
- Precio por defecto: las bermudas nuevas van a $85.000 salvo que la usuaria diga otro precio (las Purple Brand 1.1 ya subidas están a $150.000).
- Precio por defecto: las pantalonetas de algodón van a $70.000 salvo que la usuaria diga otro precio.
- Precio por defecto: las pantalonetas 1.1 van a $90.000 y llevan '1.1' en el nombre, salvo que la usuaria diga otro precio.
- Camisetas (categoría Camisetas): 'Alto gramaje' a $100.000 y 'Top quality' a $95.000. El tipo NO se muestra en el sitio (es solo interno para fijar el precio). Nombre: 'Camiseta <Marca>' según la foto, con descripción corta tipo 'Camiseta importada <Marca>'. La usuaria manda las fotos por lotes de una misma talla y dice si son top o alto gramaje.
- Productos pueden tener 'd' (descripción corta que se ve al abrir el producto) e 'img2' (segunda foto, p. ej. la espalda: se ve en miniaturas al abrir y al pasar el mouse en computador).
