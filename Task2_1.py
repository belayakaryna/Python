n = 0
def squares(a, b, n):
  if a == b:
       return a, b, n+1
  elif a < b:
       print('Отрезаем квадрат со сторонами: '+str(a), str(a))
       return squares(a, b-a, n+1)
  else:
       print('Отрезаем квадрат со сторонами: '+str(b), str(b))
       return squares(a-b, b, n+1)
a = int(input('Введите сторону a \n'))
b = int(input('Введите сторону b \n'))
print('Размер  сторон последнего квадрата и  количество получаемых квадратов '+str(squares(a, b, n)))

