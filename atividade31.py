print("--- Atividade 31: Ler Arquivo ---")
nome_arquivo = "texto.txt"
try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(f"Conteúdo do arquivo '{nome_arquivo}':")
        print(conteudo)
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado. Por favor, execute a Atividade 30 primeiro.")
except IOError as e:
    print(f"Erro ao ler o arquivo: {e}")
print("-" * 60)