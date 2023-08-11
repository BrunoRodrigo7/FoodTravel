import tkinter as tk
from view.inicio_view import HomeView

class LoginController:
    def __init__(self, view):
        self.view = view

    def login(self):
        home_window = tk.Toplevel(self.view)
        home_view = HomeView(home_window)