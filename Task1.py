# Вариант 7
# В переменную Y ввести номер года. Определить, является ли год високосным.
Y = int(input('Введите год для проверки на високосность \n'))
if (Y % 4 == 0) and (Y % 100 != 0) or (Y % 400 == 0):
    print('Год является високосным')
else:
    print('Год  не является високосным')


















