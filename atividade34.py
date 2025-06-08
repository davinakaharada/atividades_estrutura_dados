print("--- Atividade 34: Tratar Erros de Entrada (Não Numéricos) ---")
while True:
    try:
        numero = float(input("Digite um número: "))
        print(f"Você digitou o número: {numero}")
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um valor numérico.")
print("-" * 60)