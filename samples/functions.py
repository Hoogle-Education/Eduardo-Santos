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