
# ax + b = 0
# ax = -b
# x = -b/a

# 4x + 5 = 0 => -5/4 = -1.25

# ax^2 + bx + c = 0
# delta = b^2 - 4ac
# x1 = (-b + delta) / 2a
# x1 = (-b - delta) / 2a

from math import sqrt

def solve_linear_equation(cof_a, cof_b):
  return (-cof_b / cof_a)

def solve_quadratic_equation(cof_a, cof_b, cof_c):
  delta = cof_b**2 - 4*cof_a*cof_c
  x1 = (-cof_b + sqrt(delta)) / 2*cof_a
  x2 = (-cof_b - sqrt(delta)) / 2*cof_a
  
  return x1, x2