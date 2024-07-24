# controller/cadastro_controller.py
from model.usuario_m import UsuarioModel
from view.cadastro_v import CadastroView

class CadastroController:
    def __init__(self, root, main_controller):
        self.model = UsuarioModel()
        self.root = root
        self.main_controller = main_controller
        self.register_view = None

    def show_register_view(self):
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = CadastroView(self.root, self)
        else:
            self.register_view.deiconify()

    def register(self):
        username = self.register_view.get_username()
        password = self.register_view.get_password()
        if username and password:
            self.model.add_user(username, password)
            self.register_view.destroy()
            self.main_controller.show_login_view()
        else:
            self.register_view.show_error("Por favor, preencha todos os campos.")
