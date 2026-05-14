# Projeto Cancela Automática
# Criar um algoritmo que consiga gerenciar entrada e saída de veículos, inserindo valores por hora permanecia. 
# A forma de entrada e saída deve ser especifícada e permitir o usúario inserir os dados necessários para registro do veículo

# Passos

# 1 - Pressionar botão , imprimiu um ticket
# Calcular tempo de permanencia 
# Pagar o ticket 
# Devolver o ticket na saída 
#Liberar e fechar cancelas

# 2 - Acesso por TAGs (Sem parar, Connect Car...)
# Calcular tempo de permanencia 
# Gerar pagamento em fatura 
# Liberar e fechar cancelas 

# 3 - Erros 
# Verificar sinal de trsnamissão da TAG 
# Verificar acessso por ticket ou TAG ao mesmo tempo 
# Perdeu ticket (levantar informações)
# Problemas com cancela 
import time

print("=== Estacionamento ===")

ticket_valido = "1234"

print(f"Seu ticket é: {ticket_valido}")
print("Entrada registrada!")

entrada = time.time()

# SAÍDA 
while True:
    ticket_digitado = input("Digite seu ticket para sair: ").strip()

    if ticket_digitado == ticket_valido:
        print("Ticket válido!")
        break
    else:
        print("Ticket inválido, tente novamente...")
        time.sleep(1)

saida = time.time()

tempo_total = (saida - entrada) / 60

valor = (tempo_total / 60) * 5

print(f"Tempo no estacionamento: {int(tempo_total)} minutos")
print(f"Valor a pagar: R${valor:.2f}")

# PAGAMENTO
while True:
    pagamento = float(input("Digite o valor pago: R$"))

    if pagamento >= valor:
        troco = pagamento - valor
        print(f"Pagamento aprovado! Troco: R${troco:.2f}")
        break
    else:
        print("Valor insuficiente, tente novamente...")

print("Abrir cancela ")
    



