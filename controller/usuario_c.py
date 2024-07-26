from view.cadastro_v import CadastroView
from view.login_v import LoginView
from view.produto_v import ProdutoView
import tkinter as tk

class UsuarioController:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def show_view(self, view_class):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self.root, self)

    def show_cadastro(self):
        self.show_view(CadastroView)

    def show_login(self):
        self.show_view(LoginView)

    def show_produtos(self):
        self.show_view(ProdutoView)

    def show_initial_screen(self):
        self.show_view(MainApplication)

    def register_user(self, nome, endereco, email, senha):
        from model.usuario_m import UsuarioModel
        model = UsuarioModel()
        if model.register_user(nome, endereco, email, senha):
            self.show_message("Cadastro realizado com sucesso!")
        else:
            self.show_message("Erro ao realizar o cadastro.")

    def show_message(self, message):
        from tkinter import messagebox
        messagebox.showinfo("Informação", message)






