from datetime import datetime

print("--- Atividade 26: Dia da Semana ---")
while True:
    data_str = input("Digite uma data (dd/mm/aaaa): ")
    try:
        data_obj = datetime.strptime(data_str, "%d/%m/%Y")
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        print(f"O dia da semana é: {dias_semana[data_obj.weekday()]}")
        break
    except ValueError:
        print("Formato de data inválido ou data inexistente. Use dd/mm/aaaa.")
print("-" * 60)