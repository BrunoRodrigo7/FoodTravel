import json

class Filtro:
    def __init__(self):
        with open("app/data/ubicaciones.json", "r") as f:
            self.ubicaciones = json.load(f)
        with open("app/data/locales.json", "r") as f:
            self.locales = json.load(f)

    def buscar(self, consulta, tipo_cocina=None, precio_min=None, precio_max=None, popularidad=None, disponibilidad=None):
        resultados = []
        for local in self.locales:
            if consulta.lower() not in local["nombre"].lower():
                continue
            if tipo_cocina and local["tipo_cocina"] != tipo_cocina:
                continue
            precio_min_local = float(local["precio_minimo"])
            if precio_min and precio_min_local < float(precio_min):
                continue
            precio_max_local = float(local["precio_maximo"])
            if precio_max and precio_max_local > float(precio_max):
                continue
            popularidad_local = float(local["popularidad"])
            if popularidad and popularidad_local < float(popularidad):
                continue
            if disponibilidad and local["disponibilidad"] != disponibilidad:
                continue

            
            ubicacion = next((u for u in self.ubicaciones if u["id"] == local["id_ubicacion"]), None)
            if ubicacion:
                resultados.append({
                    "nombre": local["nombre"],
                    "direccion": ubicacion["direccion"],
                    "latitud": ubicacion["latitud"],
                    "longitud": ubicacion["longitud"]
                })
        return resultados
    