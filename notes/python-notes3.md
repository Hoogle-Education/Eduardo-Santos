# Seleção

## Estrutura `if`

faca um programa que diz se um aluno esta aprovado(nota >= 7) ou reprovado(nota <7)

```py
if condition:
  code_if_its_true()
```

```py
nota = 7.0

if nota >= 7:
  print('Aprovado')

if nota < 7:
  print('Reprovado')
```

## Estrutura `if...else`

```py
if condition:
  code_if_its_true()
else:
  code_if_its_false()
```

## Estrutura

Aumentando o problema:

- maior ou igual a 7: aprovado
- entre 4 e 7: recuperacao
- menor a 4: reprovado

```py
nota = 6.0

if nota >= 7.0:
  print('Aprovado')
else:
  # nota < 7
  if nota >= 4.0:
    print('Recuperacao')
  else:
    print('Reprovado')
```

melhorando...

```py
nota = 6.0

if nota >= 7.0:
  print('Aprovado')
elif nota >= 4.0:
  print('Recuperacao')
else:
  print('Reprovado')
```
