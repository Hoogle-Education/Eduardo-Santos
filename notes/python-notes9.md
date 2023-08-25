## Funções no python

Motivações:

- Reuso de codigo
- Maior legibilidade e expressividade
- Código mais de facil de manutenção
- Encapsular alguma lógica mais complicada

```py
def calcula_media_ponderada(a, b):
  return (a * 34.12 + b * 93.5) / (34.12 + 93.5)

a = int(input())
b = int(input())

media = calcula_media_ponderada(a, b)
```

# Programação Orientada a Objetos

```py
def add_patient(names, ages, documents, streets):
  name = input('digite seu nome')
  names.append(name)
  # ...

names = ['a']
ages = [25]
documents = ['111.222.333']
streets = ['Rua A']
appointments = [['12/07', '15/07']]

# trocando dois elementos
origin, destiny = 2, 3
names[origin], names[destiny] = names[destiny], names[origin]
```

## Melhorando a abordagem

classe/molde: Pessoa, Carro
objeto/instancia/fruto do molde: Joao, Ferrari

Classe: tem(atributo) + faz(método)

```py
class Pessoa:
  def __init__(self, name, age, document, street):
    self.name = name
    self.age = age
    self.document = document
    self.street = street

joao = Pessoa('Joao da Silva', 23, '1A', 'Rua A')
maria = Pessoa('Maria da Silva', 24, '1B', 'Rua B')
```

## Método e função

todo método é uma função, só que o método pertence a alguém
