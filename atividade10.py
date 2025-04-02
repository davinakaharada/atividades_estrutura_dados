# 10. Encontrar o Maior Elemento
# Enunciado: Crie uma função que encontre e retorne o maior elemento de uma lista.

def maior_valor(lista):
    
    maior_numero = 10
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

print(maior_valor([10,7,8,20]))

