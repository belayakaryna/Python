'''В соответствии со своим вариантом разработать программу для работы с файлами на языке Python.
Предварительно создать текстовый файл F1 не менее чем из 10 строк и записать в него информацию.'''
# Вариант 9
'''Скопировать из файла F1 в файл F2 все строки, начинающиеся на букву «А», расположенные между строками с номерами N1 и N2.
Определить количество слов в первой строке файла F2.'''

N1 = int(input('Введите номер строки N1 '))
N2 = int(input('Введите номер строки N2 '))
mas1 = []
mas3 = []
try:
    with open(r'D:\F1.txt', 'r', encoding='utf-8') as f:
     for line in f:
       line = line.strip()
       mas1.append(line)  # добавление строк файла в список
     mas2 = mas1[N1-1:N2-1]  # добавление в массив выбранных строк, N1-1 И N2-1 - так как номерация в списке идёт с 0, а номера строк с 1
     for i in mas2:
      if i[0] == 'А':
       mas3.append(i)
     if len(mas3)==0:
         print('Нужных строк не найдено')
     else:
      with open (r'D:\F2.txt', 'w', encoding='utf-8') as ff:
        ff.write('\n'.join(mas3))
      with open(r'D:\F2.txt', 'r', encoding='utf-8') as fff:
        l = fff.readline()
        print(len(l.split(' ')))
except FileNotFoundError:
 print('File not found')
except IOError:
 print("An IOError has occurred!")









