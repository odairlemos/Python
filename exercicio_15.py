#Variables
maior = 0

#Main Code
for i in range(10):
    numero = int(input("Insira um numero: "))

    if numero > maior:
        maior = numero

print("O maior valor inserido foi: ", maior)