# 1) Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
#"Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# print('Bem vindo ao nosso Registro de Operador \n')
# nome = input('Qual é o nome do operador? \n ')
# registro = input(' Qual é o turno?')
# print(f'Operador {nome} Registrado no Turno {registro}  Boa jornada!')

#2)Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
#exiba quantas peças serão produzidas em um turno de 8 horas.

# print('Bem vindo a nossa produção')
# pecas= int(input('Digite a quantidade de peças em uma hora \n' ))
# total= pecas * 8 
# print('A quantidade de pecças produzidas em 8 horas é de ' , total )

#3) Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# pressao= float(input('Qual é a pressão ? \n'))
# PSI= 14.5
# total= pressao * PSI
# print('A pressão por BAG é de ' , round(total,2))

#4) Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# print('Qual é a nota de inspeção de peça \n ')
# peca1 = int(input('Digite o valor da primeira peça: \n '))
# peca2 = int(input('Digite o valor da primeira peça: \n '))  
# peca3 = int(input('Digite o valor da primeira peça: \n '))
# total = ((peca1 + peca2 + peca3)/3)
# print (' O total de peças foi' , total)

# #5) Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# print('Termostato Inteligente')
# temperatura = int(input('Digite a temperatura \n'))
# if temperatura < 40:
#     print(f"BAIXA CARGA: {temperatura}°C detectado!")
# elif 40 > temperatura <= 70:
#     print('NORMAL')
# else: 
#     print('ALERTA: Resfriamento Ativado!')

# 6)  Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# print(' Bem vindo ao classificador de Lotes')
# código= input(' Digite o código do produto \n ')
# if código == "A":
#     print('Alimentos')
# elif código == "E":
#     print('Eletrônicos')
# else:
#     print('Desconhecido')

# # 7) Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar

# print('Bem vindo a Segurança de Operação')
# sensor_porta= input("Sensor porta aberto ou fechado \n")
# sensor_emergencia= input("Sensor emergencia desligado ou ligado \n ")
# if sensor_porta == "fechado" or sensor_emergencia == " desligado":
#     print("Máquina pode ligar")
# else:
#     print("Máquina não pode ligar")

# #8) Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# print("Bem Vindo ao Calculo de Descarte")
# pecas= int(input("Total de peças produzidas \n "))
# defeituosas= int(input("Total de defeituosas \n"))
# if defeituosas > 5:
#     print("Revisar Processo")
# else:
#     print("Processo Otimizado")

# #9) Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# print("Validação de Medidas")
# medida= float(input("Digite a medida da peça \n "))
# if medida < 9.8:
#     print("Está peça está abaixo da tolerância")
# elif medida > 10.2:
#     print("Está peça está a cima da tolerância")
# elif medida < 
# else:
#     print("Está peça está no limite de tolerância")

# #10) Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!"

# print(" Bem Vindo a Contagem Regressiva")
# for i in range (10, 0 ,-1):
#     print(i)
#     print("Prensa Ativada!")

# #11) Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.

# total=0
# print("Soma de Produção")
# while True: 
#     peso= float(input("Digite o peso das caixas \n"))
#     if peso == 0:
#         break 
#     total+= peso
#     print('ALERTA! Temperatura atingiu o limmite. Desligando motor...')

# #12) Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# Ao final, mostre qual foi a maior temperatura lida.

# maior = 0
# for i in range (5):
#     temperatura= float(input(f"Temperatura {i+1}: "))
#     if i == 0 or temperatura > maior:
#         maior = temperatura
# print(f" Maior Temperatura: , {maior}")

#13) 
# senha_correta = "admin123"
# tentativas = 3 
# while tentativas > 0:
#     senha - input("Digite a senha:")
#     if senha == senha_correta:
#         print("Acesso Permitido")
#         break 
#     else:
#         tentativas = 1 
#         print("Acesso Negado")
#     if tentativas == 0:
#         print("Painel Bloqueado")
