#Revisão Tkingter 

import tkinter as tk
from tkinter import messagebox, ttk

#DEF funções em bloco 
def cadastrar_usuario():
    #.get
    nome_usuario = ent_nome_usuario.get()
    curso_usuario = ent_curso_usuario.get()
    escola_usuario = cmb_nome_escola.get()

    if nome_usuario =="" and curso_usuario and escola_usuario == "":
        messagebox.showinfo("Bem-vindo", "Digite seu nome e seu curso e escolha sua escola")
    else:
        messagebox.showinfo("Bem-vindo", f"Olá{nome_usuario} seu curso é {curso_usuario} e sua escola é {escola_usuario}!")




# 0 - Etapa Janela
janela = tk.Tk()
janela.title("Revisão Tkinter")
janela.geometry("400x400")
janela.configure(bg="light blue")

#1- Etapa componentes 
# Labels = Rotulos ou nossos antigos prints 

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=("Arial", 14), fg="green")
lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)                                                            
lbl_curso_usuario= tk.Label(janela, text="Digite seu curso", font=("Arial", 14), fg="green")
lbl_curso_usuario.grid(row=1, column=0, pady=10, padx=10)           
lbl__nome_escola= tk.Label(janela, text="Escolha sua Escola:", font=("Arial", 14), fg="black")

#Entrys = Caixa de texto antigos input 
ent_nome_usuario= tk.Entry(janela, font=("Arial", 14), width= 30)
ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)
ent_curso_usuario= tk.Entry(janela, font=("Arial", 14), width= 30)
ent_curso_usuario.grid(row=1, column=1, pady=10, padx=10)

# ComboBox = Caixa de seleção
cmb_nome_escola= ttk.Combobox(janela, values=["SESI408", "SESI05"])
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)

#Botões = Botões de clique
btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font= ("Arial", 14), fg="black", command=cadastrar_usuario)
btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)
btn_fechar_janela = tk.Button(janela, text='Fechar', command=janela.destroy)
btn_fechar_janela.grid(row=6, column=1, pady=10, padx=10)

# 4 Etapa Loop
janela.mainloop()