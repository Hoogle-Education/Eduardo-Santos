# 2, 4, 6, 8, 10 
# pares: tem o formato 2k
# par % 2 == 0

# escreva todos os pares de 1 ate 100

inicio = 1
fim = 100
atual = inicio

while atual <= fim:
  if atual % 2 == 0:
    print(atual)
    
  atual += 1