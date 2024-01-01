from cryptography.fernet import Fernet
class open_key:
    def open_key(name_key):
        try:
            with open(name_key, 'rb') as load_key:
                key = Fernet(load_key.read())
                return key
        except FileNotFoundError as erro_chave:
            print(erro_chave)