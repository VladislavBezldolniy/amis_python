print("Программа рахує алгебраїчну суму Σ і^2 - x^2")
x = float(input("Введіть значення x = "))
def operation(i):     # Вводиться функція "operation"
    '''
        Призначена для підрахунку алгебраїчної суми і**2 - x**2
        Args:
        x:float, 1 з чисел
        i:int,
        Returns:
        float, що дорівнює кількості сумми i**2 - x**2
        Raises:
        -
        Examples:
        >>>print(counter(0,3))
        14
        >>>print(counter(1,4))
        26
        '''
    if i < 0:                                     # Розгалуження по параметру і, (і > 0, і < 0, або i = 0)
        return "Змінна i не може бути менше нуля"  # і < 0 Виконати операцію неможливо
    elif i == 0:
        return 0  # Завершення циклу
    else:
        return i**2 - x**2 + operation(i - 1)  # і > 0, отже викликається рекурсія, зі зміною на і - 1
print(operation(int(input("Введіть кількість ітерацій, і = "))))  # Виклик функції operaion
a = 0
int(a)
A = input().split(" ")
def chet(a):
    '''
            Призначена для підрахунку кількості чисел,що кратні двум
            Args:
            a:int, const (counter)
            A:list, list
            Returns:
            int, що дорівнює кількості чисел кратних двум
            Raises:
            -
            Examples:
            >>>print(counter(5, 3, 5, 6, 7, 2, 7))
            2
            >>>print(counter(1, 4, 6, 7, 4, 6, 3))
            4
            '''
    if A[a] % 2 == 0:
        return chet(a + 1)
    else:
        return 0
print(chet(a))


