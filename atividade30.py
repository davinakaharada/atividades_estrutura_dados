print("--- Atividade 30: Escrever em Arquivo ---")
nome_arquivo = "texto.txt"
frase = "Python é incrível!"
try:
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(frase)
    print(f"A frase '{frase}' foi escrita no arquivo '{nome_arquivo}'.")
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")
print("-" * 60)