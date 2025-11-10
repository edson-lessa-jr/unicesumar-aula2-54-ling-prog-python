"""
Script principal do projeto de demonstração de estruturas condicionais.
Oferece um menu de opções e chama a função `executar` de cada módulo de exemplo.
"""

# Importa os módulos das demonstrações para que suas funções possam ser usadas neste script.
# Cada módulo corresponde a um exemplo específico de estrutura condicional.
from exemp02 import exemplo_if_else
from exemp03 import menu_aritmetico
from exemp04 import divisao_segura
from exemp05 import classificacao_idade
from exemp06 import classificacao_nota
from exemp01 import exemplo_if_simples


def exibir_menu():
    """Exibe o menu principal de demonstrações para o usuário."""
    print("\n=== MENU DE DEMONSTRAÇÕES ===")
    print("1 - Exemplo if simples (par e raiz)")
    print("2 - Exemplo if-else (par x ímpar)")
    print("3 - Menu aritmético (elif)")
    print("4 - Exemplo de divisão segura (if aninhado)")
    print("5 - Classificação por faixa etária (elif)")
    print("6 - Classificação de notas (elif)")
    print("0 - Sair")


def main():
    """Função principal que controla a execução das demonstrações."""
    # O loop `while True` cria um menu que se repete indefinidamente até que o usuário decida sair.
    while True:
        # Chama a função para mostrar o menu de opções.
        exibir_menu()
        # Pede ao usuário para escolher uma opção e remove espaços em branco com .strip().
        opcao = input("Escolha a demonstração que deseja executar: ").strip()

        # Usa uma estrutura if/elif/else para determinar qual demonstração executar com base na escolha do usuário.
        if opcao == '1':
            # Executa a demonstração do if simples.
            exemplo_if_simples.executar()
        elif opcao == '2':
            # Executa a demonstração do if-else.
            exemplo_if_else.executar()
        elif opcao == '3':
            # Executa o menu aritmético.
            menu_aritmetico.executar()
        elif opcao == '4':
            # Executa a demonstração da divisão segura.
            divisao_segura.executar()
        elif opcao == '5':
            # Executa a demonstração da classificação por idade.
            classificacao_idade.executar()
        elif opcao == '6':
            # Executa a demonstração da classificação de notas.
            classificacao_nota.executar()
        elif opcao == '0':
            # Se a opção for '0', exibe uma mensagem de despedida e sai do loop com `break`.
            print("Encerrando o programa. Obrigado por utilizar as demonstrações!")
            break
        else:
            # Se a opção não for nenhuma das anteriores, informa ao usuário que é inválida.
            print("Opção inválida. Por favor, tente novamente.")
        
        # Pausa a execução e espera o usuário pressionar Enter. Isso melhora a 
        # visualização, impedindo que o menu reapareça imediatamente após uma demonstração.
        input("\nPressione Enter para retornar ao menu...")


# Esta é uma construção padrão em Python.
# O código dentro deste `if` só será executado se o script for rodado diretamente.
# Ele não será executado se o `main.py` for importado por outro script.
if __name__ == "__main__":
    # Chama a função `main` para iniciar o programa.
    main()
