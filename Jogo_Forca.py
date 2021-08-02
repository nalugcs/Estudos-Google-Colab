import random

def jogar():
  palavra_secreta = escolhe_palavra_secreta()
  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
  
  print("Palavra Secreta: {}".format(letras_acertadas), end="\n\n")
  
  enforcou = False
  acertou = False
  erros = 0
 
  while (not enforcou and not acertou):
    chute = input("Qual letra? ")
    chute = chute.lower()
    chute = chute.strip()

    if (chute in palavra_secreta):
      marca_chute_correto(chute, palavra_secreta, letras_acertadas)
    else:
        erros += 1

    enforcou = erros == 6
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)
    print("jogando...", end="\n\n")

  if (acertou):
    print("Você ganhou!")
  else:
    print("Você perdeu!")


def escolhe_palavra_secreta():
  arquivo = open("palavras.txt","r")
  palavras = []

  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

  arquivo.close()

  #escolher aleatório uma palavra de um arquivo
  numero = random.randrange(0,len(palavras))
  palavra_secreta = palavras[numero]

  return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
  palavra_secreta = escolhe_palavra_secreta()
  return ["_" for letra in palavra_secreta]


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
  index = 0
  for letra in palavra_secreta:
    if (chute == letra):
      letras_acertadas[index] = letra
    index += 1

if (__name__ == "__main__"):
  jogar()
