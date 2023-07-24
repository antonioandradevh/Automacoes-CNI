import os
import sys
import tkinter as tk
from tkinter import filedialog
from unidecode import unidecode

def rename_files_and_folders(directory):
    try:
        while True:
            renamed = False
            for root, dirs, files in os.walk(directory):
                for filename in files:
                    path = os.path.join(root, filename)
                    new_filename = unidecode(filename)
                    if ' ' in new_filename:
                        new_filename = new_filename.replace(' ', '_')
                    new_path = os.path.join(root, new_filename)
                    if new_filename != filename:
                        try:
                            os.rename(path, new_path)
                            print(f"Arquivo renomeado: {filename} -> {new_filename}")
                            renamed = True
                        except PermissionError as e:
                            print(f"Erro de permissão: {e}")
            
                for foldername in dirs:
                    path = os.path.join(root, foldername)
                    new_foldername = unidecode(foldername)
                    if ' ' in new_foldername:
                        new_foldername = new_foldername.replace(' ', '_')
                    new_path = os.path.join(root, new_foldername)
                    if new_foldername != foldername:
                        try:
                            os.rename(path, new_path)
                            print(f"Pasta renomeada: {foldername} -> {new_foldername}")
                            renamed = True
                        except PermissionError as e:
                            print(f"Erro de permissão: {e}")

            if not renamed:
                break
    except Exception as e:
        print(f"Erro ao renomear arquivos e pastas: {e}")

def select_directory():
    diretorio = filedialog.askdirectory()
    if diretorio:
        rename_files_and_folders(diretorio)


def select_directory():
    diretorio = filedialog.askdirectory()
    if diretorio:
        selected_directory_label.config(text="Diretório selecionado: " + diretorio)
        rename_files_and_folders(diretorio)
# Criação da janela principal
window = tk.Tk()
window.title("Renomear Arquivos e Pastas")
window.geometry("400x150")

# Widgets
label = tk.Label(window, text="Clique no botão abaixo para buscar o diretório:")
label.pack(pady=10)

search_button = tk.Button(window, text="Buscar Diretório", command=select_directory, relief=tk.RIDGE)
search_button.pack(pady=5)

selected_directory_label = tk.Label(window, text="Diretório selecionado:")
selected_directory_label.pack(pady=5)

rename_button = tk.Button(window, text="Renomear", command=lambda: rename_files_and_folders(select_directory.get()), relief=tk.RIDGE)
rename_button.pack(pady=10)

# Inicia o loop principal da interface gráfica
window.mainloop()
