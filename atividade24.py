print("--- Atividade 24: Soma dos Ímpares em uma Lista ---")
def soma_impares_lista(lista_numeros):
    soma = 0
    for num in lista_numeros:
        if num % 2 != 0:
            soma += num
    return soma

while True:
    entrada = input("Digite números separados por espaço (ex: 1 2 3): ")
    try:
        numeros = [int(x) for x in entrada.split()]
        print(f"A soma dos números ímpares é: {soma_impares_lista(numeros)}")
        break
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números inteiros.")
print("-" * 60)