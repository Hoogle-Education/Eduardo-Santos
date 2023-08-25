# Matriz

- Vetor de vetor
- Array de Array
- Array 2D

## Acesso

`matriz[linha][coluna]`

```python
matrix = [ [9.2, 6.3, 5.4],
           [5.6, 3.4, 7.1],
           [7.8, 9.0, 2.3] ]

print(matrix[0][1])
print(matrix[2][2])
print(matrix[2][1])
print(matrix[1][2])
```

## input de matrizes

```
3 4
1 2 3 4
4 5 6 7
7 8 9 1
```

```python
linhas, colunas = input().split()
linhas, colunas = int(linhas), int(colunas)

for linha in range(linhas):
  print(input().split())
```
