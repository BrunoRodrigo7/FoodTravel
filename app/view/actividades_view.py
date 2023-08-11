import tkinter as tk
import json
from datetime import datetime

class Eventos:
    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.title("Eventos")

        with open("app/data/actividades.json", "r") as f:
            self.actividades = json.load(f)
        with open("app/data/ubicaciones.json", "r") as f:
            self.ubicaciones = json.load(f)
        with open("app/data/locales.json", "r") as f:
            self.locales = json.load(f)

        self.local_var = tk.StringVar()
        self.local_var.set(self.locales[0]["nombre"])
        local_menu = tk.OptionMenu(self.window, self.local_var, *[l["nombre"] for l in self.locales])
        local_menu.pack()

        actu_boton = tk.Button(self.window, text="Actualizar", command=self.actualizar_eventos)
        actu_boton.pack()

        imprim_boton = tk.Button(self.window, text="Confirmar Asistencia", command=self.imprimir_asist)
        imprim_boton.pack(pady=10)

        volver_boton = tk.Button(self.window, text="Volver", command=self.window.destroy)
        volver_boton.pack(pady=10)

    def actualizar_eventos(self):
        for widget in self.window.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

        local_nombre = self.local_var.get()
        local_id = next(l["id"] for l in self.locales if l["nombre"] == local_nombre)

        self.actividades_filtradas = [a for a in self.actividades if a["local_id"] == local_id]

        for actividad in self.actividades_filtradas:
            evento_frame = tk.Frame(self.window)
            evento_frame.pack(fill=tk.X, padx=10, pady=5)

            evento_nombre = tk.Label(evento_frame, text=actividad["nombre"])
            evento_nombre.pack(side=tk.LEFT)

            hora_inicio = datetime.fromisoformat(actividad["hora_inicio"])
            hora_str = hora_inicio.strftime("%H:%M")
            evento_inicio_hora = tk.Label(evento_frame, text=hora_str)
            evento_inicio_hora.pack(side=tk.LEFT)

            ubicacion_id = actividad['id_ubicacion']
            ubicacion = next(u for u in self.ubicaciones if u["id"] == ubicacion_id)
            event_location = tk.Label(evento_frame, text=ubicacion['direccion'])
            event_location.pack(side=tk.LEFT)

            event_local = tk.Label(evento_frame, text=local_nombre)
            event_local.pack(side=tk.LEFT)

    def imprimir_asist(self):
        for actividad in self.actividades_filtradas:
            print(actividad["nombre"] + ": " + str(actividad['asistencia']))