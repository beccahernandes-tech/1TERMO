# #Foco: print, input, operações matematicas e f-string
# #1) Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# #"Operador [Nome] registrado no Turno [Turno]. Boa jornada!"
# print("Registro de Operador")
# operador= input("Digite se nome...")
# turno= input("Digite seu turno...")
# print(f"Operador {operador} registrado no Turno {turno}. Boa jornada!")

# # 2)Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# #exiba quantas peças serão produzidas em um turno de 8 horas.
# print("Cálculo de Produção")
# producao_hora = int(input("Digite a quantidade de peças produzidas em 1 hora..."))
# producao_turno = producao_hora
# print(f"Quantidade de peças produzidas em um turno de 8 horas:
# {producao_turno}")

# #3) Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# # ≈ 14.5 PSI) e exiba com duas casas decimais.
# print("Conversor de Unidade")
# pressao_bar = float(input("digite a pressão em Bar..."))
# pressao_psi = pressao_bar * 14.5
# print(f"Pressão em PSI {pressao_psi:.2f}")
# print(f"Pressão em PSI: {pressao_psi}" , round (pressao_psi, 2))

# #4) Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# # aritmética simples delas.
# print("Inspeção de Peças")
# nota1 = float(input("Digite a nota de inspeção 1 (0 a 10)..."))
# nota2 = float(input("Digite a nota de inspeção 2 (0 a 10)..."))
# nota3 = float(input("Digite a nota de inspeção 3 (0 a 10)..."))
# media = (nota1 + nota2 + nota3) / 3
# print(f"Média de qualidade da peça: (media:.2f)")
# print("Média de qualidade da peça: " , round(media, 2))

# #5) Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".
# print("Termometro Inteligente")
# temperatura = float(input("Digite a temperatura do motor em ° C...."))
# if temperatura < 40:
#     print('Baixa carga')
# elif 40<= temperatura <= 70:
#     print("Normal")
# else:
#     print("Alerta: Resfriamento Ativo!")
# print("Termostrato Inteligente - Versão 2")

# # PARTE 2
# print("Termometro Inteligente")
# temperatura = float(input("Digite a temperatura do motor em ° C...."))
# if temperatura < 40:
#     print('Baixa carga')
# elif  temperatura > 70:
#     print("Alerta: Resfriamento Ativo!")
# else:
#     print("Normal")
# print("Termostrato Inteligente - Versão 2")

# # 6)  Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# # exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".
# print('Classificador de Lotes')
# codigo_produto == ("Digite o codigo do produto ...")
# if codigo_produto == "A":
#     print("Alimentos")
# elif codigo_produto ('E'):
#     print("Eletronicos")
# else:
#     print("Desconhecido")

# # # 7) Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# # botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# # iniciar
# print('Segunça de Operação')
# sensor_porta = input("Digite o status do sensor da porta (fechada/aberta) ...")
# botao_emergencia = input("Digite o status do botão de emergencia (ligado/desligado) ...")
# if sensor_porta == "fechada" and botao_emergencia == "desligado':"
#     print('A máquina pode iniciar')
# else:
#     print("A máqiina não pode iniciar")
    
# # #8) Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# # o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# # "Processo Otimizado".
# print("Cálculo de Descarte")
# total_pecas = int(input("Digite o total de pecas produzidas..."))
# total_defeituosas = int(input("Digite o total de peças defeituosas..."))
# descarte_percentual = (total_defeituosas / total_pecas) * 100
# if descarte_percentual > 5: 
#     print("Revisar Processo")
# else:
#     print("Processo Otimizado")
# print(f"Processo Otimizado ")

# # #9) Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# # diga se está dentro da tolerância, acima ou abaixo.
# print('Validação de Medida')
# medida = float(input("Digite a medida de peça em mm..."))
# if medida < 9.8:
#     print("A peça está abaixo da tolerância.")
# elif medida > 10.2:
#     print("A peça está acima da tolerância.")
# else:
#     print("Validação de Medida ")

# # #10) Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# # de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!"
# print(" Bem Vindo a Contagem Regressiva")
# for i in range (10, 0 ,-1):
#     print(i)
#     print("Prensa Ativada!")

# # #11) Soma de Produção (Acumulador): Use um while para pedir o peso de várias caixas.
# # O loop para quando o usuário digitar 0. No fim, mostre o peso total acumulado.
# print("Soma de Produção (Acumulador)")
# peso_total= 0
# while True:
#     peso_caixa = float(input("Digite o peso da caixa (0 para parar)..."))
#     if peso_caixa == 0;
#         break
#     peso_total += peso_caixa
# print(f"Peso total acumulado: {peso_total:.2f} Kg")


# # #12) Múltiplas Leituras: Use um for para pedir a temperatura de 5 sensores diferentes.
# # Ao final, mostre qual foi a maior temperatura lida.
#  maior = 0
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

# 14)
print("Simulador de Estoque")
estoque= 100
while True:
    print("\nMenu:")
    print("1. Adicione itens")
    print("2. Remover itens")
    print("3. Sair")
    escolha= input("Escolha uma opção(1,2 ou 3)...")

    if escolha == 1:
        quantidade= int(input("Digite a quantidade de itens a adicionar..."))
        estoque += quantidade 
        print(f"Estoque atualizado: {estoque} itens")
    elif escolha == "2":
        quantidade = int(input("Digite a quantidade de itens a remover..."))
        estoque -= quantidade 
        print(f"Estoque atualizado: {estoque} itens")
        if estoque < 10:
            print("Estoque Critico!")
    elif escolha == "3":
        print("Saindo do simulador de estoque.")
        break
    else:
        print("Opção invalida. Tente Novamento")

# 15)
print("Relatorio de Turno Completo")
total_pecas = 5 
pecas_aprovadas = 0 
for i in range(1, total_pecas + 1):
    diamentro = float(input(f"Digite o diametro da peça {1} em mm..."))
    if 19.9 <= diametro <= 20.1:
        pecas_aprovadas += 1 
eficiencia = (pecas_aprovadas / total_pecas) * 100
print(f"Total de peças aprovadas: {pecas_aprovadas} ")
print(f"Eficiencia do lote: {eficiencia: 2f}%") 