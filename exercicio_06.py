class ValidaNumero:

  def validando (self, valor):
    if valor >= 0:
      print("O valor {0} e Positivo".format(valor))
    else:
      print("O valor {0} e Negativo".format(valor))
    if valor % 2 == 0:
      print("O valor {0} e Par".format(valor))
    else:
      print("O valor {0} e Impar".format(valor))

teste = ValidaNumero()

numero = int(input ("Insira o numero: "))

teste.validando(numero)