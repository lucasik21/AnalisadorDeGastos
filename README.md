# Analisador de Gastos Pessoais

Um script em Python desenvolvido para o terminal que permite o cadastro, leitura e consolidação de gastos financeiros diários através de manipulação de arquivos CSV. 

## 🚀 Funcionalidades
- **Cadastro Interativo:** Inserção de novos gastos (Data, Descrição, Categoria e Valor) via terminal.
- **Consolidação Automática:** Leitura e soma automática de dados salvos em um arquivo `.csv`.
- **Relatório por Categoria:** Cálculo do total gasto segmentado por categoria e exibição do saldo geral.
- **Prevenção de Erros (Tratamento de Exceções):** Validação de inputs do usuário para evitar falhas no sistema.

## 🛠️ Tecnologias e Conceitos Aplicados
- **Python 3** (Lógica de programação, laços de repetição e funções).
- **Biblioteca `csv`** (Nativa do Python, utilizada para leitura e escrita de dados).
- **Biblioteca `os`** (Utilizada para verificação de diretórios e arquivos locais).

## Como executar o projeto

1. Certifique-se de ter o [Python](https://www.python.org/) instalado na sua máquina.
2. Clone este repositório ou baixe os arquivos para uma pasta local.
3. Abra o terminal (Prompt de Comando ou PowerShell) na pasta do projeto.
4. Execute o seguinte comando:
   ```bash
   python main.py
