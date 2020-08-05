import random
A = []
n = int(input('Ведите размер списка'))
for i in range(n):
    a = random.randint(0, 99)
    A.append(a)
print(A)
ma = A[0]
mi =A[0]
for i in range(len(A)//2):
    if A[i] > ma:
      ma = A[i]
      n_max = i
    if A[i] < mi:
      mi = A[i]
      n_min = i
print('Максимальный элемент '+str(ma)+' находится под номером '+str(n_max))
print('Минимальный элемент '+str(mi)+' находится под номером '+str(n_min))


