"""
Módulo para classificar a média final de um aluno usando `if`/`elif`/`else`.
"""

def executar():
    """Executa o mini-caso de classificação de notas."""
    try:
        # Pede ao usuário para digitar a média final e tenta converter para float (número com casas decimais)
        media = float(input("Digite a média final do aluno: "))
    except ValueError:
        # Se a entrada não for um número válido, exibe uma mensagem de erro e encerra a função
        print("Entrada inválida. Use um número decimal válido.")
        return

    # Verifica a situação do aluno com base na média
    if media >= 7.0:
        # Se a média for maior ou igual a 7.0, o aluno está aprovado
        print("Resultado: aprovado")
    elif media >= 5.0:
        # Se a média não for >= 7.0, mas for maior ou igual a 5.0, o aluno está em recuperação
        print("Resultado: em recuperação")
    else:
        # Se nenhuma das condições anteriores for atendida (média < 5.0), o aluno está reprovado
        print("Resultado: reprovado")

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Chama a função principal para iniciar o programa
    executar()
