

def saudação(nome):
    return f"Olá, {nome}!"

mensagem = saudação("Maria")
print(mensagem)

#Exemplo 2
nome = input('Seu nome: ')
idade = int(input('Sua idade: '))  #Converte texto para inteiro 
print(f' {nome} tem {idade} anos.')