# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Введите номер дня недели')
day = int(input())
if day in range(1,6):
    print('Нет')
elif day in range(6, 8):
    print('Да')
else:
    print('Дня', day, 'не существует')