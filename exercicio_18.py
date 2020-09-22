class Animal:

    def Comer(self, comida):
        print("O animal esta comendo ", comida)

class Cachorro:
    Animal.Comer("Osso")

class Gato:
    Animal.Comer("Whisklas Sache")

class Cavalo:
    Animal.Comer("Milho triturado")

class AnimalTeste:

    animais = [Cachorro, Gato, Cavalo]

    for i in range(3):
        print("O que voce come:")
        print(animais[i].Comer)

