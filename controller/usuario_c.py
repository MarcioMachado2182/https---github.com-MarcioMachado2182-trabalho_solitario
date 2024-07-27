# controller/usuario_c.py
from view.login_v import TelaLogin
from view.cadastro_v import TelaCadastro
from view.produtos_v import TelaProdutos
from tkinter import messagebox

class UsuarioController:
    def __init__(self, root):
        self.root = root
        self.tela_inicial = None
        self.tela_cadastro = None
        self.tela_produtos = None
        self.tela_login = None

    def set_tela_inicial(self, tela_inicial):
        self.tela_inicial = tela_inicial

    def ir_para_login(self):
        self.tela_inicial.withdraw()
        if self.tela_login is None:
            self.tela_login = TelaLogin(self.tela_inicial, self)
        self.tela_login.deiconify()

    def ir_para_cadastro(self):
        self.tela_inicial.withdraw()
        if self.tela_cadastro is None:
            self.tela_cadastro = TelaCadastro(self.tela_inicial, self)
        self.tela_cadastro.deiconify()

    def ir_para_produtos(self):
        if self.tela_produtos is None:
            self.tela_produtos = TelaProdutos(self.tela_inicial, self)
        self.tela_produtos.deiconify()
        if self.tela_cadastro:
            self.tela_cadastro.withdraw()
        if self.tela_login:
            self.tela_login.withdraw()

    def voltar_para_tela_inicial(self):
        if self.tela_cadastro:
            self.tela_cadastro.withdraw()
        if self.tela_produtos:
            self.tela_produtos.withdraw()
        if self.tela_login:
            self.tela_login.withdraw()
        self.tela_inicial.deiconify()

    def cadastrar_usuario(self, nome, endereco, email, senha):
        if inserir_usuario(nome, endereco, email, senha):
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso")
            self.ir_para_produtos()
        else:
            messagebox.showerror("Erro", "Erro ao realizar cadastro")

    def buscar_produtos(self):
        return buscar_produtos()

    def cadastrar_produto(self, nome, valor, caminho_imagem):
        if inserir_produto(nome, valor, caminho_imagem):
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso")
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar produto")






