"""
Módulo para demonstrar o uso de `elif` através de um menu aritmético.
O usuário escolhe uma operação matemática e os números envolvidos.
"""

def executar():
    """Executa a demonstração do menu aritmético com `elif`."""
    try:
        # Pede ao usuário para digitar dois números e tenta convertê-los para float (números com casas decimais)
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        # Se o usuário digitar algo que não seja um número válido, exibe uma mensagem de erro
        print("Entrada inválida. Use números válidos.")
        # Interrompe a execução da função se a entrada for inválida
        return

    # Exibe o menu de opções para o usuário
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Lê a opção do usuário e remove espaços em branco do início e do fim com .strip()
    opcao = input("Opção: ").strip()

    # Verifica qual opção o usuário escolheu usando uma estrutura if/elif/else
    if opcao == '1':
        # Se a opção for '1', calcula e exibe a soma
        print(f"Resultado da soma: {num1 + num2}")
    elif opcao == '2':
        # Se a opção for '2', calcula e exibe a subtração
        print(f"Resultado da subtração: {num1 - num2}")
    elif opcao == '3':
        # Se a opção for '3', calcula e exibe a multiplicação
        print(f"Resultado da multiplicação: {num1 * num2}")
    elif opcao == '4':
        # Se a opção for '4', verifica se o segundo número é zero
        if num2 == 0:
            # Se for zero, exibe uma mensagem de erro, pois não é possível dividir por zero
            print("Não é possível dividir por zero!")
        else:
            # Caso contrário, calcula e exibe a divisão
            print(f"Resultado da divisão: {num1 / num2}")
    else:
        # Se o usuário digitar qualquer outra coisa, informa que a opção é inválida
        print("Opção inválida! Por favor, escolha entre 1 e 4.")

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    executar()
