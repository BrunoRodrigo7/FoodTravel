import json
import tkinter as tk
from view.inicio_view import HomeView

class LoginView():
    def __init__(self, root):
        self.root = root
        self.username_label = tk.Label(self.root, text="Usuario:")
        self.username_entry = tk.Entry(self.root)
        self.password_label = tk.Label(self.root, text="Contraseña:")
        self.password_entry = tk.Entry(self.root, show="*")
        self.login_button = tk.Button(self.root, text="Iniciar Sesion", command=self.login)

        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
    

    def login(self):
        
        with open('app/data/usuarios.json', 'r') as f:
            data = json.load(f)

        username = self.username_entry.get()
        password = self.password_entry.get()

        for user in data["usuarios"]:
            if user["nombre"] == username and user["contrasena"] == password:
                home_window = tk.Toplevel(self.root)
                home_view = HomeView(home_window)
                break
        else:
            print("Error", "Nombre de usuario o contraseña incorrectos")
            
           