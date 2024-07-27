import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk
from view.produtos_v import TelaProdutos  # Importar apenas quando necessário

class TelaCarrinho:
    def __init__(self, parent):
        self.parent = parent  # Referência para a tela anterior

        # Cria uma nova janela (toplevel)
        self.root = tk.Toplevel()
        self.root.title("Tela do Carrinho")

        # Carregar imagem de fundo
        self.bg_image = PhotoImage(file="midia/Feeling.png")
        self.bg_width = self.bg_image.width()
        self.bg_height = self.bg_image.height()

        # Definir tamanho da janela para o tamanho da imagem
        self.root.geometry(f"{self.bg_width}x{self.bg_height}")
        self.root.resizable(False, False)

        # Configurar o fundo da janela
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Adicionar widgets à tela do carrinho
        self.label_carrinho = ttk.Label(self.root, text="Carrinho de Compras")
        self.label_carrinho.place(x=self.bg_width // 2 - 75, y=self.bg_height // 2 - 100)

        self.botao_concluir = ttk.Button(self.root, text="Concluir Pedido", command=self.concluir_pedido)
        self.botao_concluir.place(x=self.bg_width // 2 - 75, y=self.bg_height - 80, width=150, height=30)

        self.botao_voltar = ttk.Button(self.root, text="Voltar para Produtos", command=self.voltar_para_produtos)
        self.botao_voltar.place(x=self.bg_width // 2 - 75, y=self.bg_height - 40, width=150, height=30)

    def concluir_pedido(self):
        # Lógica para concluir o pedido
        print("Pedido concluído")
        self.root.destroy()
        self.parent.deiconify()

    def voltar_para_produtos(self):
        self.root.destroy()
        TelaProdutos(self.parent)  # Crie a tela de produtos aqui

