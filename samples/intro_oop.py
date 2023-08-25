class Pessoa:
  def __init__(self, name, age, document, street):
    # atributos
    self.name = name
    self.age = age
    self.document = document
    self.street = street
    
  # metodos
  def make_birthday(self):
    self.age += 1
  
  def __str__(self):
    # printar o cara
    return f'{self.name}, age: {self.age}, document: {self.document}, street: {self.street}'

joao = Pessoa('Joao da Silva', 23, '1A', 'Rua A')
maria = Pessoa('Maria da Silva', 24, '1B', 'Rua B')
pedro = Pessoa('pedro da Silva', 24, '1C', 'Rua C')
lucas = Pessoa('lucas da Silva', 24, '1D', 'Rua D')
yasmin = Pessoa('yasmin da Silva', 24, '1E', 'Rua E')

pedro.street = 'Rua nova'
yasmin.make_birthday()

pessoas = [joao, maria]
pessoas.append(pedro)
pessoas.append(lucas)
pessoas.append(yasmin)

for pessoa in pessoas:
  print(pessoa)