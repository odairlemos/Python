LIMITE = 10


class Informando:

    def manupula_numeros(self):
        valor = 0
        media = 0
        contador = 0
        soma = 0
        maior = 0
        menor = 9999

        while contador < LIMITE:

            valor = int(input("Insira o numero: "))
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
            soma += valor
            contador += 1

        media = soma / LIMITE

        print("Resultados Obtidos:\n")
        print("\nO MAIOR valor e: {0}".format(maior))
        print("\nO MENOR valor e: {0}".format(menor))
        print("\nA SOMA dos valores e: {0}".format(soma))
        print("\nA MEDIA dos valores e: {0}".format(media))


verifica = Informando()
verifica.manupula_numeros()