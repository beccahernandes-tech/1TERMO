# Sistemas Operacionais: Windows, Linux e iOS

## 📌 Conceitos Fundamentais de SO
*   **Gerenciamento de Processos:** Criação, escalonamento, sincronização e finalização de processos e threads.
*   **Gerenciamento de Memória:** Memória virtual, paginação, segmentação e alocação de RAM.
*   **Sistemas de Arquivos:** Organização, armazenamento, permissões e recuperação de dados em disco.
*   **Gerenciamento de Dispositivos (I/O):** Drivers de comunicação, interrupções e buffers de entrada/saída.

---

## 🪟 Microsoft Windows (Arquitetura Comercial e Desktop)
*   **Núcleo (Kernel):** Arquitetura híbrida (NT Kernel) que combina elementos de sistemas monolíticos e micronúcleos.
*   **Sistema de Arquivos Padrão:** **NTFS** (com suporte a journaling e permissões avançadas) e **FAT32/exFAT** para mídias removíveis.
*   **Gerenciamento de Processos:** Baseado em threads com escalonamento por prioridade dinâmica preemptiva.
*   **Interface e API:** API nativa Win32/Win64 e subsistema gráfico integrado ao modo kernel para maior desempenho.
*   **Subsistemas Adicionais:** **WSL (Windows Subsystem for Linux)**, que permite rodar binários Linux nativamente dentro do Windows.

---

## 🐧 Linux (Arquitetura de Código Aberto e Servidores)
*   **Núcleo (Kernel):** Monolítico puro, altamente modular (módulos carregáveis dinamicamente em tempo de execução).
*   **Sistema de Arquivos Padrão:** Família **EXT** (EXT4), além de suporte nativo a **Btrfs** e **XFS**.
*   **Gerenciamento de Processos:** Utiliza o escalonador *Completely Fair Scheduler* (CFS), focado em eficiência e divisão justa de CPU.
*   **Segurança e Permissões:** Modelo rigoroso baseado em usuários, grupos e permissões lógicas de leitura, escrita e execução (rwx).
*   **Estrutura de Diretórios:** Padronizada pelo FHS (*Filesystem Hierarchy Standard*), onde tudo é tratado como arquivo (ex: `/dev`, `/etc`, `/proc`).

---

## 🍏 Apple iOS (Arquitetura Mobile e Restrita)
*   **Núcleo (Kernel):** Baseado no kernel **XNU**, um micronúcleo híbrido derivado do Mach e componentes do FreeBSD (Unix).
*   **Sistema de Arquivos Padrão:** **APFS (Apple File System)**, otimizado para armazenamento Flash/SSD, com forte foco em criptografia.
*   **Gerenciamento de Processos:** Foco extremo em economia de energia; suspensão agressiva de processos em segundo plano (*Backgrounding*).
*   **Segurança (Sandbox):** Cada aplicativo roda isolado em seu próprio contêiner lógico, sem acesso direto aos arquivos de outros apps ou do sistema.
*   **Camadas de Software:** Dividido em camadas estruturadas: *Core OS*, *Core Services*, *Media Layer* e *Cocoa Touch* (Interface).

---

## 📊 Tabela Comparativa de Arquiteturas


| Característica | Microsoft Windows | Linux | Apple iOS |
| :--- | :--- | :--- | :--- |
| **Tipo de Kernel** | Híbrido (NT) | Monolítico Modular | Híbrido (XNU / Darwin) |
| **Código-Fonte** | Proprietário / Fechado | Código Aberto (GPL) | Proprietário / Fechado |
| **Padrão de Arquivos** | NTFS | EXT4 | APFS |
| **Interface Padrão** | Gráfica (GUI) integrada | Linha de Comando (CLI) / GUI | Toque na tela (Cocoa Touch) |
| **Foco de Mercado** | Desktops e Corporativo | Servidores, IoT e Supercomputadores | Dispositivos Móveis (iPhone) |
