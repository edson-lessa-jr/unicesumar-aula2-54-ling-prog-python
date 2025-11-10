"""
Módulo para demonstrar o uso de um `if-else`.
Lê um número inteiro e calcula a raiz quadrada se o número for par,
ou informa que é ímpar caso contrário.
"""

# Importa o módulo math para usar a função de raiz quadrada (sqrt)
import math

def executar():
    """Executa a demonstração do `if-else` (par vs ímpar)."""
    try:
        # Pede ao usuário para digitar um número e tenta converter para inteiro
        num = int(input("Digite um número inteiro: "))
    except ValueError:
        # Se o usuário digitar algo que não seja um número inteiro, exibe uma mensagem de erro
        print("Entrada inválida. Por favor, insira um número inteiro.")
        # Interrompe a execução da função se a entrada for inválida
        return

    # Verifica se o número é par. O operador % retorna o resto da divisão.
    # Se o resto da divisão por 2 for 0, o número é par.
    if num % 2 == 0:
        # Se o número for par, calcula a raiz quadrada
        raiz = math.sqrt(num)
        # Imprime uma mensagem formatada mostrando o resultado
        print(f"O número {num} é par. A raiz quadrada de {num} é {raiz:.2f}.")
    else:
        # Se a condição do if for falsa (ou seja, o número é ímpar), este bloco é executado
        print(f"O número {num} é ímpar. Neste exemplo não iremos calcular a raiz.")

# A boa prática de verificar se o script é o principal não está aqui,
# mas se estivesse, chamaria a função executar().
# Exemplo:
if __name__ == "__main__":
    executar()
