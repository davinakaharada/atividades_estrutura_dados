import random
import time

print("--- Atividade 29: Simulação de Lançamento de Dado ---")
print("Lançando o dado...")
time.sleep(2)  # Pausa de 2 segundos
print(f"O dado caiu no número: {random.randint(1, 6)}")
print("-" * 60)