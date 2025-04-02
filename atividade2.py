# 2. Inserção Múltipla
# Enunciado: Crie uma lista vazia e use append para adicionar os números 5, 3, 8, 6 e 1.
# Imprima a lista resultante.

def add_lista(lista, numeros):
    for numero in numeros:
        lista.append(numero)
    return lista

numeros ='53861'
lista = []

resultado = add_lista(lista,numeros)
print(resultado)
