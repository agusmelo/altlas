# Atlas de Banderas

Juego web para aprender las banderas, las capitales y la ubicación de los 195 países soberanos, pensado para jugar y competir entre amigos. Esta es la versión actual del front: un único HTML sin backend, generado a partir de una plantilla y los datos de este repo.

## Cómo probarlo

Abrí `dist/index.html` en el navegador. Ya viene armado y no necesita servidor.

Para regenerarlo después de cambiar la plantilla o los datos:

```bash
python3 scripts/build.py
```

Solo necesita Python 3.8 o superior, sin dependencias.

## Estructura

| Ruta | Qué hay |
| --- | --- |
| `src/index.template.html` | Toda la app: HTML, CSS y JavaScript, con marcadores `__DATA__`, `__FLAGS__`, etc. |
| `data/paises.txt` | Código, nombre, capital, continente y primer dato curioso de cada país (separado por `\|`) |
| `data/significado-y-clave.txt` | Qué significa cada bandera y cómo reconocerla |
| `data/datos-curiosos-2.txt` | Segundo dato curioso de cada país |
| `data/ficha.json` | Superficie, puesto, idiomas, moneda, dominio web, salida al mar |
| `data/banderas-parecidas.json` | Grupos de banderas que se confunden entre sí |
| `data/geo.json` | Código numérico ISO y coordenadas del centro de cada país |
| `data/nombres-mapa.json` | Nombres en español de todos los territorios del mapa |
| `data/world-countries-50m.topo.json` | Mapa del mundo (TopoJSON, escala 1:50 m) |
| `public/flags/*.svg` | Las 195 banderas, sin modificar |
| `scripts/build.py` | Arma `dist/index.html` embebiendo todo lo anterior |

## Cosas a tener en cuenta

- **Registro compartido:** el registro de exploradores y la tabla "Hoy en el grupo" usan la base de datos que ofrece Claude a los artifacts publicados (`window.claude.use("db")`). Fuera de Claude esa parte muestra un aviso y el resto del juego funciona igual.
- **Progreso:** se guarda en el `localStorage` del navegador.
- **Banderas:** se insertan en línea; el código les pone IDs únicos y les quita `<title>`/`<desc>` en cada inserción. No optimizarlas con svgo: comparten IDs cortos y se rompen al aparecer varias juntas.
- **Textos:** los datos curiosos, significados y claves fueron escritos para el juego y todavía no tienen una revisión editorial con fuentes.

## Fuentes y licencias

- Banderas: [hampusborgos/country-flags](https://github.com/hampusborgos/country-flags), de Wikimedia Commons, dominio público.
- Mapa: [topojson/world-atlas](https://github.com/topojson/world-atlas), basado en [Natural Earth](https://www.naturalearthdata.com/), dominio público.
- Códigos, coordenadas, superficie, idiomas y monedas: [mledoze/countries](https://github.com/mledoze/countries), licencia ODbL.
- Librerías cargadas desde CDN: D3 v7 y topojson-client.
- Tipografías: IM Fell English y EB Garamond (Google Fonts, licencia OFL).
