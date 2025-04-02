# 4. Pesquisa Linear (retornar índice)
# Enunciado: Crie uma função que faça pesquisa linear em uma lista e retorne o índice
# do elemento se encontrado ou -1 se não estiver presente.
def busca_notas(notas,nota_aluno):
    for indice, nota in enumerate(notas):
        if (nota == nota_aluno):
            status = indice
            break
        else:
            x = -1
    return status
notas = [10,7,8,6]
nota_aluno = 7

print(busca_notas(notas, nota_aluno))    