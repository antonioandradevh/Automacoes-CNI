import os
import tkinter as tk
from tkinter import filedialog
from unidecode import unidecode
from PIL import Image, ImageTk  # Importe o módulo Pillow

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

window.configure(bg="#1F5DA5")  # Definir o background da janela

# Carregar a imagem de fundo
imagem_fundo = Image.open("programas/Multiprograms/bk.png")
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

# Criar um rótulo para a imagem de fundo
fundo_label = tk.Label(window, image=imagem_fundo)
fundo_label.place(relwidth=1, relheight=1)

# Frame para centralizar os botões verticalmente
button_frame = tk.Frame(window, bg="#1F5DA5")
button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Widgets
label = tk.Label(button_frame, text="Clique no botão abaixo para buscar o diretório:", bg="#1F5DA5", fg="white")
label.pack(pady=10)

search_button = tk.Button(button_frame, text="Buscar Diretório", command=select_directory, relief=tk.RIDGE)
search_button.pack(pady=5, padx=10)
search_button.config(bg="#FFFFFF", fg="#1F5DA5", font=("Arial", 14))  # Ajuste a fonte e o tamanho

selected_directory_label = tk.Label(button_frame, text="Diretório selecionado:", bg="#1F5DA5", fg="white")
selected_directory_label.pack(pady=5)

rename_button = tk.Button(button_frame, text="Renomear", command=lambda: rename_files_and_folders(select_directory.get()), relief=tk.RIDGE)
rename_button.pack(pady=5, padx=10)
rename_button.config(bg="#FFFFFF", fg="#1F5DA5", font=("Arial", 14))  # Ajuste a fonte e o tamanho

# Inicia o loop principal da interface gráfica
window.mainloop()
