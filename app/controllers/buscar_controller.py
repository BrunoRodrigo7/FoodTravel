import tkinter as tk
from view.buscar_view import Filtro

class Botones:
    def crear_botones(self, ventana, entrada_consulta, entrada_tipo_cocina, entrada_precio_min, entrada_precio_max, entrada_popularidad, entrada_disponibilidad):
        marco_botones = tk.Frame(ventana)
        marco_botones.pack()
        boton_resultados = tk.Button(marco_botones, text='Mostrar resultados', command=lambda: self.boton_resultados(
            entrada_consulta.get(),
            entrada_tipo_cocina.get(),
            entrada_precio_min.get(),
            entrada_precio_max.get(),
            entrada_popularidad.get(),
            entrada_disponibilidad.get()
        ))
        boton_resultados.pack(side="left")
        
        boton_volver = tk.Button(marco_botones, text='Volver', command=lambda: self.boton_volver(ventana))
        boton_volver.pack(side="left")

    def boton_resultados(self, consulta, tipo_cocina, precio_min, precio_max, popularidad, disponibilidad):
        
        filtro = Filtro()
        resultados = filtro.buscar(consulta, tipo_cocina, precio_min, precio_max, popularidad, disponibilidad)
        
        print(resultados)
        pass 
         
    def boton_volver(self, ventana):
        ventana.destroy()
        pass