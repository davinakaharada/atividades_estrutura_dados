print("--- Atividade 32: Armazenar Contato em Arquivo ---")
nome_arquivo = "contatos.txt"
nome = input("Digite o nome do contato: ")
telefone = input("Digite o telefone do contato: ")

try:
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:  # 'a' para adicionar ao arquivo
        arquivo.write(f"Nome: {nome}, Telefone: {telefone}\n")
    print(f"Contato '{nome}' armazenado com sucesso em '{nome_arquivo}'.")
except IOError as e:
    print(f"Erro ao escrever no arquivo: {e}")
print("-" * 60)