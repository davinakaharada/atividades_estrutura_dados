print("--- Atividade 33: Tratar Erro de Divisão por Zero ---")
while True:
    try:
        numero = float(input("Digite um número para dividir 100 por ele: "))
        resultado = 100 / numero
        print(f"100 dividido por {numero} é: {resultado}")
        break
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero. Por favor, digite outro número.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
print("-" * 60)