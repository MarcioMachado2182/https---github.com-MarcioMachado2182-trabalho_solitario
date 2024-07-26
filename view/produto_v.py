import tkinter as tk

class ProdutoView(tk.Toplevel):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.controller = controller
        self.title("Produtos")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Criação dos widgets para ProdutoView
        tk.Label(self, text="Produtos").pack()
        tk.Button(self, text="Voltar", command=self.destroy).pack()






