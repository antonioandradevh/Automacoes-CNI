import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

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
            result_label.config(text=f"Conversões concluídas em '{output_folder}'")
        except Exception as e:
            result_label.config(text=f"Erro ao converter o PDF para Word: {e}")

# Configuração da janela
root = tk.Tk()
root.title("Conversor PDF para Word")

# Botão para iniciar a conversão de múltiplos arquivos PDF para Word
convert_button = tk.Button(root, text="Converter PDFs para Word", command=convert_pdf_to_word)
convert_button.pack()

# Rótulo para exibir o resultado da conversão
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
