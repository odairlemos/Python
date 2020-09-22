def muda_ordem (listagem):

    lista_nova.append(lista[2])
    lista_nova.append(lista[3])
    lista_nova.append(lista[0])
    lista_nova.append(lista[1])

    return(lista_nova)

#Variables
lista = []
lista_nova = []
contador = 4


#Main Code
for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista: ")))

muda_ordem(lista)

print(lista_nova)