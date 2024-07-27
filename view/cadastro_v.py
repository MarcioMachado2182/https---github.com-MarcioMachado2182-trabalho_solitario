import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from controller.cadastro_c import CadastroController

class TelaCadastro:
    def __init__(self, parent):
        self.parent = parent  # Referência para a tela inicial

        # Cria uma nova janela (toplevel)
        self.root = tk.Toplevel()
        self.root.title("Tela de Cadastro")

        # Carregar imagem de fundo
        self.bg_image = PhotoImage(file="midia/Feeling.png")  # Use uma imagem adequada para a tela de cadastro
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

        # Inicializar o controlador
        self.controller = CadastroController(self)

    def salvar(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        endereco = self.entry_endereco.get()
        print(f"Nome: {nome},  Endereço: {endereco}, Email: {email}, Senha: {senha}")

        # Lógica para salvar os dados do cadastro
        # ...

        # Fechar a tela de cadastro
        self.root.destroy()
        
        # Reexibir a tela inicial
        self.parent.deiconify()

    def ir_para_login(self):
        # Fechar a tela de cadastro
        self.root.destroy()
        
        # Recriar e exibir a tela de login
        from view.login_v import TelaLogin
        TelaLogin(self.parent)

    def ir_para_produtos(self):
        # Fechar a tela de cadastro
        self.root.destroy()
        
        # Recriar e exibir a tela de produtos
        from view.produtos_v import TelaProdutos
        TelaProdutos(self.parent)









