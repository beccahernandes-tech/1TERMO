#tratamento de erros com python
#Erros comuns:
# - ZeroDivisionError: divisão por zero 
# - ValueError: conversão de tipo inválida 
# - IndexError: acesso a índice fora do limite 
# - KeyError: acesso a chave inexistente em dicionário 

#Exemplo de tratamento de erros
# print("Exemplo de tratamento de erros")
# try:
#     num1 = int(input("Digite o primeiro número..."))
#     num2 = int(input("Digite o segundo número..."))
#     resultado = num1 / num2 
#     print(f"O resultado da divisão é: {resultado:.2f}")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero.")

# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número inteiro. ")

# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")

# except NameError:
#     print("Erro: Váriavel não definida.")

# if num1 > 100:
#     print("O número digitado é maior que 100.")
#     for i in range(1, 6):
#         print(f"{num1} x {i} = {num1 * i}")
#         if num1 * i > 1000:
#             print("O resultado da multiplicação é maior que 1000")
#             try:
#                 pass
#             except Exception as e :
#                 print(f"Ocorreu um erro inesperado: {e}")
# else:
#     print("O número digitado é menor ou igual a 100")

#Exemplo 1:
# Escreva um programa que solicite ao usúario um número inteiro e calcule a media de uma lista de números. O programa deve tratar os seguintes erros:
# ValueError: se o usúario digitar um valor que não seja um número inteiro.

# print("Lista de números ")
# total= 0
# try:
#     for baby1 in range(1,4):
#         baby1 = int(input("Digite um número inteiro \n"))
#         total += baby1
#     print("Média:" , baby1 / 4 ) 
#         # print("Média:" , baby1 / 4 ) 
# except ValueError:
#      print("se o usúario digitar um valor que não seja um número inteiro.")

# Exercicio 2:
# Escreva um programa que solicite ao usúario uma lista de palavras e conte quantas vezes cada palavra aparece na lista. O programa deve tratar os seguintes erros:
# - ValueError: se o usúario digitar um valor que não seja uma string. 

# print("Lista de palavras")
# contagem= {}

# while True:
#     palavra = input("Digite uma palavra (ou 'flm' para parar): ")

#     if palavra == "flm":
#         break

#     try:
#         int(palavra)
#         print("ERRO: digite apenas palavras")
#     except ValueError:
#         if palavra in contagem:
#             contagem[palavra] += 1
#         else:
#             contagem[palavra] = 1
# print(contagem)

#Exercicio 3 
# escrever um programa mais simples de tratamento de erros, como por exemplo, solicitar um usuario um número. O programa deve tratar os seguintes erros:
# - ValueError: se o usuário digitar um valor que não seja um número 
# - ZeroDivisionError: se o usuário digital zero como divisor.
total=0
try:
    nome = int(input("Digite um numero \n "))
    divisão= int(input("Digite um dividor \n"))
    total= nome/divisão
    print("Resultado" , total)
except ValueError: 
 print("Digite números") 
except ZeroDivisionError: 
 print("Não é possivel dividir por zero!.")
