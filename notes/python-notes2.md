# Mais tipos no python

## Lista/array/vetor

```py
conteudo = ['matheus', 23, 1.8, ['bruno', 'pedro', 'maria']]

print(conteudo)
```

### Acessando posicoes

- Toda lista eh indexada em zero.
- ![exemplo vetores](/assets/c-arrays.jpg)
- Se tem tamanho `n`, logo, ultimo elemento esta na `n-1`

podemos acessar uma posicao:

```py
# pega o primeiro elemento
print(conteudo[0])
```

podemos acessar um intervalo

```py
# pega os elementos 0 e 1
print(conteudo[0:2])

# pega tudo a partir do terceiro elemento
print(conteudo[2:])
```

modos de acessar o ultimo elemento:

- jeito tradicional

```py
lista = ['a', 'b', 'c']
# captura a quantidade de elementos
tamanho = len(lista)
print(lista[tamanho-1])
```

- com indices negativos

```py
lista = ['a', 'b', 'c']
print(lista[1])
```

- indices negativos observam a lista de tras para frente

## Lendo entradas numa mesma linha

## Repeticao

- inicialização
- verificação (objetivo final)
- atualização
- `range(start = 0, stop, step = 1)`
- a funcao range nao inclui o stop.
- a funcao range eh analoga ao acesso de vetores:
- `[start:stop]`

```py
for number in range(5):
  print(number) # 0 1 2 3 4
```

## Percorrendo vetores

```py
salarios = [100, 100, 200, 200, 300]
reajuste = 0.03
# quantidade = len(salarios)

for pos in range(5):
  salarios[pos] = salarios[pos]*reajuste

print(salarios)
```
