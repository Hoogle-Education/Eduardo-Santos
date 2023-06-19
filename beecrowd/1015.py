# import global
# import math

# import de funcoes
from math import sqrt

linha = input().split()
x1, y1 = float(linha[0]), float(linha[1])

linha = input().split()
x2, y2 = float(linha[0]), float(linha[1])

diferenca_x = (x1 - x2) ** 2
diferenca_y = (y1 - y2) ** 2
dist = sqrt(diferenca_x + diferenca_y)

print(f'{dist:.4f}')
