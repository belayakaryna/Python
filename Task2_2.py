import base64
mas = []
a = int(input('Введите количество строк двумерного массива \n'))
b = int(input('Введите количество столбцов двумерного массива  \n'))
r = 1
def Print(mas):
    for i in mas:
        for j in i:
            print(j, end='  ')
        print()
def Massive(a, b, r):
  for i in range(a):
    mas.append([])
    for j in range(b):
     if r <= 64:
        mas[i].append(base64.b64encode(str(r).encode()))
        #mas[i].append(r)
        r += 1
     else:
       r = 1
       mas[i].append(base64.b64encode(str(r).encode()))
       #mas[i].append(r)
       r += 1
  return Print(mas)
print(Massive(a, b, r))