import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3

def converter_audio():
    texto = ""
    arquivo = filedialog.askopenfilename(filetypes=[("texto", "*.txt")])
    if arquivo:
        with open(arquivo, 'r') as file:
            texto = file.read()

    if texto:
        engine = pyttsx3.init()
        engine.save_to_file(texto, 'output.mp3')
        engine.runAndWait()
        messagebox.showinfo('Sucesso', 'Seu audio foi criado com sucesso!')

root = tk.Tk()
root.title("Conversor de Texto para Áudio")
root.geometry('400x100')
btn_selecionar_arquivo = tk.Button(root, text="Selecionar Arquivo de Texto", command=converter_audio)
btn_selecionar_arquivo.pack(pady=20)

root.mainloop()