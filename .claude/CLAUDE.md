# Tienda PITBULLS (tiendapitbulls.github.io)

- Todo el sitio está en `index.html` (HTML, CSS y JS en un solo archivo). Los productos están en el arreglo `const P = [...]` dentro del script.
- Fotos de productos en `fotos/productos/`. Portada: `fotos/portada.jpg` (computador) y `fotos/portada-movil.jpg` (celular). Video de fondo del local: `videos/local.mp4`.
- **Cada vez que se agregue, cambie o quite un producto**, ejecutar `node _herramientas/generar-paginas.js` para regenerar `p/<id>.html`. Esas páginas son las que muestran la foto, el nombre y el precio como vista previa en el mensaje de pedido de WhatsApp.
- El número de WhatsApp de la tienda está en la constante `WHATSAPP` (formato 57 + celular).
- Probar en celular y computador antes de publicar.
