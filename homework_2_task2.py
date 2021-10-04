# Задача 2
# Написать программу, где:
# Ввод:
# Первый аргумент который сохраняется в одну переменную.(input, от 3 до 23)
# Второй аргумент который сохраняется в другую переменную.(input, от 3 до 23)
# Третий аргумент который является операцией(+, -, *, /)
# Вывод:
# Данная операция должна произойти с использованием первых двух аргументов.



def task2(variable_1: int, variable_2: int, variable_action):
    if 3 <= variable_1 <= 23 and 3 <=variable_2 <= 23:
        if variable_action == '+':
            result = variable_1 + variable_2
        elif variable_action == '-':
            result = variable_1 - variable_2
        elif variable_action == '*':
            result =  variable_1 * variable_2
        elif variable_action == '/':
            result = variable_1 / variable_2
    else:
        result = 'Введите число от 3 до 23'
    return result

# variable_1 = int(input('Переменая 1:'))
# variable_2 = int(input('Переменая 2:'))
# variable_action = input('Действие ((+, -, *, /)):')
# a = task2(variable_1, variable_2, variable_action)
# print(a)