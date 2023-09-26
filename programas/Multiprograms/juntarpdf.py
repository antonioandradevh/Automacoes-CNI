import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
from docx import Document
from PIL import Image, ImageTk

def merge_pdfs_and_docs():
    # Selecionar arquivos PDF e DOCX
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF and DOCX Files", "*.pdf;*.docx")])
    
    if not file_paths:
        return
    
    # Selecionar pasta de saída
    output_folder = filedialog.askdirectory()
    
    if not output_folder:
        return
    
    pdf_merger = PdfMerger()
    
    for file_path in file_paths:
        _, file_extension = os.path.splitext(file_path)
        
        if file_extension.lower() == ".pdf":
            # Verificar se o arquivo PDF é válido antes de adicioná-lo ao merger
            if is_valid_pdf(file_path):
                pdf_merger.append(file_path)
            else:
                result_label.config(text=f"Arquivo PDF inválido: '{file_path}'", fg="red")
        elif file_extension.lower() == ".docx":
            # Arquivo DOCX, converter para PDF e adicionar ao merger
            doc = Document(file_path)
            pdf_path = os.path.join(output_folder, f"{os.path.basename(file_path)}.pdf")
            doc.save(pdf_path)
            pdf_merger.append(pdf_path)
            os.remove(pdf_path)  # Remover o arquivo PDF temporário
    
    # Salvar o arquivo PDF final
    output_pdf_path = os.path.join(output_folder, "merged.pdf")
    with open(output_pdf_path, "wb") as output_pdf:
        pdf_merger.write(output_pdf)
    
    result_label.config(text=f"Arquivos combinados em '{output_pdf_path}'", fg="#0961AE")

# Função para verificar se um arquivo PDF é válido
def is_valid_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            content = file.read()
        return b"%PDF" in content  # Verifica se o arquivo contém a marca de início de PDF
    except Exception as e:
        print(f"Erro ao verificar arquivo PDF: {e}")
        return False

# Configuração da janela
root = tk.Tk()
root.title("Juntar PDFs e DOCX")
root.geometry("500x500")
root.configure(bg="#0961AE")  # Definir a cor de fundo da janela

# Carregar a imagem de fundo
imagem_fundo = Image.open("programas/Multiprograms/bk.png")
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

# Criar um rótulo para a imagem de fundo
fundo_label = tk.Label(root, image=imagem_fundo)
fundo_label.place(relwidth=1, relheight=1)

# Criar um Frame para centralizar o botão
frame = tk.Frame(root, bg="#0961AE")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Botão para juntar arquivos PDF e DOCX
merge_button = tk.Button(frame, text="Juntar PDFs e DOCX", command=merge_pdfs_and_docs, bg="white", fg="#0961AE", font=("Arial", 14))
merge_button.pack()

# Rótulo para exibir o resultado da junção
result_label = tk.Label(root, text="", bg="#0961AE", fg="white")
result_label.pack()

root.mainloop()
