import tkintermapview
import tkinter as tk
import json
from view.buscar_view import Filtro
from view.mapa_view import VistaPrincipal
from view.plan_view import PlanificadorRutas
from view.reviews_view import ReviewVentana
from controllers.mapa_controller import ControladorPrincipal
from controllers.buscar_controller import Botones


class HomeView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.menu_inicio()

    def menu_inicio(self):
        self.explore_button = tk.Button(self, text="Explorar", command=self.abrir_mapa)
        self.explore_button.pack()
        self.search_button = tk.Button(self, text="Buscar", command=self.busqueda_mapa)
        self.search_button.pack()
        self.plan_button = tk.Button(self, text="Planificar", command=self.planificacion_rutas)
        self.plan_button.pack()
        self.review_button = tk.Button(self, text="Reseñas", command=self.mostrar_reviews)
        self.review_button.pack()
        self.back_button = tk.Button(self, text="Volver", command=self.master.destroy)
        self.back_button.pack()
        
    def abrir_mapa(self):
        map_window = tk.Toplevel(self.master)
        controlador = ControladorPrincipal(map_window)
        
    
    def busqueda_mapa(self):
        botones = Botones()
        ventana_busqueda = tk.Toplevel(self.master)
        ventana_busqueda.title("Búsqueda")

        marco_entradas = tk.Frame(ventana_busqueda)
        marco_entradas.pack()
  
        tk.Label(marco_entradas, text="Consulta:").pack()
        entrada_consulta = tk.Entry(marco_entradas)
        entrada_consulta.pack()

        tk.Label(marco_entradas, text="Tipo de cocina:").pack()
        entrada_tipo_cocina = tk.Entry(marco_entradas)
        entrada_tipo_cocina.pack()

        tk.Label(marco_entradas, text="Precio mínimo:").pack()
        entrada_precio_min = tk.Entry(marco_entradas)
        entrada_precio_min.pack()

        tk.Label(marco_entradas, text="Precio máximo:").pack()
        entrada_precio_max = tk.Entry(marco_entradas)
        entrada_precio_max.pack()

        tk.Label(marco_entradas, text="Popularidad:").pack()
        entrada_popularidad = tk.Entry(marco_entradas)
        entrada_popularidad.pack()

        tk.Label(marco_entradas, text="Disponibilidad:").pack()
        entrada_disponibilidad = tk.Entry(marco_entradas)
        entrada_disponibilidad.pack()


        botones.crear_botones(ventana_busqueda, entrada_consulta, entrada_tipo_cocina, entrada_precio_min, entrada_precio_max, entrada_popularidad, entrada_disponibilidad)
        
    def planificacion_rutas(self):
        planificador = PlanificadorRutas("app/data/usuarios.json", "app/data/locales.json", "app/data/ubicaciones.json")

        usuarios = planificador.usuarios
        locales = planificador.locales
        ubicaciones = planificador.ubicaciones

        ubicaciones_dict = {}
        for ubicacion in ubicaciones:
            ubicaciones_dict[ubicacion['id']] = ubicacion

        locales_dict = {}
        for local in locales:
            locales_dict[local['id']] = local

        planificador.mostrar_ventana()
        
    def mostrar_reviews(self):
        review_window = ReviewVentana()
        review_window.run()