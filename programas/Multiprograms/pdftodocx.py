import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter
from PIL import Image, ImageTk

def convert_pdf_to_word():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    
    if not file_paths:
        return
    
    output_folder = filedialog.askdirectory()
    
    if not output_folder:
        return
    
    for file_path in file_paths:
        try:
            cv = Converter(file_path)
            output_file = f"{output_folder}/{file_path.split('/')[-1].replace('.pdf', '.docx')}"
            cv.convert(output_file, start=0, end=None)
            cv.close()
            result_label.config(text=f"Conversões concluídas em '{output_folder}'", fg="#0961AE")
        except Exception as e:
            result_label.config(text=f"Erro ao converter o PDF para Word: {e}", fg="red")

# Configuração da janela
root = tk.Tk()
root.title("Conversor PDF para Word")
root.geometry("500x500")
root.configure(bg="#0961AE")  # Definir o background da janela

# Carregar a imagem de fundo
imagem_fundo = Image.open("programas/Multiprograms/bk.png")
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

# Criar um rótulo para a imagem de fundo
fundo_label = tk.Label(root, image=imagem_fundo)
fundo_label.place(relwidth=1, relheight=1)

# Criar um Frame para centralizar o botão
frame = tk.Frame(root, bg="#0961AE")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Botão para iniciar a conversão de múltiplos arquivos PDF para Word
convert_button = tk.Button(frame, text="Converter PDFs para Word", command=convert_pdf_to_word, bg="white", fg="#0961AE", font=("Arial", 14))
convert_button.pack()

# Rótulo para exibir o resultado da conversão
result_label = tk.Label(root, text="", bg="#0961AE", fg="white")
result_label.pack()

root.mainloop()
