contador = int(input('digite de onde vc quer iniciar: '))
objetivo = int(input('digite aonde vc quer parar: '))
atualizacao = int(input('digite o ritmo que vc quer avancar: '))

while contador <= objetivo:
  print(contador)
  contador += atualizacao
