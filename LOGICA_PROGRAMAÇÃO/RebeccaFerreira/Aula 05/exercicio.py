# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo relatorio de produção diaria
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada uma:

# for lote in  range(1, 6) : 
#     print(f' Processando lote númeri {lote}...')
#     print('Qualidade verificada. [OK]')
#     print('Produção do dia finalizada!')

# #Imagine que você quer armazenar carros:
# for carros in range (10):
#     print(f'Quantidade de carros  (carros)')

#Exemplo 2
# # Contar até 4 
# for a in range(5):
#     print(a)

# #Exemplo 3 
# pecas= ['Engrenagens', 'Eixo' , 'Rolamento' , 'Parafuso']
# maquinas= [ 'Máquinas 1', 'Máquina 2']

# for item in pecas:  
#     print(f'Item em estoque: {item}')
#     for maq in maquinas :
#         print(f'Máquinas que temos {maq}')

#Exercico 01
# for a in range(1,11):
#     print(a)
#     print(f' Peça nº {a} processada com sucesso')
#     print('Ciclo concluido com sucesso!')

# #Exercico 02
# quantidade= [10, 5, 10, 13]
# frutas= ['Banana' , 'Manga', 'Melancia' , 'Abacaxi' ]
# for B in range(1, 11):
#      print(B)
#      print(f' A quantidade de Bananas produzids são nº {B} ')
# for M in range(1, 11) :
#      print(M)
#      print(f' A quantidade de Manga produzids são nº {M} ')
# for ME in range(1, 11) :
#      print(ME)
#      print(f' A quantidade de Melancia produzids são nº {ME} ')
# for A in range(1, 11):
#      print(A)
#      print(f' A quantidade de Abacaxi produzids são nº {A} ')

# Banana= 10
# Manga=5
# Melancia=10
# Abacaxi=13
# xtotal= Banana + Manga + Melancia + Abacaxi
# print('A quantidade total é ' , xtotal )

# #Atividade 3 
# print(' Bem-Vindo a nossa tabuada')
# x1= int(input('Digite o primeiro numero \n '))
# for x2 in range (1 , 11):
    
#     print(f"{x1} x {x2} = ", x1*x2)

# O laço while (Repetições Indeterminadas)

# Use o while quando você não sabe quando vai parar, Ele depende de uma condição (como um sensor de segurança ou um botão de emergencia)
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)

#Repete enquanto a temperatura estiver segura 
#Inicio 

# temperatura= 25
# while temperatura < 40:
#     print(f'Temperatura atual: {temperatura} °C. Sistema operando...')
#     temperatura += 3 #Simulando o aquecimento da máquina 
#     print('ALERTA! Temperatura atingiu o limmite. Desligando motor...')

# Exemplo: Menu de Interação
# opcao= ""

# while opcao != "sair":
#     opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ") .lower()
#     if opcao != "sair":
#       print(f'Dado "{opcao}" registrado no banco de dados. ')
# print('Sistema encerrado')
    
#Exercicio 04
# Criar um menu de opções com 4 itens ex: Escolher series apresente sua escolha de series das outras três.
# qualquer opção diferente sair do menu 

while opcao != "sair":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ") .lower()
    if opcao != "sair":
      print(f'Dado "{opcao}" registrado no banco de dados. ')
print('Sistema encerrado')

opção1= Comedia 
opção2= Horror
opção3= Ação 
opção4= Misterio


print('MEU MENU DE SERIES')
print('Comedia')
print('Horror')
print('Ação')
print('Misterio')


