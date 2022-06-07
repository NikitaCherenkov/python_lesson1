# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def to_bool(a):
    if (a in ['1', 'yes', 'true']):
        return True
    else:
        return False

entry = input("Введите значения X, Y, Z через пробел: ").split()
x = to_bool(entry[0])
y = to_bool(entry[1])
z = to_bool(entry[2])
if not (x or y or z) == ((not x) and (not y) and (not z)):
    print(True)
else:
    print(False)
