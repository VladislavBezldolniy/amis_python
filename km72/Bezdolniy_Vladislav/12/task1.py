def func(lst):
    '''
        Призначена для знаходження другого елемента за порядком зростання
        Args:
        lst:str, список коистувачв
        Returns:
        str, що дорівнює другому елементу
        Raises:
        -
        Examples:
        »>print(func(-1,4,2))
        2
        »>print(func(-1,-2,-5))
        -2
        '''
    lst = lst.split(" ")
    lst = sorted(lst)
    return lst[1]

print(func(input("input list - ")))