import os
from path import Path
from cryptography.fernet import Fernet
class gera_chave:
    #Método para gerar uma chave 
    def generate_keys(name_key):
        name_key = name_key + ".key"
        generated_key = Fernet.generate_key()
        with open(name_key, 'wb') as new_key:
            new_key.write(generated_key)
            print(' Chave -> {} gerada com sucesso, guarde a com muito cuidado!!\n'.format(name_key))