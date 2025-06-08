print("--- Atividade 23: Par ou Ímpar ---")
def verificar_par_impar(numero):
    return "Par" if numero % 2 == 0 else "Ímpar"

while True:
    try:
        num = int(input("Digite um número inteiro para verificar se é par ou ímpar: "))
        print(f"O número {num} é: {verificar_par_impar(num)}")
        break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
print("-" * 60)