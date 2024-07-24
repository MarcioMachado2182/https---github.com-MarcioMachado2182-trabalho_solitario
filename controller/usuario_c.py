


class UsuarioController:
    def __init__(self, root):
        self.model = UsuarioModel()
        self.root = root
        self.usuario_view = None
        self.login_view = None
        self.register_view = None

    def hide_other_views(self, view_to_show):
        # Oculta a tela de login se estiver aberta
        if self.login_view and self.login_view.winfo_exists() and self.login_view != view_to_show:
            self.login_view.withdraw()

        # Oculta a tela de cadastro se estiver aberta
        if self.register_view and self.register_view.winfo_exists() and self.register_view != view_to_show:
            self.register_view.withdraw()

        # Oculta a tela do usuário se estiver aberta
        if self.usuario_view and self.usuario_view.winfo_exists() and self.usuario_view != view_to_show:
            self.usuario_view.withdraw()

    def show_login_view(self):
        self.hide_other_views(self.login_view)

        if self.login_view is None or not self.login_view.winfo_exists():
            self.login_view = LoginView(self.root, self)
        else:
            self.login_view.deiconify()

    def show_register_view(self):
        self.hide_other_views(self.register_view)

        if self.register_view is None or not self.register_view.winfo_exists():
            self.register_view = CadastroView(self.root, self)
        else:
            self.register_view.deiconify()

    def show_usuario_view(self):
        self.hide_other_views(self.usuario_view)

        if self.usuario_view is None or not self.usuario_view.winfo_exists():
            self.usuario_view = UsuarioView(self.root, self)
        else:
            self.usuario_view.deiconify()

    # Restante do seu código...



    