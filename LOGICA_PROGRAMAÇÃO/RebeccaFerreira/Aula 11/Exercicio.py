def nome(): 
    nome = input("Digite seu nome: ")
    return nome
print(f"Olá {nome()}!")

def setor():
    Setor = input("Digite seu setor: ")
    return Setor

setor2 = ""

setor2 = setor()
if setor2 == "eletrica":
    print("Lembre-se de usar sempre: \n Luvas de Alta tensão! \n Botas dielétricas! \n Capacete com proteção contra choque!")
elif setor2 == "trabalho em altura":
    print("Lembre-se de usar sempre: \n Cinto de segurança tipo paraquedista! \n Trava Quedas! \n Capacete com jugular!")
elif setor2 == "mecanica":
    print("Lembre-se de usar sempre: \n Luvas de proteção! \n Óculos de segurança! \n Protetores auriculares!")
else:
    print("Setor sem necessidade de EPI.")
print(f"Bem-vindo ao setor {setor2}!")

def status_dos_treinamentos():
    status = input("Digite o status dos treinamentos (NR-10, NR-35 e Brigada): ")
    return status
print(f"O status dos treinamentos é: {status_dos_treinamentos()}!")

def verificar_treinamento():
    tempo = input(f"Digite o ultimo treinamento de Brigada realizado: \n (1) Menos de 6 meses \n (2) Entre 6 meses e 1 ano \n (3) Mais de 1 ano")
if 'Brigada' == '1':
    print("Treinamento atualizado! Parabéns!")
elif 'Brigada' == '2':
    print("Treinamento próximo de vencer! Agende uma reciclagem em breve.")
elif 'Brigada' == '3':
    print("Treinamento vencido! Agende uma reciclagem o mais rápido possível.")
else:
    print("Opção inválida. Por favor, selecione uma opção válida.")

    