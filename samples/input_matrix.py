n_linhas, n_colunas = input().split()
n_linhas, n_colunas = int(n_linhas), int(n_colunas)

matrix = []

for _ in range(n_linhas):
  # leia uma linha e separe em vetor
  vetor = input().split()
  
  # converta cada elemento para inteiro
  for i in range(n_colunas):
    vetor[i] = int(vetor[i])
  
  # adicione o vetor na matriz(vetor de vetores)
  matrix.append(vetor)
  
print('---------------------')

for i in range(n_linhas):
  
  for j in range(n_colunas):
    # imprime os elementos
    print(matrix[i][j], end=' ')
    
  print() # pula pra proxima linha

print('---------------------')

for i in range(n_linhas):
  print(matrix[i][i], end=' ')
  
print('---------------------')

for i in range(n_linhas):
  print(matrix[i][n_linhas - i - 1], end=' ')

# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]

# (i+1) + (j-1) = 
# i + j = n - 1
# j = n - i - 1