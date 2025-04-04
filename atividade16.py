# 16. Remover Duplicados
# Enunciado: Crie uma função que receba uma lista e retorne uma nova lista com os
# elementos duplicados removidos, mantendo a ordem original.

lista = [1,1,3,4,1,3,1]

def remove_duplicados():
    nova_lista = []
    nova_lista.append(lista[0])
    for a in lista:
        for b in nova_lista:
            if a == b:
                item_igual = True
                
        if item_igual == False: nova_lista.append(a)
        item_igual = False
            
    return nova_lista

print(remove_duplicados())
        