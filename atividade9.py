# 9. Soma de Elementos
# Enunciado: Crie uma função que receba uma lista e retorne a soma de todos os seus
# elementos.

def soma_itens(lista):
    soma_numero = 0
    for numero in lista:
        soma_numero = soma_numero + numero
    return soma_numero

lista = [10,7,8,20]

print(soma_itens(lista))