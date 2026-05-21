import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Briagada")
janela.geometry("1000x500") #Largura x Altura
janela.configure(bg="#0e0e0f")


def funcionarios():
    setor2 = entry_setor.get().lower()

    if setor2 == "eletrica":
        messagebox.showwarning(
            "EPI - Elétrica",
            "Use:\n"
            "- Luvas isolantes\n"
            "- Capacete\n"
            "- Óculos de proteção"
        )

    elif setor2 == "mecanica":
        messagebox.showwarning(
            "EPI - Mecânica",
            "Use:\n"
            "- Luvas de raspa\n"
            "- Botina de segurança\n"
            "- Óculos de proteção"
        )

    elif setor2 == "trabalho em altura":
        messagebox.showwarning(
            "EPI - Altura",
            "Use:\n"
            "- Cinto de segurança\n"
            "- Capacete com jugular\n"
            "- Talabarte"
        )

    else:
        messagebox.showinfo(
            "Setor Seguro",
            "Setor sem necessidade de EPI."
        )

lbl_setor = tk.Label(janela, text="Digite seu setor:", bg="#0e0e0f", fg="white", font=("Arial", 14))
lbl_setor.pack(pady=20)
entry_setor = tk.Entry(janela, font=("Arial", 12))
entry_setor.pack(pady=10)
btn_verificar = tk.Button(janela, text="Verificar EPI", command=funcionarios, bg="#2e31cc", fg="white", font=("Arial", 12))
btn_verificar.pack(pady=15) 



janela.mainloop()