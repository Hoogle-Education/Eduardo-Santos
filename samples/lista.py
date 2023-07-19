list = input().split()

# codigo ruim: dificil de entender, extender e mudar
size = len(list)

print(f'tamanho: {size}')

# for index in range(size):
# list[index] = int(list[index])

# range(n) = 0, 1, 2, 3, 4, ..., n-1
for index in range(size):
  list[index] = int(list[index])
  print(f'{type(list[index])} - {2+list[index]}')
  
# 1 2 3 4 5
prod = 1

for index in range(size):
  prod *= list[index]
  
# 40 37 38 32 39 31 41 36 35 31

pos_menor = 0

for pos_atual in range(size):
  valor_atual = list[pos_atual]
  valor_menor = list[pos_menor]
  
  if valor_atual <= valor_menor:
    pos_menor = pos_atual
    
print(f'o menor esta na posicao: {pos_menor}')
print(f'menor valor: {list[pos_menor]}')