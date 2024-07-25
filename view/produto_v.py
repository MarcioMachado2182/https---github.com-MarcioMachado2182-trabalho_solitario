import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ProdutoView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configuração da janela de produtos
        self.title("Produtos")
        self.geometry("800x600")

        # Carregar a imagem de fundo
        bg_image = Image.open("midia/Py-Shirts.png")
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

        # Botões para navegar entre as telas
        self.produtos_button = ttk.Button(self.button_frame, text="Produtos", command=self.controller.show_produto_view, style="Transparent.TButton")
        self.produtos_button.pack(side="right", padx=5)
        self.login_button = ttk.Button(self.button_frame, text="Login", command=self.controller.show_login_view, style="Transparent.TButton")
        self.login_button.pack(side="right", padx=5)
        self.register_button = ttk.Button(self.button_frame, text="Cadastro", command=self.controller.show_register_view, style="Transparent.TButton")
        self.register_button.pack(side="right", padx=5)

        # Botão para voltar à tela inicial
        self.back_button = ttk.Button(self.button_frame, text="Voltar à Tela Inicial", command=self.controller.show_usuario_view, style="Transparent.TButton")
        self.back_button.pack(side="right", padx=5)

        # Lista de produtos (exemplo)
        self.produtos_list = tk.Listbox(self)
        self.produtos_list.pack(pady=10, fill='both', expand=True)

        # Adicionar alguns produtos de exemplo
        self.produtos_list.insert(tk.END, "Produto 1")
        self.produtos_list.insert(tk.END, "Produto 2")
        self.produtos_list.insert(tk.END, "Produto 3")
