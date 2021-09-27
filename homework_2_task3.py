# Задача 3
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#
# Выведите все элементы, которые меньше 5.
# Примечание, использовать list comprehension.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print_num_less_5 = lambda i: print(i) if i < 5 else i
squares = [print_num_less_5(i) for i in a]