import tkinter as tk
from tkinter import ttk

class CadastroView(tk.Toplevel):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.title("Cadastro")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Frame para os widgets
        frame = tk.Frame(self)
        frame.pack(pady=10, padx=10, fill='both', expand=True)

        # Label e campo para Nome
        tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.nome_entry = tk.Entry(frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label e campo para Endereço
        tk.Label(frame, text="Endereço:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.endereco_entry = tk.Entry(frame)
        self.endereco_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label e campo para Email
        tk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        # Label e campo para Senha
        tk.Label(frame, text="Senha:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.senha_entry = tk.Entry(frame, show='*')
        self.senha_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botão para Submeter
        submit_button = tk.Button(frame, text="Cadastrar", command=self.cadastrar)
        submit_button.grid(row=4, column=0, pady=10, sticky='e')

        # Botão para Voltar para Tela Inicial
        back_button = tk.Button(frame, text="Voltar para Tela Inicial", command=self.destroy)
        back_button.grid(row=0, column=2, pady=10, sticky='w')

        # Botão para Voltar para Login
        login_button = tk.Button(frame, text="Voltar para Login", command=self.show_login)
        login_button.grid(row=1, column=2, columnspan=2, pady=10)

    def cadastrar(self):
        nome = self.nome_entry.get()
        endereco = self.endereco_entry.get()
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        self.controller.register_user(nome, endereco, email, senha)

    def show_login(self):
        self.destroy()  # Fecha a tela de cadastro
        self.controller.show_login()  # Abre a tela de login






