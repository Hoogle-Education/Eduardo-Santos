numeros = input().split()
quantidade = len(numeros)

# convertendo cada numero para sua versao inteira
for pos in range(0, quantidade):
  numeros[pos] = int(numeros[pos])
  
print(sum(numeros))