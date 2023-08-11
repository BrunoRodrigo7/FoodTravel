import tkinter as tk
import tkintermapview
import json
from models.local import Local
from models.ubicacion import Ubicacion
from models.actividades import Actividad
from models.rutas_visitas import VisitRoute
from controllers.login_controller import LoginController
from controllers.mapa_controller import ControladorPrincipal
from controllers.buscar_controller import Botones
from view.login_view import LoginView
from view.inicio_view import HomeView
from view.mapa_view import VistaPrincipal
from view.buscar_view import Filtro
from view.actividades_view import Eventos
from view.reviews_view import ReviewVentana

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x300")
        login_views = LoginView(self.root)
        self.root.mainloop()
        
        
if __name__ == "__main__":
    app = MainApp()