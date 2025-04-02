# 8. Inverter Lista (sem usar reverse)
# Enunciado: Crie uma função que inverta uma lista sem usar o método reverse.

nova_lista = []

def ao_contrario(lista):
    global nova_lista
    tamanho_lista = len(lista)
    while tamanho_lista > 0:
        tamanho_lista = tamanho_lista - 1
        nova_lista.append(lista[tamanho_lista])
    return nova_lista

lista = ['a','b','c','d','e','f','g']
print(ao_contrario(lista))
