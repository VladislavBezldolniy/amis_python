print("""Здравствуйте!
Данная программа предназначена для расчёта возможностей перемещения шахматного 
слона по шахматной доске.""")
#Выводим приветствие и предназначение программы
x = int(input("Введите номер начального ряда:"))#Команда для ввода переменной
y = int(input("Введите номер начального столбца:"))#Команда для ввода переменной
x1 = int(input("Введите номер конечного ряда:"))#Команда для ввода переменной
y1 = int(input("Введите номер конечного столбца:"))#Команда для ввода переменной
if (0< x <9) and (0< x1 <9) and (0< y <9) and (0< y1 <9):#условие для правильного ввода данных
    if abs(x-x1) == abs(y1-y):#условие перевдвижения слона
        res = "Yes"  # вводим новую переменную и присваиваем её соответственное значение
    else:#условие невозможности передвижения слона
        res = "No"  # вводим новую переменную и присваиваем её соответственное значение
elif x < 0 or y < 0 or x > 8 or y > 8:  # условие для неправильного ввода данных
    res = "Количество рядов/столбцов не должно превышать 8 и должно быть положительным числом."
# вводим новую переменную и присваиваем её соответственное значение
elif x1 < 0 or y1 < 0 or x1 > 8 or y1 > 8:#условие для неправильного ввода данных
    res = "Количество рядов/столбцов не должно превышать 8 и должно быть положительным числом."
    # вводим новую переменную и присваиваем её соответственное значение
print(res)#выводим результат
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))  # Команда для окончания программы

