X = []
Y = []
def sp(n):    # Вводиться функція sp
    if n > 0:
        X.append(input("Введіть елемент - "))     # Додавання елементу ло списку
        return sp(n - 1)   # Змененння ітератора n на 1
    else:
        return X
n = int(input("Введіть кількість елементів списку - "))
sp(n)    # Виклик функції
def revers(n):    # Вводиться функція
    if n == 0:
        return Y
    else:
        Y.append(X[n - 1])    # Елементи додаються у зворотньому порядку
        return revers(n - 1)
revers(n)    # Викликається функція
print(X, "Початковий список")
print(Y, "Перевернутий список")