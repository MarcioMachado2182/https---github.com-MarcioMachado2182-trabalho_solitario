import tkinter as tk
from tkinter import ttk

class LoginView(tk.Toplevel):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.title("Login")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Frame para os widgets
        frame = tk.Frame(self)
        frame.pack(pady=10, padx=10, fill='both', expand=True)

        # Label e campo para Email
        tk.Label(frame, text="Email:").grid(row=0, column=0, columnspan=1, padx=5, pady=5)
        self.email_entry = tk.Entry(frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        # Label e campo para Senha
        tk.Label(frame, text="Senha:").grid(row=1, column=0,  columnspan=1, pady=10)
        self.senha_entry = tk.Entry(frame, show='*')
        self.senha_entry.grid(row=1, column=1, padx=5, pady=5)

        # Botão para Submeter
        login_button = tk.Button(frame, text="Login", command=self.login)
        login_button.grid(row=2, column=1,  columnspan=1, pady=10)

        # Botão para Voltar para Cadastro
        back_button = tk.Button(frame, text="Voltar para Cadastro", command=self.show_cadastro)
        back_button.grid(row=3, column=0, columnspan=1, pady=10)

       # Botão para Voltar para Tela Inicial
        back_button = tk.Button(frame, text="Voltar para Tela Inicial", command=self.destroy)
        back_button.grid(row=4, column=0, columnspan=1, pady=10)

    def login(self):
        email = self.email_entry.get()
        senha = self.senha_entry.get()
        # Aqui você pode adicionar lógica de login, se necessário
        print(f"Login attempt with email: {email} and password: {senha}")

    def show_cadastro(self):
        self.destroy()  # Fecha a tela de login
        self.controller.show_cadastro()  # Abre a tela de cadastro

       



