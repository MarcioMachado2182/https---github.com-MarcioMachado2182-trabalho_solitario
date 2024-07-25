from model.usuario_m import UsuarioModel
from view.login_v import LoginView
from view.cadastro_v import CadastroView
from view.produto_v import ProdutoView
from view.usuario_v import UsuarioView

class UsuarioController:
    def __init__(self, root):
        self.model = UsuarioModel()
        self.root = root
        self.root.title("Tela Inicial")
        self.root.geometry("800x600")

        self.usuario_view = UsuarioView(self.root, self)
        self.usuario_view.pack(fill="both", expand=True)
        
        self.login_view = None
        self.register_view = None
        self.produto_view = None

    def hide_other_views(self, view_to_show):
        """Esconde outras janelas, exceto a que deve ser exibida"""
        if self.login_view and self.login_view != view_to_show:
            self.login_view.withdraw()
        if self.register_view and self.register_view != view_to_show:
            self.register_view.withdraw()
        if self.produto_view and self.produto_view != view_to_show:
            self.produto_view.withdraw()

    def show_login_view(self):
        """Exibe a tela de login"""
        self.hide_other_views(self.login_view)
        if self.login_view is None or not self.login_view.winfo_exists():
            self.login_view = LoginView(self.root, self)
        else:
            self.login_view.deiconify()

    def show_register_view(self):
        """Exibe a tela de cadastro"""
        self.hide_other_views(self.register_view)
        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = CadastroView(self.root, self)
        else:
            self.register_view.deiconify()

    def show_produto_view(self):
        """Exibe a tela de produtos"""
        self.hide_other_views(self.produto_view)
        if self.produto_view is None or not self.produto_view.winfo_exists():
            self.produto_view = ProdutoView(self.root, self)
        else:
            self.produto_view.deiconify()

    def login(self):
        """Método para login do usuário"""
        username = self.login_view.get_username()
        password = self.login_view.get_password()
        if self.model.authenticate(username, password):
            self.login_view.destroy()
            self.show_usuario_view()
        else:
            self.login_view.show_error("Nome de usuário ou senha incorretos.")

    def register(self):
        """Método para registro do usuário"""
        username = self.register_view.get_username()
        password = self.register_view.get_password()
        if username and password:
            self.model.add_user(username, password)
            self.register_view.destroy()
            self.show_login_view()
        else:
            self.register_view.show_error("Por favor, preencha todos os campos.")