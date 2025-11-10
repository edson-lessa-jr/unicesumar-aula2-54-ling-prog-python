"""
Módulo para demonstrar como impedir a divisão por zero usando verificação aninhada.
"""

def executar():
    """Executa a demonstração da divisão segura."""
    try:
        # Pede ao usuário para digitar o numerador e o denominador, e tenta convertê-los para float
        numerador = float(input("Digite o numerador: "))
        denominador = float(input("Digite o denominador: "))
    except ValueError:
        # Se a entrada não for um número válido, exibe uma mensagem de erro e encerra a função
        print("Entrada inválida. Use números válidos.")
        return

    # Verifica se o denominador é diferente de zero
    if denominador != 0:
        # Se o denominador não for zero, realiza a divisão e imprime o resultado
        print(f"Resultado da divisão: {numerador / denominador}")
    else:
        # Se o denominador for zero, informa ao usuário que a operação não é possível
        print("Divisor igual a zero. Não é possível realizar a operação!")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    executar()
