# model.py
# model.py
class UsuarioModel:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        self.users.append({'username': username, 'password': password})

    def authenticate(self, username, password):
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False
