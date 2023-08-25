from equations import solve_quadratic_equation, solve_linear_equation

a, b = 4, 5

# john = Person('John', 23, 'Fortaleza')
# maria = Person('Maria', 23, 'Recife')
# john.say_hello(maria)

result = solve_linear_equation(a, b)
print(f'the result of ({a})x + ({b}) = 0 is equal to {result}')\
  
c, d, e = 1, -4, 4

result2 = solve_quadratic_equation(cof_b = d, cof_a = c, cof_c = e)
print(f'the result of ({c})x^2 + ({d})x + ({e}) = 0 is equal to {result2}')