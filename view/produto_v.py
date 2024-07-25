import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from controller.banco_c import BancoController

class ProdutoView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.db = BancoController()
        self.title("Produtos")
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
        """Cria os widgets da tela de produtos"""
        self.form_frame = tk.Frame(self, bg='white', padx=20, pady=20)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Adicione widgets para mostrar produtos, adicionar produtos, etc.
        ttk.Label(self.form_frame, text="Produtos").grid(row=0, column=0, padx=10, pady=5)

        # Exemplo: botão para adicionar um produto
        ttk.Button(self.form_frame, text="Adicionar Produto", command=self.add_product).grid(row=1, column=0, padx=10, pady=5)

    def add_product(self):
        """Método fictício para adicionar um produto"""
        print("Adicionar produto")  # Substitua por uma lógica real para adicionar produtos

    def close(self):
        """Fecha a conexão com o banco de dados"""
        self.db.close()


