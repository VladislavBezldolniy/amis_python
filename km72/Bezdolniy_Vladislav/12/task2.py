i = 0
def func(lst):
       '''
        Призначена для порівняння з максимальним елементом списку
        Args:
        lst:str, список коистувачв
        Returns:
        int, що дорівнює кількості елементів рівних максимальному
        -
        Examples:
        »>print(func(-1,4,2))
        0
        »>print(func(-1,-1,-5))
        1
        '''
    lst = lst.split(" ")
    lst = sorted(lst)
    ln = len(lst)
    mx = lst[ln]
    mx = mx + 1
    def cicle(n):
        if cicle(n + 1) == mx:
            return i + 1

    return cicle(-1)


print(func(input("input list - ")))