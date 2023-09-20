import os
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
        selected_directory_label.config(text="Diretório selecionado: " + diretorio)
        rename_files_and_folders(diretorio)

# Criação da janela principal
window = tk.Tk()
window.title("Renomear Arquivos e Pastas")
window.geometry("500x500")

# Centralizar a janela na tela
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"500x500+{x}+{y}")

window.configure(bg="#0961AE")  # Definir o background da janela

# Widgets
label = tk.Label(window, text="Clique no botão abaixo para buscar o diretório:", bg="#0961AE", fg="white")
label.pack(pady=10)

search_button_frame = tk.Frame(window, bg="#0961AE")
search_button_frame.pack()

search_button = tk.Button(search_button_frame, text="Buscar Diretório", command=select_directory, relief=tk.RIDGE)
search_button.pack(pady=5, padx=10)
search_button.config(bg="#FFFFFF", fg="#0961AE", font=("Arial", 12))

selected_directory_label = tk.Label(window, text="Diretório selecionado:", bg="#0961AE", fg="white")
selected_directory_label.pack(pady=5)

rename_button_frame = tk.Frame(window, bg="#0961AE")
rename_button_frame.pack()

rename_button = tk.Button(rename_button_frame, text="Renomear", command=lambda: rename_files_and_folders(select_directory.get()), relief=tk.RIDGE)
rename_button.pack(pady=5, padx=10)
rename_button.config(bg="#FFFFFF", fg="#0961AE", font=("Arial", 12))

# Inicia o loop principal da interface gráfica
window.mainloop()