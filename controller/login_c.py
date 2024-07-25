from model.usuario_m import UsuarioModel
from view.login_v import LoginView

class LoginController:
    def __init__(self, root, main_controller):
        self.model = UsuarioModel()
        self.root = root
        self.main_controller = main_controller
        self.login_view = None

    def show_login_view(self):
        self.main_controller.show_login_view()

    def login(self):
        """Realiza o login do usuário"""
        username = self.login_view.get_username()
        password = self.login_view.get_password()
        if self.model.authenticate(username, password):
            self.main_controller.show_usuario_view()  # Exibe a tela do usuário após login bem-sucedido
        else:
            self.login_view.show_error("Nome de usuário ou senha incorretos.")
