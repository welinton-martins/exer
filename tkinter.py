import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def msg_user():
    nome_usr = simpledialog.askstring("Input", "Qual o seu nome?")
    if nome_usr:
        messagebox.showinfo("Saudacao",f"Ola, {nome_usr}!")

janela = tk.Tk()
janela.title("Exemplo de GUI com Tkinter")
msg_btn = tk.Button(janela, text="Clique aqui para inserir seu nome:", command = msg_user)

msg_btn.pack(pady=20)
janela.mainloop()