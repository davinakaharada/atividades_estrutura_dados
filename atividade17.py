# 17. Inserir Elemento se Não Existir
# Enunciado: Crie uma função que insira um elemento em uma lista apenas se ele ainda
# não estiver presente.

lista = [1,2,4,5,6,7]

def inserindo_elemento(novo_elemento):
    for i in lista:
        if novo_elemento not in lista:
            lista.append(novo_elemento)
    return lista

print(inserindo_elemento(3))

##############################################################################################

lista = [20,40,50,80,90]
elemento = 100

def esta_presente():
    existe = False
    for item in lista:
        if elemento == item: existe = True
        
    if existe == False: lista.append(elemento)
    return lista
print(esta_presente())