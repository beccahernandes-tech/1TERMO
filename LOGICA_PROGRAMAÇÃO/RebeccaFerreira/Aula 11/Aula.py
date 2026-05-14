#Explicação de def: A palavra-chave "def" é usada para definir uma função em Python.
# Uma função é um bloco de código reutilizável que realiza uma tarefa específica
# return: A palavra-chave "return" é usada para retornar um valor de uma função. 
# Quando a função é chamada, ela executa o código dentro dela e retorna o valor especificado após a palavra-chave "return". 
# O valor retornado pode ser usado em outras partes do programa.

# def nome():
#     nome = input("Digite seu nome: ")
#     return nome
# print(f"Olá, {nome()}!")

# def valores():
#     print("Digite tres valores:")
#     a = int(input("Digite o primeiro valor: "))
#     b = int(input("Digite o segundo valor: "))
#     c = int(input("Digite o terceiro valor: "))
#     return a, b, c
# print(f"O maior valor é: {max(valores())}")

#Reutilizando funções 
# nome()
# valores()

##Conceito Chave 
#def: Indice o início da definição da função,
#Nome: Identifica a função para você chama-la depois. 
#Parametros: Ddados que a função recebe (opcional).
#return: Envia o resultado de volta para quem chamou a função (opcional).
def calcular_dobro(numero):
    return numero * 2
#Como usar: resultado = calcular_dobro(5)
print(calcular_dobro(8))