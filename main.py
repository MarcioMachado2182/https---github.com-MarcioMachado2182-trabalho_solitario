# main.py
import tkinter as tk
from controller.usuario_c import UsuarioController
from view.usuariomain_v import MainApplication

def main():
    root = tk.Tk()  # Cria a instância raiz
    root.withdraw()  # Esconde a janela principal para evitar que apareça
    controller = UsuarioController(root)  # Cria o controlador
    app = MainApplication(root, controller)  # Cria a aplicação principal
    app.deiconify()  # Mostra a janela principal
    app.mainloop()  # Inicia o loop principal da aplicação

if __name__ == "__main__":
    main()

