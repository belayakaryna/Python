mas=[3,5,67,-65,34,21]
for i in range(len(mas)):
    if i!=0 and i!=(len(mas)-1):
     if mas[i]>mas[i+1] & mas[i]>mas[i-1]:
      print(i)
