# view/usuario_v.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class UsuarioView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Tela Inicial")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Carregar e configurar a imagem de fundo
        try:
            bg_image = Image.open("midia/background.png")
            self.bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
            self.bg_label = tk.Label(self, image=self.bg_photo)
            self.bg_label.place(relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Arquivo de imagem não encontrado.")

        # Frame para os botões no canto superior esquerdo
        button_frame = tk.Frame(self, bg='white', bd=0)
        button_frame.place(x=10, y=10, anchor='nw')

        # Criar botões com fundo transparente
        ttk.Button(button_frame, text="Cadastrar", command=self.controller.show_cadastro_view).pack(pady=5, padx=5, anchor='nw')
        ttk.Button(button_frame, text="Login", command=self.controller.show_login_view).pack(pady=5, padx=5, anchor='nw')
        ttk.Button(button_frame, text="Produtos", command=self.controller.show_produto_view).pack(pady=5, padx=5, anchor='nw')

        # Configurar o estilo dos botões para ter fundo transparente
        style = ttk.Style()
        style.configure('TButton', background='transparent', padding=5)


