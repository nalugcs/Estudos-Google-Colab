import random
def jogar():
  
  print("Jogo de adivinhação", end= '\n\n')
  nro_secreto = random.randrange(1,101)
  total_tentativas = 2
  rodada = 1
  while(total_tentativas >= rodada):
    print("Tentativa {} de {}".format(rodada, total_tentativas), end="\n")
    chute = input("Digite seu número: ")
    chute_numero = int(chute)
    if (chute_numero < 0):
      print("Número inserido errado!", end="\n \n")
      continue
    else:
        maior = chute_numero > nro_secreto
        menor = chute_numero < nro_secreto

        if (nro_secreto == chute_numero):
          print("Você acertou!")
          break
        else:
          if (maior):
            print("Você errou! O número é menor do que você chutou!", end="\n \n")
          elif (menor):
              print("Você errou! O número é maior do que você chutou!", end = "\n \n")
        
        rodada = rodada + 1
        
  print("Fim do Jogo! O Número era: {}".format(nro_secreto))

  if(__name__ == "__main__"):
    jogar()
