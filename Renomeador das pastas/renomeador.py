import os
import sys
from unidecode import unidecode

# Define o diretório atual como o diretório onde o arquivo está localizado
diretorio_atual = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(diretorio_atual)

def rename_files_and_folders(directory):
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

if __name__ == "__main__":
    diretorio = input("Digite o caminho para o diretório: ")
    rename_files_and_folders(diretorio)
