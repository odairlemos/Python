#Variables
nomes = []

#Main Code
for i in range(5):
    nome = input("Insira o nome: ")
    nomes.append(nome)
print("\nImpressao do conjunto de nomes:\n")
for i in range(5):
    print(nomes[i])