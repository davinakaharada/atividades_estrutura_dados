print("--- Atividade 21: Soma de Duas Matrizes 2x2 ---")

matriz1 = []
print("Digite os elementos da primeira matriz (2x2):")
for i in range(2):
    linha = []
    for j in range(2):
        while True:
            try:
                elemento = int(input(f"Elemento [{i}][{j}] da primeira matriz: "))
                linha.append(elemento)
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")
    matriz1.append(linha)

matriz2 = []
print("Digite os elementos da segunda matriz (2x2):")
for i in range(2):
    linha = []
    for j in range(2):
        while True:
            try:
                elemento = int(input(f"Elemento [{i}][{j}] da segunda matriz: "))
                linha.append(elemento)
                break
            except ValueError:
                print("Por favor, digite um número inteiro.")
    matriz2.append(linha)

matriz_soma = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]

print("\nMatriz resultante da soma:")
for linha in matriz_soma:
    print(f"[{' '.join(map(str, linha))}]")
print("-" * 60)