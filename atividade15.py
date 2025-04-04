# 15. Verificar Presença de Elemento
# Enunciado: Crie uma função que verifique se um elemento está presente em uma lista,
# retornando True ou False.


lista = ['a','b','c','d','e']
encontre = 's'
def presenca_elemento():
    for i in lista:
        if i == encontre: return True
        return False

print(presenca_elemento())

    