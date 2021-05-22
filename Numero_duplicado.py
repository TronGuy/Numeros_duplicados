def encontrar_numeros(*args):
    nova_lista_original = list(*args)
    nova_lista = nova_lista_original[1:]

    position = 1
    numero = 0
    for n,values in enumerate(nova_lista):
        if values == nova_lista[position]:
            numero = values
            break
        position += 1
        if position > len(nova_lista)-1:
            break
    if numero == 0:
        numero = -1
    return f'Lista:{nova_lista_original},Modificada:{nova_lista}, Retorno:{numero}'

lista_de_listas_de_inteiros = [

    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
    [4,8,8,8,5,1,10,3,1,7],
    [1,3,7,2,2,1,5,1,9,9],
    [10,2,2,1,3,5,10,5,10,1],
    [1,6,1,5,1,1,1,4,7,3],
    [1,3,7,1,10,5,9,2,5,7],
    [4,7,6,5,2,9,2,1,2,1],
    [5,3,1,8,5,7,1,8,8,7],
    [10,9,8,7,6,5,4,3,2,1]

]
#Teste com números do exercício
print(encontrar_numeros([1,2,3,3,2,1]))
print(encontrar_numeros([1,2,3,4,5,6]))

#Teste com os iteráveis
for i in lista_de_listas_de_inteiros:
    print(encontrar_numeros(i))
