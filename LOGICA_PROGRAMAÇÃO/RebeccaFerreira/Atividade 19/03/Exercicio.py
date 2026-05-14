# #Lista de Temperaturas lidas pelo sensor por minuto 
# leituras= [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRITICO: {temp}°C detectado! Acionado parada de emergencia.")
#         break #O loop para aqui e NÃO lê os proximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. O peracional normal.")

# print( "Sistema desligado. Aguardando manutenção")

# materiais= ['metal', 'metal', 'plastico' , 'metal' , 'vidro', 'metal']
# for peça in materiais:
#     if peça != 'metal':
#         print(f"Aviso: Peça de {peça} detectada. Desviando para descarte... ")
#         continue #Pula o restaurante do código abaixo e vai para a próxima peça 

#     #Este código só roda se a peça for de metal 
#     print(f' Processando peça de {peça}. Furando e polindo')

# print('Fim do lote de produção')

#Exercicio 1
#Tente criar um código que conte de 1 a 10, maus use o continue para não imprimir o númeoro 5 (simulando uma falha de sensor especifica no item 5)
# for i in range(1 , 11):
#     if i == 5:
#         print(f'Falha no sensor do item 5')
#         continue 
#     print(f'Continuação da contagem {i}')

# from time import sleep 
# for i in range(1 ,11):
#     if i== 5:
#         print(f'Falha ao ler o n° {i}')
#         sleep(1.8)
#         continue 
#     print(i)
#     sleep(0.7)
# print("Acabou")

#Exercicio 2 
# Simule um semaforo com parada para cada cor, Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa. 

# import time 

# print(" SEMÁFORO")

# verde=10
# amarelo= 9
# vermelho= 8

# print('verde')
# time.sleep(verde)

# print('amarelo')
# time.sleep(amarelo)

# print('vermelho')
# time.sleep(vermelho)
# print("Ciclo finalizado")

# Exercicio 4
# Soma de cargas de energia (for)
# Uma fabrica tem 5 maquinas. Peça ao usuario (vai input dentro do loop) o consumo em KWh de cada uma das máquinas. Ao final do loop, o programa deve exibir o consumo total de fabrica 
# total=0
# for i in range(1, 6):
#     KWh= float(input(f'Digite o valor de KWh de {i} \n'))
#     total += KWh 

# print(f'O consumo total foi de: {total} ')


#Exercicio 5 
#Identificador de peças defeituosas (for +if)
# percorra uma lista de medidas de peças: 
# medidas= [50.1, 49.8, 52.0, 50.0, 48.5]
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça. diga se ela está 'Apavorada' ou 'Rejeitada'.

# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for i in medidas:
#     if i > 50.0:
#         print(f'Peça aprovada' , [i])
#     elif i < 50.0:
#         print(f'Peça reprovada' , [i])
#     else:
#        print(f'{i}= Reprovada')

#Exercicio 6 
# Uma balança idustrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50Kg, mas o sistema aceita variações. 

int(input('Digite a peso \n'))
for i in peso:
    if i > 50.0:
        print(f'Abaixo do peso' , [i])
    elif i < 50.0:
        print(f'Acima do peso' , [i])
    else:
       print(f'{i}= Reprovada')

#Exercicio 7 
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classificar o estado da máquina seguindo esta hierarquia:
# Critico (Prioridade 1): Se a pressão dor maior que 100 OU as horas de uso forem maiores que 10.000.
# Mensagem: 'PARADA IMEDIATA: Risco de falha catastofrica.'
# Alerta (Prioridade 2): Se a pressão estiver entre 80 a 100 (inclusiva).
# Mensagem:'MANUTENÇAO AGENDADA: Pressão acima do ideal'
# Monitoramento (Proridade 3): Se as horas de uso foram entre 8.000 e 10.000
# Mensagem: 'Aviso: Máquina aproximando-se da revisão de 10k horas '
# Normal: Para qualquer outro caso que não se encaixe nos acimas
# Mensagem: SISTEMA OPERAL: Todos os parimetros dentro da normalidade