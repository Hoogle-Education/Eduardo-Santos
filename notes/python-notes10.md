# Funções

codigo ruim: dificil de entender, extender e mudar

- Processos definidos
- Conjunto de passos bem definido
- Entradas: argumento, parametro
- Saidas: retorno
- Objetivo: termina ou retorna

```py
def welcome():
  print('Welcome to my program')

def hello():
  welcome()
  print('Hello, world')

def hello_someone(name):
  welcome()
  print(f'Hello, {name}')

hello()
hello_someone('john')
```

# john = Person('John', 23, 'Fortaleza')

# maria = Person('Maria', 23, 'Recife')

# john.say_hello(maria)
