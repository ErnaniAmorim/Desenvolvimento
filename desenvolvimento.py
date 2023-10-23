almoco_favorito = "Arroz com lasanha bolonhesa"
almoco_preco = 29.9
orcamento = 210.0
sobremesa_preco = 4.9
quantidade_pessoas = 5

total = almoco_preco * 5 + sobremesa_preco * 3
troco = orcamento - total




print("O orçamento total é de", 50*3 + 2*30)
print("O valor total é de", almoco_preco * 5 + sobremesa_preco * 3)
if (orcamento > total):
  print("Você tem orçamento para pagar a conta")
  print("Sobrou", troco, "de troco.")
else:
    print("Você terá que lavar os pratos!")