#!/usr/bin/env python3
"""Arma dist/index.html: toma la plantilla y le embebe los datos, las banderas y el mapa.

Uso:  python3 scripts/build.py
No necesita dependencias: solo Python 3.8+.
"""
import json, os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "data"
read = lambda p: (D / p).read_text(encoding="utf-8")

codes = [l.split("|")[0] for l in read("paises.txt").splitlines() if l.strip()]
flags = {c.lower(): (ROOT / "public" / "flags" / f"{c.lower()}.svg").read_text(encoding="utf-8") for c in codes}

replacements = {
    "__DATA__": json.dumps(read("paises.txt"), ensure_ascii=False),
    "__INFO__": json.dumps(read("significado-y-clave.txt"), ensure_ascii=False),
    "__FACTS2__": json.dumps(read("datos-curiosos-2.txt"), ensure_ascii=False),
    "__FICHA__": read("ficha.json"),
    "__SIMILAR__": json.dumps(json.loads(read("banderas-parecidas.json")), ensure_ascii=False),
    "__GEO__": json.dumps(json.loads(read("geo.json"))),
    "__MAPNAMES__": json.dumps(json.loads(read("nombres-mapa.json")), ensure_ascii=False),
    "__WORLD__": read("world-countries-50m.topo.json"),
    "__FLAGS__": json.dumps(flags),
}

html = (ROOT / "src" / "index.template.html").read_text(encoding="utf-8")
for key, value in replacements.items():
    html = html.replace(key, value)

out = ROOT / "dist" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"Listo: {out.relative_to(ROOT)} ({len(html) // 1024} KB)")
