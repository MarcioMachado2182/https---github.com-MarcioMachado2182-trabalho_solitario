# controller/login_controller.py
from model.usuario_m import UsuarioModel
from view.login_v import LoginView

class LoginController:
    def __init__(self, root, main_controller):
        self.model = UsuarioModel()
        self.root = root
        self.main_controller = main_controller
        self.login_view = None

    def show_login_view(self):
        if self.login_view is None or not self.login_view.winfo_exists():
            self.login_view = LoginView(self.root, self)
        else:
            self.login_view.deiconify()

    def login(self):
        username = self.login_view.get_username()
        password = self.login_view.get_password()
        if self.model.authenticate(username, password):
            self.login_view.destroy()
            self.main_controller.show_add_produto_view()
        else:
            self.login_view.show_error("Nome de usuário ou senha incorretos.")
