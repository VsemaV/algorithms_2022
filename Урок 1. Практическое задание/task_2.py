"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.
"""

# Сложность первого алгоритма должна быть O(n^2) - квадратичная.

def check_1(lst_obj):
    N = len(lst_obj)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if lst_obj[j] > lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
    print(lst_obj[0])


# Сложность второго алгоритма должна быть O(n) - линейная.

def check_2(lst_obj):
    min_number = lst_obj[0]
    for j in lst_obj:
        if j < min_number:
            min_number = j
    return min_number

list1 = [1, 2, 3, 4, 5, 6]

result1 = check_1(list1)


result2 = check_2(list1)
print(result2)


