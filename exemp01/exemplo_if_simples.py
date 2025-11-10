"""
Módulo para demonstrar o uso de um `if` simples.
Lê um número inteiro e calcula a raiz quadrada se o número for par.
"""

# Importa o módulo math para usar a função de raiz quadrada (sqrt)
import math

def executar():
    """Executa a demonstração do `if` simples (par e raiz)."""
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
        # Calcula a raiz quadrada do número
        raiz = math.sqrt(num)
        # Imprime uma mensagem formatada mostrando o resultado
        print(f"O número {num} é par. A raiz quadrada de {num} é {raiz:.2f}.")
    
    # Esta linha é executada sempre, independentemente da condição do if
    print("Quando ímpar, nada é feito")

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    executar()
