# 6. Inserção em Lista Ordenada
# Enunciado: Crie uma função que insira um elemento em uma lista ordenada,
# mantendo a ordem sem usar sort.

lista = [3,5,2,1,4]
numero_to_add = 6

def ordena_lista():
    lista.append(numero_to_add)
    x = 0
    while x < len(lista)-1:
        if lista[x] <= lista[x+1]:
            x += 1
        else:
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
            x = 0
            
    return lista

print(ordena_lista())    