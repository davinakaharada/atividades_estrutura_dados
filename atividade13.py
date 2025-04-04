# 13. Filtrar Elementos Pares
# Enunciado: Crie uma função que retorne uma nova lista contendo apenas os números
# pares de uma lista dada.
lista = [1,2,3,4,5,6,7,8,9,10]

def elemento_par():
    lista_par=[]
    for par in lista:
        resto = par%2
        if resto == 0:
            lista_par.append(par)
    return lista_par

resposta = elemento_par()

print(resposta)