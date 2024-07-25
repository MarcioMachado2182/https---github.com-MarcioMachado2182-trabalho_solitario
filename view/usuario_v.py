import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class UsuarioView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg='white')
        
        # Carregar a imagem de fundo
        bg_image = Image.open("midia/casal_caveira.jpg")
        self.bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)
        
        self.create_widgets()

    def create_widgets(self):
        """Cria os widgets da tela inicial"""
        # Frame para os botões
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.place(relx=0.95, rely=0.05, anchor='ne')

        # Configuração de estilo para os botões
        style = ttk.Style()
        style.configure("Transparent.TButton", background="white", relief="flat")

        # Botões para navegar entre as telas
        self.login_button = ttk.Button(self.button_frame, text="Login", command=self.controller.show_login_view, style="Transparent.TButton")
        self.login_button.pack(side="right", padx=5)
        self.register_button = ttk.Button(self.button_frame, text="Cadastro", command=self.controller.show_register_view, style="Transparent.TButton")
        self.register_button.pack(side="right", padx=5)
        self.produtos_button = ttk.Button(self.button_frame, text="Produtos", command=self.controller.show_produto_view, style="Transparent.TButton")
        self.produtos_button.pack(side="right", padx=5)

