# problema
# a loja so fecha se acabar o estoque
# o estoque inicial deve ser inserido pelo administrador
# vendendo somente de 3 em 3
# compra de 10 em 10

# ex: estoque: 1
# vendendo... estoque: -2
# reabastece... estoque: 8
# vendendo... estoque: 5
# vendendo... estoque: 2
# vendendo... estoque: -1
# reabastece... estoque: 9
# vendendo... estoque: 6
# vendendo... estoque: 3
# vendendo... estoque: 0

# o estoque inicial deve ser inserido pelo administrador
estoque = int(input('Estoque inicial: '))

# a loja so fecha se acabar o estoque
while estoque != 0:
  if estoque > 0:
    # venda
    print(f'vendendo... novo estoque: {estoque}')
    estoque -= 3
  else:
    # reabastece
    print(f'reabastecendo... novo estoque: {estoque}')
    estoque += 10

print()
print('fechou a loja')

