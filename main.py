# main.py

import tkinter as tk
from controller.usuario_c import UsuarioController

def main():
    root = tk.Tk()
    app = UsuarioController(root)
    app.show_usuario_view()  # Exibe a tela inicial ao iniciar o aplicativo
    root.mainloop()

if __name__ == "__main__":
    main()

