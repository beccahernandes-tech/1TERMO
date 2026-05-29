import tkinter as tk
from tkinter import messagebox


lista_cadastros = []



def obter_nome():
    
    nome = entry_nome.get().strip()
    return nome

def setor():
    
    Setor = entry_setor.get().lower().strip()
    return Setor

def verificar_treinamento():
    
    tempo = entry_treinamento.get().strip()
    
    if tempo == '1':
        return "Atualizado", "Treinamento atualizado! Parabéns!"
    elif tempo == '2':
        return "Proximo de vencer", "Treinamento próximo de vencer! Agende uma reciclagem em breve."
    elif tempo == '3':
        return "Vencido", "Treinamento vencido! Agende uma reciclagem o mais rápido possível."
    else:
        return "Opcao Invalida", "Opção inválida. Por favor, selecione uma opção válida."



def executar_fluxo():
    
    nome_usuario = obter_nome()
    
    
    setor2 = setor()
    
    if not nome_usuario or not setor2:
        messagebox.showwarning("Aviso", "Por favor, preencha o Nome e o Setor!")
        return

    
    if setor2 == "eletrica":
        mensagem_epi = "Lembre-se de usar sempre: \n Luvas de Alta tensão! \n Botas dielétricas! \n Capacete com proteção contra choque!"
    elif setor2 == "trabalho em altura":
        mensagem_epi = "Lembre-se de usar sempre: \n Cinto de segurança tipo paraquedista! \n Trava Quedas! \n Capacete com jugular!"
    elif setor2 == "mecanica":
        mensagem_epi = "Lembre-se de usar sempre: \n Luvas de proteção! \n Óculos de segurança! \n Protetores auriculares!"
    else:
        mensagem_epi = "Setor sem necessidade de EPI."

    
    status_final, mensagem_treino = verificar_treinamento()

    
    messagebox.showinfo("Saudação", f"Olá {nome_usuario}!\nBem-vindo ao setor {setor2}!")
    messagebox.showinfo("EPI Obrigatório", mensagem_epi)
    messagebox.showinfo("Status do Treinamento", mensagem_treino)

    
    funcionario_atual = {
        "nome": nome_usuario,
        "setor": setor2,
        "treinamento": status_final
    }
    lista_cadastros.append(funcionario_atual)

    
    print("\n--- DADOS ATUAIS NA VARIÁVEL ---")
    print(lista_cadastros)

    
    entry_nome.delete(0, tk.END)
    entry_setor.delete(0, tk.END)
    entry_treinamento.delete(0, tk.END)



janela = tk.Tk()
janela.title("Controle de EPI e Treinamentos")
janela.geometry("450x380")


lbl_nome = tk.Label(janela, text="Digite seu nome:", font=("Arial", 10, "bold"))
lbl_nome.pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)


lbl_setor = tk.Label(janela, text="Digite seu setor:", font=("Arial", 10, "bold"))
lbl_setor.pack(pady=5)
entry_setor = tk.Entry(janela, width=40)
entry_setor.pack(pady=5)


lbl_treino = tk.Label(janela, text="Digite o último treinamento de Brigada realizado:\n(1) Menos de 6 meses\n(2) Entre 6 meses e 1 ano\n(3) Mais de 1 ano", font=("Arial", 10), justify="center")
lbl_treino.pack(pady=5)
entry_treinamento = tk.Entry(janela, width=15)
entry_treinamento.pack(pady=5)


btn_rodar = tk.Button(janela, text="Rerificar e Cadastrar", command=executar_fluxo, bg="#0056b3", fg="white", font=("Arial", 11, "bold"))
btn_rodar.pack(pady=20)

janela.mainloop()





    