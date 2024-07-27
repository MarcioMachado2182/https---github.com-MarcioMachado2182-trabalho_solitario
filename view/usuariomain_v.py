# view/main_v.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class MainApplication(tk.Toplevel):
    def __init__(self, root=None, controller=None):
        super().__init__(root)
        self.title("Tela Inicial")
        self.geometry("800x600")
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Tela inicial com imagem de fundo
        self.bg_image = Image.open("midia/Feeling.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((800, 600)))
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Frame para os botões no canto superior esquerdo
        button_frame = tk.Frame(self, bg='white', bd=0)
        button_frame.place(x=10, y=10, anchor='nw')

        # Criar botões com fundo transparente
        ttk.Button(button_frame, text="Cadastrar", command=self.controller.show_cadastro).grid(row=0, column=0, padx=5, pady=5, sticky='nw')
        ttk.Button(button_frame, text="Login", command=self.controller.show_login).grid(row=1, column=0, padx=5, pady=5, sticky='nw')
        ttk.Button(button_frame, text="Produtos", command=self.controller.show_produtos).grid(row=2, column=0, padx=5, pady=5, sticky='nw')





