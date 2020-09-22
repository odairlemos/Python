#Variables
homem1 =int(input("Insira a idade do primeiro homem: "))
homem2 =int(input("Insira a idade do primeiro homem: "))
mulher1 =int(input("Insira a idade da primeira mulher: "))
mulher2 =int(input("Insira a idade da segunda mulher: "))
homem_novo = 0
homem_velho = 0
mulher_nova = 0
mulher_velha = 0

#Main Code
if homem1 > homem2:
    homem_velho = homem1
    homem_novo = homem2
else:
    homem_velho = homem2
    homem_novo = homem1

if mulher1 > mulher2:
    mulher_velha = mulher1
    mulher_nova = mulher2
else:
    mulher_velha = mulher2
    mulher_nova = mulher1

print("A soma das idades do homem mais velho com a mulher mais nova e: ", homem_velho + mulher_nova)
print("O produto das idades do homem mais novo com a mulher mais velha e: ", homem_novo * mulher_velha)