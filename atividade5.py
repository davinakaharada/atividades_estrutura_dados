# 5. Exclusão de Elemento (sem usar remove)
# Enunciado: Crie uma função que remova a primeira ocorrência de um elemento de
# uma lista sem utilizar o método remove

def remove_numero(lista, numero_busca):
    for indice, numero in enumerate(lista):
        if(numero == numero_busca):
            return lista[:indice] + lista[indice+1]
        return lista
        

lista = [1,2,3,4,5,6,7]
numero_busca = 3

print(remove_numero(lista, numero_busca))