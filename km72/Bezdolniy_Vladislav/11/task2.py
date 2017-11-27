X = []
def sp(n):    # Вводиться функція
    if n > 0:
        X.append(input("Введіть елемент - "))     # Додавання елементу ло списку
        return sp(n - 1)   # Змененння ітератора n на 1
    else:
        return X
n = int(input("Введіть кількість елементів вашого списку - "))
sp(n)    # Виклик функції


def minList(X, i):    # Вводиться функція
    global min    # Глобалізується змінна
    if i < len(X) - 1:
        if min > X[i + 1]:    # Визначення мінімального елемента
            min = X[i + 1]
            return minList(l, i + 1)    # Рекурсія з викликом і + 1
    else:
        return minList(l, i + 1)
    return min

i = int(0)
min = X[i]
print(minList(X, i))