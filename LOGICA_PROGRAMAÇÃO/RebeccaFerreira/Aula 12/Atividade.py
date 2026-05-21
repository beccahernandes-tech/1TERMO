#TKINTER

#Componentes widget
#tk: Tk() #Janela 
#lb: Label() #Rótulo
#bt: Button() #Botão

# import tkinter as tk
# from tkinter import messagebox

# # 1. Criar a janela principal
# janela = tk.Tk()
# janela.title("Minha primeira janela GUI")
# janela.geometry("1000x500") #Largura x Altura
# janela.configure(bg="#2d1bd1") #Cor de fundo da janela

# # 2. Criar a função do botão (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão!")

# # 3.Criar os componentes 
# lbl_titulo = tk.Label(janela, text="Bem vindo á nossa aula de Tkinter!",  bg= "#3134d8", font=("Arial", 14, "bold"))
# btn_clique = tk.Button(janela, text=("Clique Aqui!"), font=("Arial", 11), bg= "#2e31cc", fg="white", command=mostrar_mensagem)
# bnt_close = tk.Button(janela, text="Fechar", font=("Arial", 14, "bold"), bg="#d82121", command=janela.destroy)
# #4 Possicionar os componentes
# lbl_titulo.pack(pady=20) # 'pady' adiciona um espoaçamento vertical
# btn_clique.pack(pady=10)
# bnt_close.pack(pady=10)
# #5 Rodar o loop da interface 
# janela.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# def saudar_usuario():
#     # .get() serve para buscar o texto que vamos digitar
#     nome = entry_nome.get()

#     if nome == "":
#         messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
#     else:
#         messagebox.showinfo("Saudações Alunos", f"Olá, {nome}! Seja bem-vindo ao mundo das interfaces gráficas!")

# #Configurações da janela
# app = tk.Tk()
# app.title("Exemplo 1")
# app.geometry("350x200")

# #Componentes
# lbl_instrucao = tk.Label(app, text="Digite seu nome abaixo:")
# lbl_instrucao.pack(pady=10)

# campo_nome = tk.Entry(app, font=("Arial", 12))
# campo_nome.pack(pady=5)

# btn_enviar = tk.Button(app, text="Enviar", command=saudar_usuario)
# btn_enviar.pack(pady=15)

# app.mainloop()

#Exercico: Crie uma interface gráfica que calcule a média de três notas digitadas pelo usuário. 
# A interface deve conter campos para o usuário inserir as notas e um botão para calcular a média. 
# Ao clicar no botão, a média deve ser exibida em uma mensagem. 

import tkinter as tk
from tkinter import messagebox
def calcular_media():
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())
        nota3 = float(entry_nota3.get())
        media = (nota1 + nota2 + nota3) /3
        messagebox.showinfo("Média Calculada", f"A média das notas é: {media}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para as notas.")

#configurações da janela 
app = tk.Tk()
app.title("Calculadora da Becca Média")
app.geometry("1000x500")

lbl_titulo = tk.Label(app, text="Bem vindo á nossa aula de Tkinter!",  bg= "#3134d8", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=20)
#Componentes
entry_nota1 = tk.Entry(app, font=("Arial", 12))
entry_nota1.pack(pady=5)

entry_nota2 = tk.Entry(app, font=("Arial", 12))
entry_nota2.pack(pady=5)

entry_nota3 = tk.Entry(app, font=("Arial", 12))
entry_nota3.pack(pady=5)

btn_calcular = tk.Button(app, text="Calcular Média", command=calcular_media)
btn_calcular.pack(pady=15)

app.mainloop()