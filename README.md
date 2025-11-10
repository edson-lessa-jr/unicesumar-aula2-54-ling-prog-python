# Aula 2 - Estruturas Condicionais: Tomada de Decisão
### Disciplina: Linguagem de Programação Python
### Professor: Edson Orivaldo Lessa Junior
### Ciclo: 54

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido como material de apoio para a **Aula 2**, com o objetivo de demonstrar, através de exemplos práticos e interativos, o funcionamento das **estruturas condicionais** em Python. Aqui, você encontrará códigos que ilustram desde o `if` mais simples até combinações com `elif` e `else` para resolver problemas do dia a dia.

## 🤔 O que são Estruturas Condicionais?

Na programação, nem sempre um código é executado de forma linear. Muitas vezes, precisamos que o programa tome decisões e siga caminhos diferentes com base em certas condições. É para isso que servem as estruturas condicionais!

- **`if` (Se):** Executa um bloco de código **se** uma condição for verdadeira.
- **`else` (Senão):** Executa um bloco de código alternativo **se** a condição do `if` for falsa.
- **`elif` (Senão Se):** Permite verificar múltiplas condições em sequência. É uma contração de "else if".

Com elas, podemos criar programas muito mais inteligentes e dinâmicos.

## 🚀 Exemplos Práticos no Projeto

Este repositório contém vários exemplos, cada um em seu próprio arquivo `.py` dentro de uma pasta numerada. O arquivo `main.py` na raiz do projeto oferece um menu para você executar cada um deles facilmente.

| Exemplo | Módulo | O que ele demonstra? |
| :--- | :--- | :--- |
| **1** | `exemp01/exemplo_if_simples.py` | **`if` simples:** O código só executa uma ação (calcular a raiz quadrada) se a condição (o número ser par) for atendida. Caso contrário, nada acontece. |
| **2** | `exemp02/exemplo_if_else.py` | **`if-else`:** Apresenta dois caminhos. Se o número é par, calcula a raiz; senão, informa que o número é ímpar. Um dos dois blocos sempre será executado. |
| **3** | `exemp03/menu_aritmetico.py` | **`if-elif-else`:** Perfeito para menus com várias opções. O código testa cada `elif` em ordem até encontrar uma condição verdadeira ou chegar ao `else` final (opção inválida). |
| **4** | `exemp04/divisao_segura.py` | **`if` aninhado:** Mostra como uma verificação pode ser feita dentro de outra. Aqui, primeiro verificamos se o divisor é zero antes de tentar a divisão. |
| **5** | `exemp05/classificacao_idade.py` | **Mini-Caso Prático:** Usa `elif` para classificar uma pessoa em faixas etárias (infantil, juvenil, adulto, sênior). |
| **6** | `exemp06/classificacao_nota.py` | **Mini-Caso Prático:** Classifica a situação de um aluno (aprovado, recuperação, reprovado) com base em sua média final. |

## ⚙️ Como Executar o Projeto

Você pode executar os exemplos de duas maneiras:

### 1. Usando o Menu Principal (Recomendado)

Esta é a forma mais fácil de explorar todos os exemplos.

1.  Abra seu terminal ou console.
2.  Navegue até a pasta raiz do projeto.
3.  Execute o script `main.py`:
    ```bash
    python main.py
    ```
4.  Um menu aparecerá. Digite o número da demonstração que deseja ver e pressione Enter.

### 2. Executando um Exemplo Individualmente

Cada arquivo de exemplo também pode ser executado de forma independente.

1.  Navegue até a pasta do exemplo desejado (ex: `exemp01/`).
2.  Execute o arquivo Python diretamente:
    ```bash
    python exemplo_if_simples.py
    ```

---
