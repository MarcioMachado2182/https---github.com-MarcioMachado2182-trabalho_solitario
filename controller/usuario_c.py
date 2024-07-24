# controller.py
from model.usuario_m import UsuarioModel
from view.login_v import LoginView
from view.cadastro_v import CadastroView
from view.usuario_v import UsuarioView

class UsuarioController:
    def __init__(self, root):
        self.model = UsuarioModel()
        self.root = root
        self.usuario_view = UsuarioView(root, self)
        self.login_view = None
        self.register_view = None

    def show_login_view(self):
        if self.login_view is None or not self.login_view.winfo_exists():
            self.login_view = LoginView(self.root, self)
        else:
            self.login_view.deiconify()

    def show_register_view(self):
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = CadastroView(self.root, self)
        else:
            self.register_view.deiconify()

    def login(self):
        username = self.login_view.get_username()
        password = self.login_view.get_password()
        if self.model.authenticate(username, password):
            print(f"Usuário {username} logado com sucesso!")
        else:
            self.login_view.show_error("Nome de usuário ou senha incorretos.")

    def register(self):
        username = self.register_view.username_entry.get()
        password = self.register_view.password_entry.get()
        if username and password:
            self.model.add_user(username, password)
            print(f"Usuário {username} cadastrado com sucesso!")
            self.register_view.destroy()
        else:
            self.register_view.show_error("Por favor, preencha todos os campos.")


    