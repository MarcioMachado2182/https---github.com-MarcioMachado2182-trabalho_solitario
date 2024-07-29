import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from view.usuario_v import TelaInicial

if __name__ == "__main__":
    app = TelaInicial()
    app.run()


