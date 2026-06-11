#Exercicio Crie uma aplicação que faça o calculo de idade de pessoas.
#Deve perguntar o nome da pessoa e o ano de nascimento 

import tkinter as tk
from tkinter import messagebox, ttk

def cadastrar_usuario():
    nome_usuario = ent_nome_usuario.get() 
    idade = int(ent_ano_usuario).get()

    idade = 2026 - idade 

    if cadastrar_usuario == "" and idade =="":
        messagebox.showinfo("Bem-vindo", "Digite seu nome e seu ano de nascimento")
    else:
        messagebox.showinfo("Bem-vindo", f"{nome_usuario} sua idade é {idade})



janela = tk.Tk()
janela.title("Cadastro")
janela.geometry("400x400")
janela.configure(bg="light blue")

#1- Etapa componentes 
lbl_nome_usuario = tk.Label(janela, text=("Digite seu nome \n"), font=("Arial", 14), fg="green")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)
lbl_ano_usuario = tk.Label(janela, text=("Digite o seu ano de nascimento \n"))
lbl_ano_usuario.grid(row=1, column=0, pady=10, padx=10)


#2Entrys

ent_nome_usuario= tk.Entry(janela, font=("Arial", 14), width= 30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)
ent_ano_usuario = tk.Entry(janela, font=("Arial, 14"), width=30)
ent_ano_usuario.grid(row=1, column=1, pady=10, padx=10)


janela.mainloop()