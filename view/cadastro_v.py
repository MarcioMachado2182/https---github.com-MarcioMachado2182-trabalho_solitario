import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from controller.banco_c import BancoController

class CadastroView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = BancoController()
        self.title("Cadastro")
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
        """Cria os widgets da tela de cadastro"""
        self.form_frame = tk.Frame(self, bg='white', padx=20, pady=20)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        ttk.Label(self.form_frame, text="Nome Completo:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = ttk.Entry(self.form_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.form_frame, text="Endereço:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.endereco_entry = ttk.Entry(self.form_frame)
        self.endereco_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.form_frame, text="E-mail:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(self.form_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.form_frame, text="Senha:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = ttk.Entry(self.form_frame, show='*')
        self.password_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Button(self.form_frame, text="Cadastrar", command=self.register_user).grid(row=4, column=0, columnspan=2, pady=10)

        ttk.Button(self.form_frame, text="Voltar para Login", command=self.show_login_view).grid(row=5, column=0, columnspan=2, pady=5)

    def register_user(self):
        """Registra um novo usuário no banco de dados"""
        nome = self.username_entry.get()
        endereco = self.endereco_entry.get()
        email = self.email_entry.get()
        senha = self.password_entry.get()

        if not (nome and endereco and email and senha):
            messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
            return

        if self.db.register_user(nome, endereco, email, senha):
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.show_login_view()
        else:
            messagebox.showerror("Erro", "E-mail já cadastrado ou erro ao registrar o usuário.")

    def show_login_view(self):
        """Destroi a tela de cadastro e mostra a tela de login"""
        self.destroy()
        self.controller.show_login_view()

    def close(self):
        """Fecha a conexão com o banco de dados"""
        self.db.close()
