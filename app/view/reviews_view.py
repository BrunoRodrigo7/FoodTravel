import json
from tkinter import Tk, Label, Entry, Button, Text, OptionMenu, StringVar

class ReviewVentana:
    def __init__(self):
        self.window = Tk()
        self.window.title("Reviews")
        self.reviews = []
        self.locales = []
        self.usuarios = []
        self.Cargar_datos()
        self.seleccion_locales = StringVar(self.window)
        self.seleccion_locales.set(self.locales[0]["nombre"])
        self.seleccion_locales.trace("w", self.actuali_reviews)
        self.locales_optionmenu = OptionMenu(self.window, self.seleccion_locales, *[locales["nombre"] for locales in self.locales])
        self.locales_optionmenu.pack()
        self.reviews_texto = Text(self.window)
        self.reviews_texto.pack()
        self.actuali_reviews()
        self.coment_entry = Entry(self.window)
        self.coment_entry.pack()
        self.publi_button = Button(self.window, text="Publicar", command=self.publi_comentario)
        self.publi_button.pack()
        self.volv_button = Button(self.window, text="Volver", command=self.volver)
        self.volv_button.pack()

    def Cargar_datos(self):
        with open("app/data/reviews.json", "r") as f:
            self.reviews = json.load(f)
        with open("app/data/locales.json", "r") as f:
            self.locales = json.load(f)
        with open("app/data/usuarios.json", "r") as f:
            data = json.load(f)
            self.usuarios = data["usuarios"]

    def cargar_nombre_usuario(self, id_usuario):
        usuario = next(usuario for usuario in self.usuarios if usuario["id"] == id_usuario)
        return usuario["nombre"]

    def actuali_reviews(self, *args):
        selected_locales_nombre = self.seleccion_locales.get()
        selected_locale = next(locale for locale in self.locales if locale["nombre"] == selected_locales_nombre)
        locale_reviews = [review for review in self.reviews if review["id_destino"] == selected_locale["id"]]
        reviews_text = "\n".join(f"Usuario {review['id']}: {review['comentario']} (Calificación: {review['calificacion']})" for review in locale_reviews)
        self.reviews_texto.delete("1.0", "end")
        self.reviews_texto.insert("end", reviews_text)


    def publi_comentario(self):
        comentar = self.coment_entry.get()
        seleccion_locales_nombre = self.seleccion_locales.get()
        seleccion_locales = next(locale for locale in self.locales if locale["nombre"] == seleccion_locales_nombre)
        id_usuario = 1 
        nueva_review = {
        "id": len(self.reviews) + 1,
        "id_destino": seleccion_locales["id"],
        "id_usuario": id_usuario,
        "calificacion": 5,
        "comentario": comentar
    }
        self.reviews.append(nueva_review)
        with open("app/data/reviews.json", "w") as f:
            json.dump(self.reviews, f)
            self.actuali_reviews()

    def volver(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()