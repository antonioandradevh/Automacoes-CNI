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
            result_label.config(text=f"Conversões concluídas em '{output_folder}'", fg="#0961AE")
        except Exception as e:
            result_label.config(text=f"Erro ao converter o PDF para Word: {e}", fg="red")

# Configuração da janela
root = tk.Tk()
root.title("Conversor PDF para Word")
root.geometry("400x200")

# Centralizar a janela na tela
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry(f"400x200+{x}+{y}")

root.configure(bg="#0961AE")  # Definir o background da janela

# Botão para iniciar a conversão de múltiplos arquivos PDF para Word
convert_button = tk.Button(root, text="Converter PDFs para Word", command=convert_pdf_to_word, bg="#FFFFFF", fg="#0961AE")
convert_button.pack(pady=20)

# Rótulo para exibir o resultado da conversão
result_label = tk.Label(root, text="", bg="#0961AE", fg="white")
result_label.pack()

root.mainloop()
