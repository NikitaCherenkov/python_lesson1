# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

coord0 = list(map(int, input("Введите координаты первой точки через пробел: ").split()))
coord1 = list(map(int, input("Введите координаты первой точки через пробел: ").split()))
print("Расстояние между точками: ", ((max(coord0[0], coord1[0]) - min(coord0[0], coord1[0])) ** 2 + (max(coord0[1], coord1[1]) - min(coord0[1], coord1[1])) ** 2) ** 0.5)

def max(a, b):
    if a > b:
        return a
    else:
        return b

def min(a, b):
    if a < b:
        return a
    else:
        return b
