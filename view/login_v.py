# view/login_view.py
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class LoginView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.title("Login")
        self.geometry("400x300")
        
        # Carregar a imagem de fundo
        bg_image = Image.open("midia/Py-Shirts.png")
        self.bg_photo = ImageTk.PhotoImage(bg_image.resize((400, 300)))
        
        # Label para a imagem de fundo
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)
        
        self.create_widgets()

    def create_widgets(self):
        # Widgets para o nome de usuário
        ttk.Label(self, text="E-mail:", background="white").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        # Widgets para a senha
        ttk.Label(self, text="Senha:", background="white").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = ttk.Entry(self, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botão para login
        ttk.Button(self, text="Login", command=self.controller.login).grid(row=2, column=0, columnspan=2, pady=10)

        # Botão para cadastro
        ttk.Button(self, text="Voltar para Cadastro", command=self.show_register_view).grid(row=3, column=0, columnspan=2, pady=5)

    def get_username(self):
        return self.username_entry.get()

    def get_password(self):
        return self.password_entry.get()

    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def show_register_view(self):
        self.destroy()
        self.controller.show_register_view()




