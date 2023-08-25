l = int(input())
operation = input()

matrix = []

# entrada da matriz
for i in range(12):
  vetor = []
  
  for j in range(12):
    valor = float(input())
    vetor.append(valor)
    
  matrix.append(vetor)

# calculo da soma
soma = 0

for j in range(12):
  soma += matrix[l][j]

# decisao da saida  
if operation == 'S':
  print(f'{soma:.1f}')
else:
  media = soma / 12
  print(f'{media:.1f}')