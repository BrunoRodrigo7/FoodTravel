import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
import json
from PIL import Image, ImageTk
from view.actividades_view import Eventos

class VistaPrincipal:
    def __init__(self, root, seleccionar_local_callback=None, seleccionar_ubicacion_callback=None):
        self.root = root
        self.seleccionar_local_callback = seleccionar_local_callback
        self.seleccionar_ubicacion_callback = seleccionar_ubicacion_callback
        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='right')

        self.frame_locales = tk.Frame(self.root, width=300, height=600)
        self.frame_locales.pack(side='left', fill='both', expand=True)

        # Placeholder para el mapa
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        # Listbox para los locales
        self.lista_locales = tk.Listbox(self.frame_locales)
        self.lista_locales.bind('<<ListboxSelect>>', self.mostrar_info_local)
        self.lista_locales.pack(fill='both', expand=True)
        
    def agregar_local(self, local):
        nombre = local.nombre
        self.lista_locales.insert(tk.END, nombre)

    def mostrar_info_local(self, event):
        # Obtener el índice del elemento seleccionado
        index = self.lista_locales.curselection()[0]
        # Obtener el nombre del local seleccionado
        nombre_local = self.lista_locales.get(index)
        # Buscar la información del local en el archivo JSON
        with open("app/data/locales.json", 'r') as f:
            locales = json.load(f)
            for local in locales:
                if local["nombre"] == nombre_local:
                    info_local = local
                    break
        # Crear una nueva ventana para mostrar la información
        info_window = tk.Toplevel(self.root)
        info_window.title(nombre_local)
        # Agregar widgets para mostrar la información
        tk.Label(info_window, text="Nombre: " + info_local["nombre"]).pack()
        tk.Label(info_window, text="Tipo de cocina: " + info_local["tipo_cocina"]).pack()
        # Convertir la lista de ingredientes en una cadena de texto
        ingredientes_str = ", ".join(info_local["ingredientes"])
        # Mostrar la cadena de texto en una etiqueta
        tk.Label(info_window, text="Ingredientes: " + ingredientes_str).pack()
        precio_minimo_str = str(info_local["precio_minimo"])
        precio_maximo_str = str(info_local["precio_maximo"])
        popularidad_str = str(info_local["popularidad"])
        # Mostrar la cadena de texto en una etiqueta
        tk.Label(info_window, text="Precio Minimo: " + precio_minimo_str).pack()
        tk.Label(info_window, text="Precio Maximo: " + precio_maximo_str).pack()
        tk.Label(info_window, text="Popularidad: " + popularidad_str).pack()
        tk.Label(info_window, text="Disponibilidad: " + info_local["disponibilidad"]).pack()
        # Agrego un botón para dirigir a la ventana de eventos
        event_button = tk.Button(info_window, text="Eventos", command=self.mostrar_eventos)
        event_button.pack()
        # Agregar un botón para cerrar la ventana
        tk.Button(info_window, text="Volver", command=info_window.destroy).pack()
        
    def mostrar_eventos(self):
        eventos_mostrar = Eventos(self.root)
          
        
    def agregar_marcador_mapa(self, latitud, longitud, texto, imagen=None):
        return self.mapa.set_marker(latitud, longitud, text=texto, image=imagen, command=self.seleccionar_ubicacion_callback)