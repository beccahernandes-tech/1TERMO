# Engenharia e Levantamento de Requisitos

## 📌 Conteúdo de Aula
*   **Introdução à Engenharia de Requisitos:** Ciclo de vida dos requisitos, importância do alinhamento com o negócio e custos de correção tardia.
*   **Elicitação de Requisitos:** Técnicas para descobrir, extrair e entender as necessidades reais das partes interessadas (stakeholders).
*   **Análise e Negociação:** Resolução de conflitos de interesses, priorização de escopo e viabilidade técnica/financeira.
*   **Especificação de Requisitos:** Técnicas de documentação formal e informal (Histórias de Usuário, Casos de Uso e Documentos de Requisitos).
*   **Validação e Gestão:** Homologação com o cliente, garantia de qualidade, rastreabilidade e controle de mudanças no escopo (Scope Creep).

---

## 📋 Requisitos Funcionais e Não Funcionais

### Requisitos Funcionais (O que o sistema deve fazer)
*   **Ações e Comportamentos:** Declarações das funções que o software deve executar quando acionado.
*   **Regras de Negócio:** Cálculos, validações e fluxos específicos (ex: "O sistema deve calcular o desconto de 10% para compras acima de R$ 500").
*   **Exemplos:**
    *   O sistema deve permitir que o usuário recupere a senha via e-mail.
    *   O sistema deve emitir uma nota fiscal eletrônica após a confirmação do pagamento.

### Requisitos Não Funcionais (Como o sistema deve operar)
*   **Atributos de Qualidade:** Restrições sobre os serviços ou funções oferecidos pelo sistema.
*   **Categorias Principais:**
    *   **Desempenho:** O tempo de carregamento da página inicial não deve passar de 2 segundos.
    *   **Segurança:** Todas as senhas de usuários guardadas no banco de dados devem ser criptografadas usando SHA-256.
    *   **Disponibilidade:** O sistema deve ficar ativo 99,9% do tempo (SLA).
    *   **Usabilidade:** A interface deve ser adaptável para dispositivos móveis (design responsivo).

---

## 📊 Diagramas de Modelagem
*   **Diagrama de Casos de Uso (UML):** Visão geral dos atores do sistema e das principais funcionalidades que eles acessam.
*   **Diagrama de Atividades (UML):** Mapeamento do fluxo de trabalho e processos de negócio de ponta a ponta.
*   **Diagrama de Classes / Entidade-Relacionamento:** Modelagem conceitual dos dados que o sistema precisará gerenciar e suas relações.
*   **Mapeamento de Processos (BPMN):** Desenho técnico dos processos atuais do cliente (*As-Is*) e do processo futuro proposto (*To-Be*).

---

## 💡 Técnicas de Elicitação e Design

### Brainstorm (Tempestade de Ideias)
*   **Objetivo:** Sessões colaborativas com o time de desenvolvimento e stakeholders para gerar novas ideias e soluções sem julgamentos iniciais.
*   **Técnicas de Afunilamento:** Uso de votação silenciosa ou Matriz de Priorização (Esforço vs. Valor) para selecionar as melhores ideias.

### Entrevistas
*   **Estruturação:** Podem ser fechadas (perguntas específicas), abertas (conversas livres) ou semiestruturadas (roteiro guia flexível).
*   **Boas Práticas:** Ouvir ativamente o usuário, focar na dor real e evitar perguntas indutivas que guiem a resposta do entrevistado.

### Prototipagem
*   **Baixa Fidelidade:** Desenhos em papel (*sketches*) ou wireframes simples para validar fluxos lógicos de tela rapidamente com o cliente.
*   **Alta Fidelidade:** Protótipos navegáveis (usando Figma ou Adobe XD) para testar a experiência do usuário e coletar feedback visual refinado antes de codificar.

---

## 📝 Relatorios Técnicos (Documentação)
1.  **Documento de Especificação de Requisitos de Software (SRS):** O padrão clássico (baseado na IEEE 830) para detalhar todos os requisitos do projeto.
2.  **Product Backlog / Histórias de Usuário:** Estrutura ágil usada para documentar demandas no formato: *"Como um [ator], eu quero [funcionalidade] para [valor de negócio]"*, acompanhada dos Critérios de Aceite.
3.  **Matriz de Rastreabilidade:** Tabela que conecta cada requisito à sua origem (quem pediu), ao código desenvolvido e ao caso de teste gerado, garantindo cobertura total do escopo.
