import tkinter as tk
import json

class PlanificadorRutas:
    def __init__(self, archivo_usuarios, archivo_locales, archivo_ubicaciones):
        with open("app/data/usuarios.json", "r") as file:
            self.usuarios = json.load(file)
        with open("app/data/locales.json", "r") as file:
            self.locales = json.load(file)
        with open("app/data/ubicaciones.json", "r") as file:
            self.ubicaciones = json.load(file)

        self.ubicaciones_dict = {}
        for ubicacion in self.ubicaciones:
            self.ubicaciones_dict[ubicacion["id"]] = ubicacion

        self.locales_dict = {}
        for local in self.locales:
            self.locales_dict[local["id"]] = local

    def obtener_historial_rutas(self, usuario_id):
        for usuario in self.usuarios["usuarios"]:
            if usuario["id"] == usuario_id:
                historial = []
                for ruta_id in usuario["historial_rutas"]:
                    local = self.locales_dict[ruta_id]
                    ubicacion = self.ubicaciones_dict[local["id_ubicacion"]]
                    historial.append((local["nombre"], ubicacion["direccion"]))
                return historial

    def mostrar_ventana(self):
        def actualizar_historial(event):
            usuario_seleccionado = lista_desplegable.get()
            for usuario in self.usuarios["usuarios"]:
                if usuario["nombre"] == usuario_seleccionado:
                    historial.delete("1.0", tk.END)
                    for ruta_id in usuario["historial_rutas"]:
                        local = self.locales_dict[ruta_id]
                        ubicacion = self.ubicaciones_dict[local["id_ubicacion"]]
                        historial.insert(tk.END, f"{local['nombre']} en {ubicacion['direccion']}\n")

    
        ventana = tk.Tk()
        ventana.title("Planificar Ruta")

        lista_desplegable = tk.StringVar(ventana)
        lista_desplegable.set(self.usuarios["usuarios"][0]["nombre"])  
        opciones = [usuario["nombre"] for usuario in self.usuarios["usuarios"]]
        menu = tk.OptionMenu(ventana, lista_desplegable, *opciones, command=actualizar_historial)
        menu.pack()
        
        boton_volver = tk.Button(ventana, text="Volver", command=ventana.destroy)
        boton_volver.pack()

        historial = tk.Text(ventana)
        historial.pack()

        actualizar_historial(None)

        ventana.mainloop()