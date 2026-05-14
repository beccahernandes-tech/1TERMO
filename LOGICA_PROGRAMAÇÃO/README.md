# Lógica de Programação com Python e GitHub

## 📌 Fundamentos da Lógica de Programação
*   **Pensamento Computacional:** Decomposição de problemas, reconhecimento de padrões, abstração e design de algoritmos.
*   **Algoritmos e Fluxogramas:** Representação de passos lógicos através de pseudocódigo (portugol) e blocos visuais.
*   **Variáveis e Tipos de Dados:** Armazenamento de informações na memória (Textos, Números Inteiros, Decimais e Booleanos).
*   **Operadores:** Utilização de operadores aritméticos (+, -, *, /), relacionais (>, <, ==, !=) e lógicos (E, OU, NÃO).

---

## 🐍 Linguagem Python
*   **Por que Python:** Sintaxe limpa, legível, próxima da linguagem humana e ideal para o aprendizado de iniciantes.
*   **Estruturas Condicionais:** Tomada de decisões no código usando as diretivas `if`, `elif` e `else`.
*   **Estruturas de Repetição:** Criação de loops para automação de tarefas usando os comandos `while` e `for`.
*   **Estruturas de Dados Básicas:** Organização de coleções de dados utilizando Listas (`[]`), Tuplas (`()`) e Dicionários (`{}`).
*   **Funções:** Modularização de código, reaproveitamento de blocos lógicos e passagem de parâmetros.

### Exemplos Práticos de Código

#### 1. Condicional Simples (IF/ELSE)
```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

#### 2. Loop com Contagem (FOR)
```python
# Exibe a tabuada do número 5
for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")
```

---

## 🐙 Git e GitHub (Controle de Versão e Portfólio)
*   **O que é o Git:** Sistema de controle de versão distribuído para rastrear alterações no código-fonte localmente.
*   **O que é o GitHub:** Plataforma em nuvem que hospeda repositórios Git, permitindo colaboração e compartilhamento de projetos.
*   **Importância para o Estudante:** Construção de portfólio técnico desde o primeiro dia de aula e histórico de evolução do aprendizado.

### Fluxo de Trabalho Local (Principais Comandos Git)
*   `git init`: Inicializa um repositório Git em uma pasta local do seu computador.
*   `git add .`: Prepara todos os arquivos modificados ou novos para o próximo salvamento (Stage).
*   `git commit -m "mensagem"`: Grava as alterações localmente com uma mensagem descritiva (Snapshot).
*   `git status`: Verifica o estado atual dos seus arquivos (quais foram modificados ou salvos).

### Integração com o GitHub (Fluxo Remoto)
*   `git remote add origin <url-do-repositorio>`: Conecta a sua pasta local ao seu repositório criado na nuvem do GitHub.
*   `git branch -M main`: Define o nome da ramificação principal do projeto como `main`.
*   `git push -u origin main`: Envia o código salvo do seu computador para o servidor do GitHub.
*   `git pull`: Atualiza o seu computador local com as alterações feitas diretamente no GitHub.

---

## 🚀 Boas Práticas de Organização
*   **Padrão de Nomenclatura:** Uso de *snake_case* para nomes de variáveis e arquivos em Python (ex: `calculo_media.py`).
*   **Mensagens de Commit:** Escrever mensagens claras e fáceis de entender (ex: `git commit -m "Adiciona exercicio da tabuada"`).
*   **Arquivo README.md:** Criar uma página inicial para cada repositório do GitHub explicando o objetivo do projeto e como rodar o código.
