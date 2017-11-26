a = float(input("Введіть число а:"))
n = int(input("Введіть бажану степінь:"))
def power(a, n):   # Ввожу функцію
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)    # Використовую цю ж функцію, тільки на крок раніше

print(power(a, n))