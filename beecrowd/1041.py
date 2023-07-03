linha = input().split()
x, y = float(linha[0]), float(linha[1])

if x == 0 or y == 0:
  if x == 0 and y == 0:
    print('Origem')
  elif x == 0:
    print('Eixo Y')
  else:
    print('Eixo X')
elif x > 0:
  if y > 0:
    print('Q1')
  else:
    print('Q4')
elif x < 0:
  if y > 0:
    print('Q2')
  else:
    print('Q3')