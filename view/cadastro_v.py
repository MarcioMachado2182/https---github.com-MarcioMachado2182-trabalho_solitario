# view/tela_cadastro.py
import tkinter as tk
from tkinter import PhotoImage, ttk
from controller.cadastro_c import CadastroController
from view.login_v import TelaLogin
from view.produtos_v import TelaProdutos

class TelaCadastro:
    def __init__(self, parent):
        self.parent = parent  # Referência para a tela inicial

        # Cria uma nova janela (toplevel)
        self.root = tk.Toplevel()
        self.root.title("Tela de Cadastro")

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

        # Criar e posicionar widgets da tela de cadastro
        self.label_nome = ttk.Label(self.root, text="Nome:")
        self.label_nome.place(x=50, y=100, anchor='w')

        self.entry_nome = ttk.Entry(self.root)
        self.entry_nome.place(x=150, y=100, width=200)

        self.label_endereco = ttk.Label(self.root, text="Endereço:")
        self.label_endereco.place(x=50, y=140, anchor='w')

        self.entry_endereco = ttk.Entry(self.root)
        self.entry_endereco.place(x=150, y=140, width=200)

        self.label_email = ttk.Label(self.root, text="Email:")
        self.label_email.place(x=50, y=180, anchor='w')

        self.entry_email = ttk.Entry(self.root)
        self.entry_email.place(x=150, y=180, width=200)

        self.label_senha = ttk.Label(self.root, text="Senha:")
        self.label_senha.place(x=50, y=220, anchor='w')

        self.entry_senha = ttk.Entry(self.root, show='*')
        self.entry_senha.place(x=150, y=220, width=200)

        self.botao_salvar = ttk.Button(self.root, text="Salvar", command=self.salvar)
        self.botao_salvar.place(x=self.bg_width // 2 - 50, y=self.bg_height - 120)

        self.botao_login = ttk.Button(self.root, text="Ir para Login", command=self.ir_para_login)
        self.botao_login.place(x=self.bg_width // 2 - 75, y=self.bg_height - 80, width=150, height=30)

        self.botao_produtos = ttk.Button(self.root, text="Ir para Produtos", command=self.ir_para_produtos)
        self.botao_produtos.place(x=self.bg_width // 2 - 75, y=self.bg_height - 40, width=150, height=30)

    def salvar(self):
        nome = self.entry_nome.get()
        endereco = self.entry_endereco.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        
        # Aqui você pode adicionar a lógica para salvar os dados
        print(f"Nome: {nome}")
        print(f"Endereço: {endereco}")
        print(f"Email: {email}")
        print(f"Senha: {senha}")

    def ir_para_login(self):
        self.root.destroy()  # Fechar a tela de cadastro
        TelaLogin(self.parent)  # Abrir a tela de login

    # view/cadastro_v.py
    def ir_para_produtos(self):
        self.root.withdraw()
        from view.produtos_v import TelaProdutos
        from controller.produtos_c import ProdutosController
        controller = ProdutosController(self)
        self.produtos_window = tk.Toplevel(self.root)
        TelaProdutos(self.produtos_window, controller)


       