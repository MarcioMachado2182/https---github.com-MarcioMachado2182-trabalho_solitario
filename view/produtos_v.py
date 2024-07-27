import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def adicionar_ao_carrinho(produto):
    print(f"{produto} adicionado ao carrinho!")

def criar_janela():
    janela = tk.Tk()
    janela.title("Tela de Produtos")

    # Ajustar o tamanho da janela
    janela.geometry("800x600")

    janela.columnconfigure(0, weight=1)
    janela.columnconfigure(1, weight=1)
    janela.columnconfigure(2, weight=1)

    # Lista de produtos (corrigida para usar caminhos de imagem como strings)
    produtos = [
        ("Millenium", 50.00, "midia/milennium_falcon.jpg"),
        ("Caveira Rosa", 60.00, "midia/cavaleiro_caveira.jpg"),
        ("Caveira Rosa", 60.00, "midia/darth_vader.jpg"),
        ("Caveira Rosa", 60.00, "midia/mulher_caveira.jpg"),
        ("Caveira Rosa", 60.00, "midia/rei_caveira.jpg"),
        ("Caveira Rosa", 60.00, "midia/star_wars2.jpg")
    ]

    for i, (nome, preco, imagem) in enumerate(produtos):
        frame = ttk.Frame(janela)
        frame.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")

        try:
            # Abrir a imagem
            img = Image.open(imagem)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Erro ao carregar a imagem {imagem}: {e}")
            img_tk = None

        # Criar o label para a imagem
        label_img = ttk.Label(frame, image=img_tk)
        label_img.image = img_tk  # Manter uma referência à imagem para evitar que seja coletada como lixo
        label_img.grid(row=0, column=0, columnspan=2)

        # Criar labels para o nome e preço do produto
        label_nome = ttk.Label(frame, text=nome)
        label_nome.grid(row=1, column=0, columnspan=2)

        label_preco = ttk.Label(frame, text=f"R$ {preco:.2f}")
        label_preco.grid(row=2, column=0, columnspan=2)

        # Botão para adicionar ao carrinho
        btn_adicionar = ttk.Button(frame, text="Adicionar ao Carrinho", command=lambda n=nome: adicionar_ao_carrinho(n))
        btn_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

    janela.mainloop()

criar_janela()



