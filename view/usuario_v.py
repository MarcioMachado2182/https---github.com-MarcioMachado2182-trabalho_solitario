import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from controller.usuario_c import UsuarioController
from view.login_v import TelaLogin
from view.cadastro_v import TelaCadastro

class TelaInicial:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tela Inicial")

        # Carregar imagem de fundo
        self.bg_image = PhotoImage(file="midia/Feeling.png")
        self.bg_width = self.bg_image.width()
        self.bg_height = self.bg_image.height()

        # Definir tamanho da janela para o tamanho da imagem
        self.root.geometry(f"{self.bg_width}x{self.bg_height}")
        self.root.resizable(False, False)  # Não permitir redimensionamento da janela

        # Configurar o fundo da janela
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Criar e posicionar botões com ttk
        self.botao_cadastro = ttk.Button(self.root, text="Ir para Cadastro", command=self.ir_para_cadastro)
        self.botao_cadastro.place(x=self.bg_width // 2 - 75, y=self.bg_height - 120, width=150, height=30)

        self.botao_login = ttk.Button(self.root, text="Ir para Login", command=self.ir_para_login)
        self.botao_login.place(x=self.bg_width // 2 - 75, y=self.bg_height - 80, width=150, height=30)

        self.botao_produtos = ttk.Button(self.root, text="Ir para Produtos", command=self.ir_para_produtos)
        self.botao_produtos.place(x=self.bg_width // 2 - 75, y=self.bg_height - 40, width=150, height=30)

        # Inicializar o controlador
        self.controller = UsuarioController(self)

    def ir_para_cadastro(self):
        # Ocultar a tela inicial
        self.root.withdraw()
        
        # Cria uma nova instância da tela de cadastro
        from view.cadastro_v import TelaCadastro
        TelaCadastro(self.root)

    def ir_para_login(self):
        # Ocultar a tela inicial
        self.root.withdraw()
        
        # Cria uma nova instância da tela de login
        TelaLogin(self.root)

    def ir_para_produtos(self):
        # Ocultar a tela inicial
        self.root.withdraw()
        
        # Cria uma nova instância da tela de produtos
        from view.produtos_v import TelaProdutos
        TelaProdutos(self.root)

    def run(self):
        self.root.mainloop()














