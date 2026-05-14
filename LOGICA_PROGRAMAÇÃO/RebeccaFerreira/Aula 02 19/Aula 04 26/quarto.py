# if: "Se" a condição for verdadeira. 
# elif: "Senão, se" (usado para multiplas condições)
# else: "Senão" (executa se nenhuma das anteriores for verdadeira)

# print('Expressões lógicas')
# idade = int(input('Digite sua idade'))

# if idade >= 18:
#     print('Você é maior de idade')
#     print('Pode tirar carta de motorista')
# elif idade >= 16:
#     print('Você ainda não é de maior mais já pode votar')
# else: 
#     print('Você é menor de idade.')

# #Exemplo 2 
# print('Escolha sua modalidade?')
# print('Opções 1: TI')
# print('Opções 2: Humanas')
# print('Opção 1: Exatas')
# modalidade= int(input('Digite sua opção de modalidade por números \n'))
# if modalidade == 1:
#     print('Você escolheu TI')
# elif modalidade == 2: 
#     print('Você escolheu Humanas')
# else:
#     print('Você escolheu Extas')        

#Exemplo 3 
# print('Categoria de Series e Filmes')
# print('Escolha uma categoria')
# print('Série = S')
# print('Filmes = F')
# categoria = input('Digite sua categoria \n')
# if categoria == 'S':
#     print('Sua escolha foi para Séries')
# elif categoria == 'F':
#     print('Sua escolha foi para Filmes')
# else:
#     print('Você não escolheu nenhuma categoria ')    

# # Exemplo 4 
# print('Calculadora com condições')
# print('Escolha como quer calcular') 
# print('1= Soma')
# print('2= Subtração')
# print('3= Multiplicação')
# print('4= Divisão')
# calculadora = float(input('Digite sua opção para calcular \n')) 
# if calculadora == 1:
#     print('1 = Você escolheu soma')
#     soma1= int(input('Digite o primeiro valor \n')) 
#     soma2= int(input('Digite o segundo valor \n '))
#     print(soma1 + soma2) 
# elif calculadora == 2:
#     print('2 = Você escolheu subtração')
#     soma1= int(input('Digite o primeiro valor \n')) 
#     soma2= int(input('Digite o segundo valor \n '))
#     print(soma1 - soma2) 
# elif calculadora == 3:
#     print('2 = Você escolheu multiplicação')
#     soma1= int(input('Digite o primeiro valor \n')) 
#     soma2= int(input('Digite o segundo valor \n '))
#     print(soma1 * soma2) 
# elif calculadora == 4:
#     print('2 = Você escolheu divisão')
#     soma1= int(input('Digite o primeiro valor \n')) 
#     soma2= int(input('Digite o segundo valor \n '))
#     print(soma1 / soma2) 
# else:
#     print('Você não escolheu nenhuma opção')
#     print(' Sair do programa')

#Crie um algoritimo para calcular a media e com base em notas, podemos inserir duas notas e apresentar a média porém a nota base de 50 é aprovado e menor que esse valor será reprovado
# print('Olá a calculadora')
# nota1 = int(input('Digite a primeira nota \n'))
# nota2 = int(input('Digite a segunda nota \n '))
# media= (nota1 + nota2)

# if media >= 50:
#     print('Aprovado')
# else:
#     print('Reprovado')

#Exercicio 2
# print('Bem vindo ao meu semaforo')
# print('1 = verde')
# print('2 = amarelo')
# print('3 = vermelho')
# cores = int(input('Qual cor você deseja? \n'))

# if cores == 1:
#     print('verde')
# elif cores == 2:
#     print(' amarelo')
# elif cores == 3:
#     print(' Vermelho')
# else:
#     print('Somente essas cores')

# Exercicio 3
print('Bem Vindo a nossa loja')
print(' 1 = roupas 5%')
print('2 = perfume 2%')
print(' 3 = sapato 10%')
produtos = int(input('Quais produtos você comprou \n'))
if produtos == 1:
    v1 = float(input("Digite o valor do produto: \n"))
    qtde = int(input("Digite a quantidade do produto \n"))
    total = v1 * qtde * 5 / 100
    print("A sua compra foi de: ", total)
elif produtos == 2:
    v1 = float(input("Digite o valor do produto: \n"))
    qtde = int(input("Digite a quantidade do produto \n"))
    total = v1 * qtde * 2 / 100
    print("A sua compra foi de: ", total)
elif produtos == 3: 
     v1 = float(input("Digite o valor do produto: \n"))
    qtde = int(input("Digite a quantidade do produto \n"))
    total = v1 * qtde * 10 / 100
    print("A sua compra foi de: ", total)

#Exercicio 4
# nota1 = int(input('Digite a primeira nota \n'))
# nota2 = int(input('Digite a segunda nota \n '))
# media= (nota1 + nota2)

# if media >= 70:
#      print('Aprovado')
# elif media < 50:
#     print('recuperação')
# else:
#     print('Reprovado')


