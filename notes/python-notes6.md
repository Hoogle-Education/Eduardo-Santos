# Repetição 2

## for (_para_)

```py
for [ITERADOR] in [ITERÁVEL]:
  [FAÇA ALGO]
```

```py
texto = 'Hello'

for letra in texto:
  print(letra)
```

```py
elementos = [10, 20 ,30 , 44, 55]

for numero in elementos:
  print(numero)
```

## range

3 sobrecargas:

### 1 parametro

`range(stop)`

- inicia em zero
- anda de um em um

```py
for number in range(4):
  print(number) # 0 1 2 3
```

### 2 parametro

`range(start, stop)`

- anda de um em um

```py
for number in range(2, 5):
  print(number) # 2 3 4
```

### 3 parametro

`range(start, stop, step)`

```py
for number in range(2, 10, 2):
  print(number) # 2 4 6 8
```
