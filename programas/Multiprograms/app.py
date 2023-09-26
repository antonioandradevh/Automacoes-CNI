import tkinter as tk
from PIL import Image, ImageTk  # Importe o módulo Pillow
import subprocess

# Funções para as ações dos botões
def executar_script1():
    subprocess.run(["python", "programas\Multiprograms\pdftodocx.py"])

def executar_script2():
    subprocess.run(["python", "programas/Multiprograms/renomeardir.py"])

def executar_script3():
    subprocess.run(["python", "programas\Multiprograms\juntarpdf.py"])

# Criar a janela principal
janela = tk.Tk()
janela.title("GUI com Tkinter")
janela.geometry("500x500")  # Definir o tamanho da janela

# Carregar a imagem de fundo
imagem_fundo = Image.open("programas/Multiprograms/bk.png")  # Substitua "seu_background.jpg" pelo nome do seu arquivo de imagem
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

# Criar um rótulo para a imagem de fundo
fundo_label = tk.Label(janela, image=imagem_fundo)
fundo_label.place(relwidth=1, relheight=1)  # Estique o rótulo para preencher toda a janela

# Botão para executar script1.py
botao1 = tk.Button(janela, text="PDF PARA WORD", font=("Arial", 14), command=executar_script1)
botao1.place(relx=0.5, rely=0.3, anchor=tk.CENTER, width=200, height=50)

# Botão para executar script2.py
botao2 = tk.Button(janela, text="RENOMEADOR", font=("Arial", 14), command=executar_script2)
botao2.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=200, height=50)

# Botão para executar script3.py
botao3 = tk.Button(janela, text="JUNTAR DOCS", font=("Arial", 14), command=executar_script3)
botao3.place(relx=0.5, rely=0.7, anchor=tk.CENTER, width=200, height=50)

# Iniciar o loop principal
janela.mainloop()