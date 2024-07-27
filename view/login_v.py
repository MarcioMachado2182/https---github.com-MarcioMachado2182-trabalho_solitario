import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from controller.login_c import LoginController
from view.cadastro_v import TelaCadastro
from view.produtos_v import TelaProdutos

class TelaLogin:
    def __init__(self, parent):
        self.parent = parent  # Referência para a tela inicial

        # Cria uma nova janela (toplevel)
        self.root = tk.Toplevel()
        self.root.title("Tela de Login")

        # Carregar imagem de fundo
        self.bg_image = PhotoImage(file="midia/Feeling.png")  # Use uma imagem adequada para a tela de login
        self.bg_width = self.bg_image.width()
        self.bg_height = self.bg_image.height()

        # Definir tamanho da janela para o tamanho da imagem
        self.root.geometry(f"{self.bg_width}x{self.bg_height}")
        self.root.resizable(False, False)  # Não permitir redimensionamento da janela

        # Configurar o fundo da janela
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Criar e posicionar widgets da tela de login
        self.label_email = ttk.Label(self.root, text="Email:")
        self.label_email.place(x=50, y=100, anchor='w')

        self.entry_email = ttk.Entry(self.root)
        self.entry_email.place(x=150, y=100, width=200)

        self.label_senha = ttk.Label(self.root, text="Senha:")
        self.label_senha.place(x=50, y=140, anchor='w')

        self.entry_senha = ttk.Entry(self.root, show='*')
        self.entry_senha.place(x=150, y=140, width=200)

        self.botao_login = ttk.Button(self.root, text="Login", command=self.login)
        self.botao_login.place(x=self.bg_width // 2 - 50, y=self.bg_height - 120)

        self.botao_cadastro = ttk.Button(self.root, text="Ir para Cadastro", command=self.ir_para_cadastro)
        self.botao_cadastro.place(x=self.bg_width // 2 - 75, y=self.bg_height - 80, width=150, height=30)

        self.botao_produtos = ttk.Button(self.root, text="Ir para Produtos", command=self.ir_para_produtos)
        self.botao_produtos.place(x=self.bg_width // 2 - 75, y=self.bg_height - 40, width=150, height=30)

        # Inicializar o controlador
        self.controller = LoginController(self)

    def login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        self.controller.login(email, senha)  # Usa o controlador para autenticar o usuário

        # Fechar a tela de login
        self.root.destroy()
        
        # Reexibir a tela inicial
        self.parent.deiconify()

    def ir_para_cadastro(self):
        # Fechar a tela de login
        self.root.destroy()
        
        # Recriar e exibir a tela de cadastro
        TelaCadastro(self.parent)

    def ir_para_produtos(self):
        # Fechar a tela de login
        self.root.destroy()
        
        # Recriar e exibir a tela de produtos
        TelaProdutos(self.parent)








       



