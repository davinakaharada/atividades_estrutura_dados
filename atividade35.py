print("--- Atividade 35: Tratar Erro de Entrada Não Numérica e Exibir Quadrado ---")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"O quadrado de {numero} é: {numero ** 2}")
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
print("-" * 60)