import random

print("--- Atividade 27: Número Aleatório (1 até N) ---")
while True:
    try:
        numero_max = int(input("Digite um número inteiro: "))
        if numero_max >= 1:
            print(f"Um valor aleatório entre 1 e {numero_max} é: {random.randint(1, numero_max)}")
            break
        else:
            print("Por favor, digite um número maior ou igual a 1.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
print("-" * 60)