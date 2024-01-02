import tkinter as tk
from tkinter import filedialog as fd
import os
from gera_chave import gera_chave


def main():
    # Create a Tkinter window
    window = tk.Tk()

    # Set the window title
    window.title('Criptografar')

    # Set the window size
    window.geometry('400x300')
    lb_gerar_chave = tk.Label(window, text="Clique para gerar a chave",padx=10,pady=10).grid(row=0,column=0)
    btn_generate_key = tk.Button(window, text='Gerar', padx=10,command=on_click_btn_generate_key).grid(row=0,column=1)

    
    lb_entrada = tk.Label(window, text="Selecione o arquivo para criptografar",padx=10,pady=10).grid(row=1,column=0)
    btn_open_file = tk.Button(window, text='Abrir arquivo', padx=10,command=on_click_btn_open_file).grid(row=1,column=1)
    

    # Start the main event loop
    window.mainloop()

def on_click_btn_generate_key():
    generate = gera_chave('Jeferson')
    generate.generate_keys()

def on_click_btn_open_file():
    filename = fd.askopenfilename(title='Selecione o arquivo para criptografar')
    if os.path.isfile(filename):
        print("ok")
    else:
        print('Sem arquivo ')

if __name__ == '__main__':
    main()