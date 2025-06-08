print("--- Atividade 22: Dobro de um Número ---")
def dobrar_numero(numero):
    return numero * 2

while True:
    try:
        num = float(input("Digite um número para dobrar: "))
        print(f"O dobro de {num} é: {dobrar_numero(num)}")
        break
    except ValueError:
        print("Entrada inválida. Digite um número.")
print("-" * 60)