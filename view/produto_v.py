import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ProdutoView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Produtos")
        self.geometry("800x600")

        # Carregar a imagem de fundo
        bg_image = Image.open("midia/Feeling.png")
        self.bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        """Cria os widgets da tela de produtos"""
        # Frame para os botões
        self.button_frame = tk.Frame(self, bg='white')
        self.button_frame.place(relx=0.95, rely=0.05, anchor='ne')

        # Configuração de estilo para os botões
        style = ttk.Style()
        style.configure("Transparent.TButton", background="white", relief="flat")

        # Botão para voltar à tela inicial
        ttk.Button(self.button_frame, text="Voltar", command=self.controller.show_usuario_view, style="Transparent.TButton").pack(side="right", padx=5)




