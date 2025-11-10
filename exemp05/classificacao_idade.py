"""
Módulo para classificar uma pessoa em categorias etárias usando `if`/`elif`/`else`.
"""

def executar():
    """Executa o mini-caso de classificação por faixa etária."""
    try:
        # Pede ao usuário para digitar a idade e tenta converter para um número inteiro
        idade = int(input("Digite a idade: "))
    except ValueError:
        # Se o usuário digitar algo que não seja um número inteiro, exibe uma mensagem de erro
        print("Entrada inválida. Por favor, insira um número inteiro.")
        # Interrompe a execução da função se a entrada for inválida
        return

    # Inicia a verificação da faixa etária usando uma estrutura if/elif/else
    if idade < 12:
        # Se a idade for menor que 12, classifica como "infantil"
        print("Categoria: infantil")
    elif idade <= 17:
        # Se a idade não for menor que 12, mas for menor ou igual a 17, classifica como "juvenil"
        print("Categoria: juvenil")
    elif idade < 65:
        # Se a idade não se encaixar nas categorias anteriores, mas for menor que 65, classifica como "adulto"
        print("Categoria: adulto")
    else:
        # Se nenhuma das condições anteriores for atendida (ou seja, idade >= 65), classifica como "sênior"
        print("Categoria: sênior")

# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    executar()
