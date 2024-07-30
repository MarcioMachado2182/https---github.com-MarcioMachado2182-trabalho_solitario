import tkinter as tk
from tkinter import ttk

class TelaLogin:
    def __init__(self, root, usuario_v):
        self.root = root
        self.usuario_v = usuario_v  # Referência à tela inicial/usuario_v
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Conteúdo da tela de login aqui...

        self.botao_voltar = ttk.Button(self.frame, text="Voltar para Tela Inicial", command=self.voltar_para_tela_inicial)
        self.botao_voltar.pack()

        self.botao_produtos = ttk.Button(self.frame, text="Ir para Produtos", command=self.ir_para_produtos)
        self.botao_produtos.pack()

    def voltar_para_tela_inicial(self):
        self.root.destroy()
        self.usuario_v.root.deiconify()

    def ir_para_produtos(self):
        self.root.withdraw()
        from view.produtos_v import TelaProdutos
        from controller.produtos_c import ProdutosController
        controller = ProdutosController(self.usuario_v)
        self.produtos_window = tk.Toplevel(self.root)
        TelaProdutos(self.produtos_window, controller, self.usuario_v)

# As demais partes da tela de login seguem aqui...








       



