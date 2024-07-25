from model.usuario_m import UsuarioModel
from view.cadastro_v import CadastroView

class CadastroController:
    def __init__(self, root, main_controller):
        self.model = UsuarioModel()
        self.root = root
        self.main_controller = main_controller
        self.register_view = None

    def show_register_view(self):
        self.main_controller.show_register_view()

    def register(self):
        """Cadastra um novo usuário"""
        username = self.register_view.get_username()
        password = self.register_view.get_password()
        if username and password:
            self.model.add_user(username, password)
            self.main_controller.show_login_view()  # Exibe a tela de login após o cadastro
        else:
            self.register_view.show_error("Por favor, preencha todos os campos.")

