# 3. Função de Inserção
# Enunciado: Crie uma função que receba uma lista e um valor, insira o valor usando
# append e retorne a lista atualizada.
def acrescentar(lista,numero):
    lista.append(numero)
    return lista


lista = []
numero = 15
print(acrescentar(lista,numero))

