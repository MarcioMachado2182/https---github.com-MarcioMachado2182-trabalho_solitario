# view/produtos_v.py
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class TelaProdutos:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = ttk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.itens_carrinho = []

        produtos = [
            ("Millenium", 50.00, "midia/milennium_falcon.jpg"),
            ("Cavaleiro Caveira", 60.00, "midia/cavaleiro_caveira.jpg"),
            ("Darth Vader", 60.00, "midia/darth_vader.jpg"),
            ("Mulher Caveira", 60.00, "midia/mulher_caveira.jpg"),
            ("Rei Caveira", 60.00, "midia/rei_caveira.jpg"),
            ("Star Wars", 60.00, "midia/star_wars2.jpg")
        ]

        for i, (nome, preco, imagem) in enumerate(produtos):
            frame = ttk.Frame(self.frame)
            frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")

            try:
                img = Image.open(imagem)
                img = img.resize((150, 150), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Erro ao carregar a imagem {imagem}: {e}")
                img_tk = None

            label_img = ttk.Label(frame, image=img_tk)
            label_img.image = img_tk
            label_img.grid(row=0, column=0, columnspan=2)

            label_nome = ttk.Label(frame, text=nome)
            label_nome.grid(row=1, column=0, columnspan=2)

            label_preco = ttk.Label(frame, text=f"R$ {preco:.2f}")
            label_preco.grid(row=2, column=0, columnspan=2)

            btn_adicionar = ttk.Button(frame, text="Adicionar ao Carrinho", command=lambda n=nome: self.adicionar_ao_carrinho(n))
            btn_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

        frame_botoes = ttk.Frame(self.frame)
        frame_botoes.grid(row=(len(produtos) + 2) // 3, column=0, columnspan=3, pady=20, sticky="s")

        btn_voltar = ttk.Button(frame_botoes, text="Voltar para Tela Inicial", command=self.voltar_para_tela_inicial)
        btn_voltar.pack(side=tk.LEFT, padx=20)

        btn_concluir = ttk.Button(frame_botoes, text="Concluir Pedido", command=self.concluir_pedido)
        btn_concluir.pack(side=tk.RIGHT, padx=20)

    def adicionar_ao_carrinho(self, produto):
        if produto not in self.itens_carrinho:
            self.itens_carrinho.append(produto)
            print(f"{produto} adicionado ao carrinho!")
        else:
            print(f"{produto} já está no carrinho!")

    def voltar_para_tela_inicial(self):
        self.frame.pack_forget()
        from view.login_v import TelaLogin
        TelaLogin(self.root)

    def concluir_pedido(self):
        if not self.itens_carrinho:
            messagebox.showwarning("Aviso", "Você deve adicionar pelo menos um produto ao carrinho antes de concluir o pedido.")
        else:
            print("Pedido concluído!")
            self.frame.pack_forget()
            from view.login_v import TelaLogin
            TelaLogin(self.root)





