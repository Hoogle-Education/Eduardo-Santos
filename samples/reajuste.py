salarios = [100, 100, 200, 200, 300, 600]
reajuste = 1.03
quantidade = len(salarios)

for pos in range(quantidade):
    print(f'Salario #{pos+1} = {salarios[pos]}')
    salarios[pos] = salarios[pos]*reajuste

print(salarios)
