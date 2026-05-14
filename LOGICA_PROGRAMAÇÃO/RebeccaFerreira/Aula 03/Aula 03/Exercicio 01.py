# # #Exercicio 01
# # # Calculo de notas por semestre onde terá duas notas formativas e uma nota somativa para encerrar o semestre 
# # #os valores de notas são de 0 a 100
# print(' Primeiro semestre!')
# nota1 = int(input('Digite sua primeira nota: \n '))
# nota2 = int(input('Digite sua segunda nota: \n '))  
# nota3 = int(input('Digite sua terceira nota: \n '))
# ntotal = ((nota1 + nota2 + nota3)/3)
# print('A media do primeiro semestre  ', ntotal)

# print('Segundo semestre!')
# nota1 = int(input('Digite sua primeira nota: \n '))
# nota2 = int(input('Digite sua segunda nota: \n '))  
# nota3 = int(input('Digite sua terceira nota: \n '))
# mtotal = ((nota1 + nota2 + nota3)/3)
# print (' A media do segundo semestre foi' , mtotal)

# print(' Relatorio de notas ')
# print(' Media do primeiro semestre', ntotal)
# print(' Media do segundo semestre', mtotal)

# boas_vindas('Ana', 'Desenvolvedora')
# boas_vindas('Carlos' , 'Gerente')

# #Exemplo 4
# def configurar_conexao(servidor, porta=8080)
#     print(f' Conectando a (servidor) na porta (porta)...')

    

# configurar_conexao('192.168.1.1')
# configurar_conexao('10.0.0.1' , 3000)
# configurar_conexao('192.168.1.2')
# configurar_conexao('10.0.0.2' , 3001)

#Exercicio 2
# Calculo de idade: Deve apresentar o nome, curso, data de nascimento e apresentar a idade sua no final
# nome= input('Digite seu nome \n')
# curso= input('Digite seu curso \n')
# nascimento= int(input('Digite sua data de nascimento \n'))
# ano= int(input('Digite o ano \n'))
# idade= (ano - nascimento)
# print('Sua idade é:' , idade)

#Exercicio 3 
# Calcular gorjetas receba o valor da conta de um restaurante e retorne o valor da gorjeta (considerando 10% do valor da conta) 
# print('Nota fiscal da edwirges becca')
# conta= int(input('Digite o valor da sua conta \n'))
# gorjeta= int(input('O valor da porcentagem de gorjeta do graçom é de:' )) 
# total= (conta / gorjeta) + conta
# print('O valor da sua compra é de' , total)

#Exercicio 4 
# # Criar um sistema para calcular o sucessor e antecessor de um valor 
# print('Sistema de antecessor e sucessor')
# número= int(input(' Digite um numero desejado \n'))
# print('O antecessor é \n' , número - 1 )
# print('O sucessor é \n' , número + 1 )

#Exercicio 5 
# Criar um algoritimo para calcular a venda de livros e que toda venda apresente em desconto fixo de 5%
print('Seja Bem-Vindo a livraria da becca')
conta= int(input('Digite o valor do livro \n'))
quantidade= int(input('Digite a quantidade \n'))
total= (conta - (conta * quantidade /5)) 
print('Sua conta foi de:' , total)