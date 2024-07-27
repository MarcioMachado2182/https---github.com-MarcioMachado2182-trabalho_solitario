try:
    from controller.usuario_c import UsuarioController
    print("Importação bem-sucedida!")
except ImportError as e:
    print(f"Erro de importação: {e}")
