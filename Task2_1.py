n = 0
def squares(a, b, n):
  if a == b:
       return a, b, n+1
  elif a < b:
       return squares(a, b-a, n+1)
  else:
       return squares(a-b, b, n+1)
a = int(input('Введите сторону a \n'))
b = int(input('Введите сторону b \n'))
print('Длины рёбер квадрата и количество получаемых квадратов '+str(squares(a, b, n)))

