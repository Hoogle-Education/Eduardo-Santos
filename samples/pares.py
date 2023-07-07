# 2, 4, 6, 8, 10 
# pares: tem o formato 2k
# par % 2 == 0

# escreva todos os pares de 1 ate 100

inicio = 2
fim = 100
atual = inicio

while atual <= fim:
  print(atual)    
  atual += 2
  
# restos lidam bem com ciclos
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0, 1, 2, 0, 1, 2, 0, 1, 2, 0