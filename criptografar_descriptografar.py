import abre_chave as encriptacao
import os
from cryptography.fernet import Fernet
class encript_decript:
    def encrypt_files(diretorio, nome_chave):
        diretorio_to_encrypt = diretorio
        print(diretorio_to_encrypt)
        loaded_key = encriptacao.open_key(nome_chave)
        try:
            os.chdir(diretorio)
            with os.scandir(diretorio_to_encrypt) as arquivos:
                for lista_arquivos in arquivos:
                    arquivo = os.Path(lista_arquivos.name)
                    if arquivo.isfile() == True:
                        with open(arquivo.name, "rb") as file:
                            file_data = file.read()
                            encrypt_data = loaded_key.encrypt(file_data)
                            with open(arquivo.name, "wb") as encritp_file:
                                print(arquivo.name)
                                encritp_file.write(encrypt_data)
                    else:
                        print('Nenhum arquivo encontrado!!')            
        except FileNotFoundError as erro_encriptar:
            print(erro_encriptar)          

    def decrypt_files(diretorio, nome_chave):
        loaded_key = encriptacao.open_key(nome_chave)
        diretorio_to_dencrypt = os.chdir(diretorio)
        with os.scandir(diretorio_to_dencrypt) as arquivos:
            for lista_arquivos in arquivos:
                arquivo = os.Path(lista_arquivos.name)
                if arquivo.isfile() == True:
                    try:
                        with open(arquivo.name, "rb") as file:
                            file_data = file.read()
                            decript_data = loaded_key.decrypt(file_data)
                            with open(arquivo.name, "wb") as decritp_file:
                                print(arquivo.name)
                                decritp_file.write(decript_data)
                    except  Fernet.InvalidToken as erro_chave:
                        print('Chave criptografica incompativel {}'.format(erro_chave))            