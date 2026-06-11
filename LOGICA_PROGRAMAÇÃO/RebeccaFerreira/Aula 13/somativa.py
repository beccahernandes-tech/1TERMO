#------------SOMATIVA------------------
#REGISTRO DO OPERADOR 
#1) 
# import tkinter as tk
# from tkinter import messagebox, ttk

# def cadastrar_operador():
#     nome_usuario = ent_nome_usuario.get()
#     numero_turno = cmb_numero_turno.get()

#     if nome_usuario =="" and numero_turno == "":
#         messagebox.showinfo("Bem-vindo", "Digite seu nome e escolha seu turno")
#     else:
#         messagebox.showinfo("Bem-vindo!", f"Operador {nome_usuario}! registrado no Turno {numero_turno} Boa Jornada!")

# janela = tk.Tk()
# janela.title("Registro do Operador")
# janela.geometry("400x400")
# janela.configure(bg="light pink")

# lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font="Arial", fg="black")
# lbl_nome_usuario.grid(row=0, column=0, pady=10, padx=10)

# ent_nome_usuario = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_nome_usuario.grid(row=0, column=1, pady=10, padx=10)

# lbl_numero_turno = tk.Label(janela, text="Selecione seu turno:", font="Arial", fg="black")
# lbl_numero_turno.grid(row=1, column=0, pady=10, padx=10)

# cmb_numero_turno = ttk.Combobox(janela, values=["A", "B", "C"])
# cmb_numero_turno.grid(row=1, column=1, pady=10, padx=10)

# btn_cadastrar_funcionario = tk.Button(janela, text="Cadastrar", font="Arial", command=cadastrar_operador)
# btn_cadastrar_funcionario.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()

#2)
# import tkinter as tk 
# from tkinter import messagebox, ttk 


# def calcular_peças():
#     quantidade_peças = int(ent_quantidade_peças.get())
#     peças= quantidade_peças * 8
#     if quantidade_peças =="" and peças == "":
#         messagebox.showinfo("Digite a quantidade de peças produzidas em 1 hora")
#     else:
#         messagebox.showinfo("Cocluido",f"A quantidade de peças em 8 horas é {peças}")



# janela = tk.Tk ()
# janela.title("Cálculo de Média")
# janela.geometry("500x400")
# janela.configure(bg="light yellow")

# lbl_quantidade_peças = tk.Label(janela, text="Digite o total de peças produzidas em 1 hora:")
# lbl_quantidade_peças.grid(row=0, column=0, pady=1, padx=10)


# ent_quantidade_peças = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_quantidade_peças.grid(row=0, column=1, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Calcular", font= ("Arial", 14), fg="black", command=calcular_peças)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()

#3)
# import tkinter as tk 
# from tkinter import messagebox

# def calcular_bar():
#      quantidade_bar = int(ent_quantidade_bar.get())
#      bars= quantidade_bar * 14.5
#      if quantidade_bar =="" and bars == "":
#          messagebox.showinfo("A pressão em BARS", "Digite a pressão em BARS")
#      else:
#          messagebox.showinfo("Cocluido",f"A pressão em PSI é {bars:.2f}")


# janela = tk.Tk()
# janela.title("Revisão Tkinter")
# janela.geometry("700x600")
# janela.configure(bg="light blue")

# lbl_quantidade_bar = tk.Label(janela, text="Digite a quantidade de  BARS", font=("Arial", 14), fg="green")
# lbl_quantidade_bar.grid(row=0, column=0, pady=10, padx=10)

# ent_quantidade_bar = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_quantidade_bar.grid(row=0, column=1, pady=10, padx=10)

# btn_realizar_calcular = tk.Button(janela, text="Calcular", font= ("Arial", 14), fg="black", command=calcular_bar)
# btn_realizar_calcular.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()

#4)
# import tkinter as tk 
# from tkinter import messagebox

# def calcular_media():
#     media1= float(ent_media1.get())
#     media2= float(ent_media2.get())
#     media3= float(ent_media3.get())
#     media_final = (media1 + media2 + media3) / 3

#     if media1 =="" and media2 =="" and media3 =="":
#         messagebox.showinfo("Média de Qualidade", "Digite as três médias para calcular a média final")
#     else:
#         messagebox.showinfo("Média de Qualidade", f"A média final é {media_final}")

# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("700x600")
# janela.configure(bg="light green")

# lbl_media1 = tk.Label(janela, text="Digite a primeira nota:", font=("Arial", 14), fg="black")
# lbl_media1.grid(row=0, column=0, pady=10, padx=10)
# lbl_media2 = tk.Label(janela, text="Digite a segunda nota:", font=("Arial", 14), fg="black")
# lbl_media2.grid(row=1, column=0, pady=10, padx=10)
# lbl_media3 = tk.Label(janela, text="Digite a terceira nota:", font=("Arial", 14), fg="black")
# lbl_media3.grid(row=2, column=0, pady=10, padx=10)

# ent_media1 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_media1.grid(row=0, column=1, pady=10, padx=10)
# ent_media2 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_media2.grid(row=1, column=1, pady=10, padx=10)
# ent_media3 = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_media3.grid(row=2, column=1, pady=10, padx=10)


# btn_realizar_cadastro = tk.Button(janela, text="Calcular", font= ("Arial", 14), fg="black", command=calcular_media)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()

#5)
# import tkinter as tk
# from tkinter import messagebox

# def verificar_temperatura():
#     temperatura = float(ent_temperatura.get())

#     if temperatura >= 40:
#         messagebox.showwarning("Alerta", "Temperatura do motor muito baixa")
#     elif temperatura <= 70:
#         messagebox.showinfo("Status", "Temperatura do motor normal")
#     else:
#         messagebox.showwarning("Alerta", "Temperatura do motor muito alta")


# janela = tk.Tk()
# janela.title("Termostato Inteligente ")
# janela.geometry("700x500")
# janela.configure(bg="light blue")

# lbl_temperatura = tk.Label(janela, text="Digite a temperatura do motor:", font=("Arial", 14), fg="black")
# lbl_temperatura.grid(row=0, column=0, pady=10, padx=10)

# ent_temperatura = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_temperatura.grid(row=0, column=1, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Conferir", font= ("Arial", 14), fg="black", command=verificar_temperatura)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)


# janela.mainloop()


#6)
# import tkinter as tk
# from tkinter import messagebox

# def cadastrar_objeto():
#     codigo_produto = ent_código.get()
#     if codigo_produto.startswith("A") or codigo_produto.startswith("a"):
#         messagebox.showinfo("Categoria", "Alimentos")
#     elif codigo_produto.startswith("E") or codigo_produto.startswith("e"):
#         messagebox.showinfo("Categoria", "Eletrônicos")
#     else:
#         messagebox.showinfo("Categoria", "Desconhecido")


# janela = tk.Tk()
# janela.title("Revisão Tkinter")
# janela.geometry("700x600")
# janela.configure(bg="light blue")

# lbl_código = tk.Label(janela, text="Digite o código do produto;", font=("Arial", 14), fg="green")
# lbl_código.grid(row=0, column=0, pady=10, padx=10)

# ent_código = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_código.grid(row=0, column=1, pady=10, padx=10)


# btn_realizar_cadastro = tk.Button(janela, text="Cadastrar", font= ("Arial", 14), fg="black", command=cadastrar_objeto)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()]

#7)
# import tkinter as tk
# from tkinter import messagebox

# def verificar_status():
#     status_maquina = ent_verificar.get().lower()
#     status_emergencia = ent_emergencia.get().lower()


#     if status_maquina == "fechada":
#         messagebox.showinfo("Status da Máquina", "A máquina pode operar")
#     elif status_emergencia == "desligado":
#         messagebox.showwarning("Status da Máquina", "A máquina pode pode operar")
#     else:
#         messagebox.showerror("Status da Máquina", "A máquina não pode operar")

# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("400x400")
# janela.configure(bg="light blue")

# lbl_verificar = tk.Label(janela, text="Digite o status da maquina", font=("Arial", 14), fg="black")
# lbl_verificar.grid(row=0, column=0, pady=10, padx=10)
# lbl_verificar = tk.Label(janela, text="Digite o status do botão de emergencia", font=("Arial", 14), fg="black")
# lbl_verificar.grid(row=1, column=0, pady=10, padx=10)

# ent_verificar = tk.Entry(janela,font=("Arial", 14), width=30)
# ent_verificar.grid(row=0, column=1, pady=10, padx=10)
# ent_emergencia = tk.Entry(janela,font=("Arial", 14), width=30)
# ent_emergencia.grid(row=1, column=1, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Verificar", font= ("Arial", 14), fg="black", command=verificar_status)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()

#8)
# import tkinter as tk
# from tkinter import messagebox

# def calcular_pecas():
#     total_pecas = int(ent_total_pecas.get())
#     pecas_defeituosas = int(ent_pecas_defeituosas.get())
    
#     pecas_descartadas = (pecas_defeituosas / total_pecas) * 100


#     if pecas_defeituosas / total_pecas < 0.05:
#         messagebox.showinfo("Revisar Processo", "O processo precisa ser revisado")
#     else:
#         messagebox.showinfo("Processo Otimizado", f"A porcentagem de peças descartadas é {pecas_descartadas:.2f}%")


# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("400x400")
# janela.configure(bg="light blue")

# lbl_total_pecas = tk.Label(janela, text="Digite o total de peças produzidas")
# lbl_total_pecas.grid(row=0, column=0, pady=10, padx=10)
# lbl_pecas_defeituosas = tk.Label(janela, text="Digite o total de peças defeituosas")
# lbl_pecas_defeituosas.grid(row=1, column=0, pady=10, padx=10)

# ent_total_pecas = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_total_pecas.grid(row=0, column=1, pady=10, padx=10)
# ent_pecas_defeituosas = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_pecas_defeituosas.grid(row=1, column=1, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Revisar", font= ("Arial", 14), fg="black", command=calcular_pecas)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)


# janela.mainloop()

#9)
# import tkinter as tk
# from tkinter import messagebox

# def verificar_peca():
#     medida_peca = float(ent_medida.get())

#     if medida_peca < 9.8:
#         messagebox.showwarning("Alerta", "Peça fora da especificação: Medida muito baixa")
#     elif medida_peca > 10.2:
#         messagebox.showwarning("Alerta", "Peça fora da especificação: Medida muito alta")
#     else:
#         messagebox.showinfo("Status", "Peça dentro da especificação")


# janela = tk.Tk()
# janela.title("Validação de Medida")
# janela.geometry("400x400")
# janela.configure(bg="light blue")

# lbl_medida = tk.Label(janela, text="Digite a medida da peça em milimetros:", font=("Arial", 14), fg="black")
# lbl_medida.grid(row=0, column=0, pady=10, padx=10)

# ent_medida = tk.Entry(janela, font=("Arial", 14), width=30)
# ent_medida.grid(row=0, column=1, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Verificar", font= ("Arial", 14), fg="black", command=verificar_peca)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()

#10)
# import tkinter as tk
# from tkinter import messagebox

# janela = tk.Tk()
# janela.title("Contagem Regressiva")
# janela.geometry("400x400")
# janela.configure(bg="light blue")

# def contar():
#     for i in range(10, -1, -1):
#         messagebox.showinfo("Contagem Regressiva", f"Contagem: {i}")
# btn_contar = tk.Button(janela, text="Iniciar Contagem", font=("Arial", 14), fg="black", command=contar)
# btn_contar.grid(row=0, column=0, pady=10, padx=10)

# btn_realizar_cadastro = tk.Button(janela, text="Prensa Ativada", font= ("Arial", 14), fg="black", command=cadastrar_usuario)
# btn_realizar_cadastro.grid(row=5, column=1, pady=10, padx=10)

# janela.mainloop()          
