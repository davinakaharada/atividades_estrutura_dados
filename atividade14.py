# 14. Calcular o Quadrado de Cada Elemento
# Enunciado: Crie uma função que retorne uma nova lista com o quadrado de cada
# elemento da lista original.

lista = [10,20,30,40,50]

def calcular_quadrado():
    global lista
    for indice,item in enumerate(lista):
        lista[indice] = lista[indice] ** 2
    return lista
        
print(calcular_quadrado())
