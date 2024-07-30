import tkinter as tk
from tkinter import ttk

class TelaCadastro:
    def __init__(self, root, usuario_v):
        self.root = root
        self.usuario_v = usuario_v  # Referência à tela inicial/usuario_v
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Ajustar a geometria da janela
        self.root.geometry("400x400")

        self.label_nome = ttk.Label(self.root, text="Nome:")
        self.label_nome.place(x=50, y=50, anchor='w')

        self.entry_nome = ttk.Entry(self.root)
        self.entry_nome.place(x=150, y=50, width=200)

        self.label_endereco = ttk.Label(self.root, text="Endereço:")
        self.label_endereco.place(x=50, y=90, anchor='w')

        self.entry_endereco = ttk.Entry(self.root)
        self.entry_endereco.place(x=150, y=90, width=200)

        self.label_email = ttk.Label(self.root, text="Email:")
        self.label_email.place(x=50, y=130, anchor='w')

        self.entry_email = ttk.Entry(self.root)
        self.entry_email.place(x=150, y=130, width=200)

        self.label_senha = ttk.Label(self.root, text="Senha:")
        self.label_senha.place(x=50, y=170, anchor='w')

        self.entry_senha = ttk.Entry(self.root, show='*')
        self.entry_senha.place(x=150, y=170, width=200)

        self.botao_salvar = ttk.Button(self.root, text="Salvar", command=self.salvar)
        self.botao_salvar.place(x=150, y=220, width=100)

        self.botao_voltar = ttk.Button(self.root, text="Voltar para Tela Inicial", command=self.voltar_para_tela_inicial)
        self.botao_voltar.place(x=150, y=260, width=200)

        self.botao_produtos = ttk.Button(self.root, text="Ir para Produtos", command=self.ir_para_produtos)
        self.botao_produtos.place(x=150, y=300, width=200)

    def salvar(self):
        nome = self.entry_nome.get()
        endereco = self.entry_endereco.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        # Implementar lógica de salvar os dados

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




       