import random

print("--- Atividade 28: Lista de 5 Números Aleatórios ---")
numeros_aleatorios = [random.randint(1, 100) for _ in range(5)]
print("Lista de 5 números aleatórios entre 1 e 100:")
print(numeros_aleatorios)
print("-" * 60)