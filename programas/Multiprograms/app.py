import tkinter as tk
import subprocess

# Funções para as ações dos botões
def executar_script1():
    subprocess.run(["python", "script1.py"])

def executar_script2():
    subprocess.run(["python", "renomeardir.py"])

# Criar a janela principal
janela = tk.Tk()
janela.title("GUI com Tkinter")
janela.geometry("550x550")  # Definir o tamanho da janela
janela.configure(bg="#0961AE")  # Restaurar a cor de fundo

# Botão para executar script1.py
botao1 = tk.Button(janela, text="PDF PARA WORD", font=("Arial", 14), command=executar_script1)
botao1.place(relx=0.5, rely=0.3, anchor=tk.CENTER, width=200, height=50)

# Botão para executar script3.py
botao3 = tk.Button(janela, text="UNDERLINE DIRS", font=("Arial", 14), command=executar_script2)
botao3.place(relx=0.5, rely=0.7, anchor=tk.CENTER, width=200, height=50)

# Iniciar o loop principal
janela.mainloop()
