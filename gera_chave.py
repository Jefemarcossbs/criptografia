from path import Path
from cryptography.fernet import Fernet

class gera_chave:
    def __init__(self, name_key):
        self.name_key = name_key
    #Método para gerar uma chave 
    def generate_keys(self):
        self.name_key = self.name_key + ".key"
        generated_key = Fernet.generate_key()
        with open(self.name_key, 'wb') as new_key:
            new_key.write(generated_key)
            print(' Chave -> {} gerada com sucesso, guarde a com muito cuidado!!\n'.format(self.name_key))