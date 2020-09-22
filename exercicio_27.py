class Quot:

    def traduzir_quot (self, codigo):

        secreto = {0: " ",1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",7: "g",8: "h",9: "i",10: "j",11: "k",12: "l",13: "m",14: "n",15: "o",16: "p",17: "q",18: "r",19: "s",
                   20: "t",21: "u",22: "v",23: "x",24: "x",25: "y",26: "z"}
        frase = []

        for a in codigo:
            for b, c in secreto.items():
                if codigo[a] == secreto[b]:
                    frase.append(secreto[b])
                else:
                    print("Valor {0} nao encontrado, prosseguindo...".format(codigo[a]))
        print(frase)
#Variables
validar = 0
mensagem = []

#Main Code
while validar != 999:
    for n in range(3):
        mensagem.append(int(input("Digite um número para adicioná-lo à lista 1: ")))
        validar = int(input("Digite '999' para SAIR e criptografar:"))
        if validar == 999:
            break

envia_comando = Quot()
envia_comando.traduzir_quot(mensagem)
