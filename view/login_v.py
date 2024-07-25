import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from controller.banco_c import BancoController


class LoginView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = BancoController()
        self.title("Login")
        self.geometry("800x600")

        # Carregar a imagem de fundo
        try:
            bg_image = Image.open("midia/Feeling.png")
            self.bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
            self.bg_label = tk.Label(self, image=self.bg_photo)
            self.bg_label.place(relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Arquivo de imagem não encontrado.")
            messagebox.showerror("Erro", "Arquivo de imagem não encontrado.")
            self.bg_photo = None
        except Exception as e:
            print(f"Erro ao carregar a imagem: {e}")
            messagebox.showerror("Erro", f"Erro ao carregar a imagem: {e}")
            self.bg_photo = None

        self.create_widgets()

    def create_widgets(self):
        """Cria os widgets da tela de login"""
        self.form_frame = tk.Frame(self, bg='white', padx=20, pady=20)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(self.form_frame, text="E-mail:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self.form_frame)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.form_frame, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.form_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Button(self.form_frame, text="Login", command=self.login_user).grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(self.form_frame, text="Cadastrar", command=self.show_cadastro_view).grid(row=3, column=0, columnspan=2, pady=5)

    def login_user(self):
        """Verifica as credenciais do usuário no banco de dados"""
        email = self.email_entry.get()
        senha = self.password_entry.get()

        if not (email and senha):
            messagebox.showwarning("Aviso", "E-mail e senha são obrigatórios.")
            return

        if self.db.validate_user(email, senha):
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            self.show_main_view()
        else:
            messagebox.showerror("Erro", "E-mail ou senha incorretos.")

    def show_cadastro_view(self):
        """Destroi a tela de login e mostra a tela de cadastro"""
        self.destroy()
        self.controller.show_cadastro_view()

    def show_main_view(self):
        """Método fictício para mostrar a tela principal após login"""
        print("Tela principal")  # Substitua por uma chamada para abrir a tela principal

    def close(self):
        """Fecha a conexão com o banco de dados"""
        self.db.close()







