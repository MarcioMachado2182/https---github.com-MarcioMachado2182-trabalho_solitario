# main.py
import tkinter as tk
from controller.usuario_c import UsuarioController

def main():
    root = tk.Tk()
    app = UsuarioController(root)
    root.mainloop()

if __name__ == "__main__":
    main()

