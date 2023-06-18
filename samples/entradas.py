# linha = input('digite numeros: ')

# splited = linha.split()

entrada = input().split()
tamanho = len(entrada)

print(entrada)

for pos in range(tamanho):
    entrada[pos] = int(entrada[pos])

print(entrada)
print(sum(entrada))
