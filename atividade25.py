import math

print("--- Atividade 25: Raiz Quadrada ---")
while True:
    try:
        numero = float(input("Digite um número para calcular a raiz quadrada: "))
        if numero >= 0:
            print(f"A raiz quadrada de {numero} é: {math.sqrt(numero)}")
            break
        else:
            print("Não é possível calcular a raiz quadrada de um número negativo.")
    except ValueError:
        print("Entrada inválida. Digite um número.")
print("-" * 60)