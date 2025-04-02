# 6. Inserção em Lista Ordenada
# Enunciado: Crie uma função que insira um elemento em uma lista ordenada,
# mantendo a ordem sem usar sort.

# def ordena_lista(lista, novo_numero):
#     lista = lista + [novo_numero]
    
#     for numero in enumerate(lista):
#         if (lista[indice] > lista[indice+1]):
#             buffer = lista[indice+1]
#             lista[indice+1] = lista[indice]
#             lista[indice] = buffer
            

lista = [5,2,4,1,7]
novo_numero =3
indice = 0
for numero in lista:
    if lista[indice] > lista[indice+1]:
        lista[indice+1] = lista[indice]
        
print(lista)
