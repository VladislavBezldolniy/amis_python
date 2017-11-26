from math import sqrt
x1 = float(input("Введіть x1: "))
x2 = float(input("Введіть x2: "))
y1 = float(input("Введіть y1: "))
y2 = float(input("Введіть y2: "))
def distance(x1, y1, x2, y2):   # Ввожу функцію
    a1a2 = sqrt((x2-x1)**2+(y2-y1)**2)  # Розрахунок по Піфагора
    return a1a2
print("Відстань між двома точками =", distance(x1, y1, x2, y2))