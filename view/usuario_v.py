# view/view.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class UsuarioView:
    def __init__(self, root, controller):
        self.controller = controller

        # Carregar a imagem de fundo
        bg_image = Image.open("midia/imagem.jpg")
        self.bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))

        # Configurar a janela principal
        root.title("Tela Inicial")
        root.geometry("800x600")
        
        # Label para a imagem de fundo
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Frame para os botões
        self.button_frame = tk.Frame(root, bg='black')
        self.button_frame.place(relx=0.95, rely=0.05, anchor='ne')

        # Configuração de estilo para os botões
        style = ttk.Style()
        style.configure("Transparent.TButton", background="black", relief="flat")
        
        # Botões de Login e Cadastro
        self.login_button = ttk.Button(self.button_frame, text="Login", command=self.controller.show_login_view, style="Transparent.TButton")
        self.login_button.pack(side="right", padx=5)
        self.register_button = ttk.Button(self.button_frame, text="Cadastro", command=self.controller.show_register_view, style="Transparent.TButton")
        self.register_button.pack(side="right", padx=5)
