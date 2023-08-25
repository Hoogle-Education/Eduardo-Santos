t = int(input())

for _ in range(t):
  n = int(input())

  # base do fib
  fib = [0, 1]

  for i in range(2, n + 1): # 2 3 4
    fib.append(fib[i-1] + fib[i-2])
    
  print(f'Fib({n}) = {fib[n]}') 