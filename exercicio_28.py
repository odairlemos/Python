#Variables
lista = []
contador = 5
media = 0
ideal = 0

#Main Code
for n in range(contador):
    lista.append(int(input("Digite um número para adicioná-lo à lista: ")))

media = (sum(lista)/5)
print("Media = ", media)

lista.sort()
print("Lista ordenada: ", lista)

for i in lista:
    if lista[i] <= media:
            ideal = i

print("O valor mais proximo da media e: ", ideal)