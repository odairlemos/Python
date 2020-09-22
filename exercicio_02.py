class EscreverValor:

  def mostrar_valor (self, valor):
    if valor == 1:
      print("Um")
    elif valor == 2:
      print("Dois")
    elif valor == 3:
      print("Tres")
    elif valor == 4:
      print("Quatro")
    elif valor == 5:
      print("Cinco")
    else:
      print("Numero invalido")

mostra_numero = EscreverValor()

numero = int(input ("Insira um numero positivo e inteiro: "))

mostra_numero.mostrar_valor(numero)

