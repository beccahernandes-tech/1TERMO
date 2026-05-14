# #Clean code - Aula 8
# #Para Usar?
# #Como usar?
# print("Clean Code - Aula 8")
# Aula=8
# print(f"Estamos na aula {Aula} de Clean Code")

# #Manipulação de arquivos e Texto 
# texto = "Python"
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower())
# print(texto.strip().capitalize())
# print(texto.strip().title())
# print(texto.strip().replace("" , "_"))
# print(texto.strip().split())

#os.getcwd 
#Para listar o caminho da pasta 

# #Escrevendo 
# with open("notas.txt" , "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre Clean Code")

# #Lendo 
# with open("notas.txt" , "r") as arquivo:
#     conteudo= arquivo.read()
#     print(conteudo)

#Execução de comandos do sistemas 
import os # importa o módulo os para interagir com o sistema operacional

# #Onde estou?
# print(os.getcwd())
# #Listas arquivos na pasta 
# print(os.listdir())
# print(os.listdir("..")) #Lista arquivos da pasta pai
# print(os.listdir("..\\..")) #Lista arquivos da pasta avó
# print(os.listdir("C:\\")) #Lista de arquivos da raiz do C 
# print(os.listdir("C:\\Users")) #Lista arquivos da pasta Users 
# print(os.listdir("C:\\Users\\Public")) #Lista arquivos da pasta Public 

#Listar arquivos na pasta 
# print(os.listdir())

# os.mkdir("Nova_pasta")
# os.rename("Nova_pasta" , "Pasta_renomeada")
# os.rmdir("Nova pasta")

# #exercicio 1:
# #Crie um strip que mostre o caminho da pasta atual.

# # print(os.getcwd())

# #2
# # print(os.listdir())

# #3
# # os.mkdir("projeto")
# # os.rename("projeto" , "meus projetos")
# # os.rmdir("meus projetos")

# #4
# # with open("log.txt" , "w") as arquivo:
# #     arquivo.write("\nLog de atividades")


# # with open("log.txt" , "r") as arquivo:
# #    conteudo= arquivo.read()
# #    print(conteudo)

# #5)
# pessoa= {
#     "nome": "Alice",
#     "idade": 30, 
#     "cidade": "São Paulo",
#     "Profissão": "Engenheira"
# }
# print(pessoa["nome"],pessoa["idade"])

# pessoa2= {
#     "nome": "Rebecca",
#     "idade": 16, 
#     "cidade": "Limeira",
#     "Profissão": "TI"
# }
# print(pessoa2["nome"])

#Exercicio 6 
# with open("desliga.bat" , "w") as desligar:
#     desligar.write("shutdown -s -t 3600 -c \ 'Desligamento programado para daqui a pouco a 1 hora. Salva seu trabalho!\ ")
#     # -s comando para desligar
#     # -t tempo difinir 
#     # -a cancelar desligamento 

# with open("desliga.bat" , "r") as desligar:
#     conteudo = desligar.read()
#     print(conteudo)

# 7)
# print(os.listdir())

# with open("notas.txt" , "r") as arquivo:
#      conteudo= arquivo.read()
#      print(conteudo)

# with open("notas.txt" , "w") as arquivo:
#      arquivo.write("notas_backup.txt")

#Exercicio 2 
# Escreva um script que liste os arquivos d euma psta e exclua os arquivos com extensão ".tmp" , O script deve exibir uma mensagem para cada arquivo excluido
pasta= os.listdir()
for arquivo in pasta:
     if arquivo.endswith(".tmp"):
          os.remove(arquivo) #remove irá apagar o arquivo 
          print(f"Arquivo {arquivo} excluido")
print("Limpeza de arquivos concluida")

#8) Criar um script de monitoramento de temperatura 
# Escreva um script que monitore a temperatura de um motor. O script deve ler a temperatura de um arquivo "temperatura.txt" e exibir uma mensagem de alerta se a temperatura estiver acima de 70°
pasta= os.listdir()
with open("temperatura.txt" , "r") as arquivo:
      temperatura= float(f .read() .string())
      print(f"temperatura: {temperatura} C°)
  if temperatura > 70: 
        

