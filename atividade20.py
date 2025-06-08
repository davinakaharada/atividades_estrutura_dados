print("--- Atividade 20: Matriz 3x3 Formatada ---")
matriz = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        while True:
            try:
                elemento = int(input(f"Elemento [{i}][{j}]: "))
                linha.append(elemento)
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")
    matriz.append(linha)

print("\nMatriz formatada:")
for linha in matriz:
    print(f"[{' '.join(map(str, linha))}]")
print("-" * 60)