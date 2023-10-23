# estrutura for

andares = 20

for andar in range (1, andares, 1):
  if andar != 13:
    print("Andar", andar)


#estrutura while

andarAtual = 1
andarFinal = 20
andarProibido = 13

while (andarAtual <= andarFinal):
    if (andarAtual != andarProibido):
      print("Andar", andarAtual)
    andarAtual = andarAtual + 1


#estrutura while em ordem decrescente

andarAtual = 20
andarFinal = 1
andarProibido = 13

while (andarAtual >= andarFinal):
    if (andarAtual != andarProibido):
        print("Andar", andarAtual)
    andarAtual = andarAtual - 1
