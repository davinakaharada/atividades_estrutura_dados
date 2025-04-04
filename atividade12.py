# 12. Contar Ocorrências de um Elemento
# Enunciado: Crie uma função que conte quantas vezes um dado elemento aparece em
# uma lista
lista = [10,9,10,9,10] # escopo global
elemento = 10 # escopo global
def conta_elementos(lista, elemento):
    conta_elemento = 0 # escopo local
    for item in lista:
        if item == elemento:
            conta_elemento +=1
    return conta_elemento


resposta = conta_elementos(lista,elemento)
print(resposta)