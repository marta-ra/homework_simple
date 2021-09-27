# Задача 2
# Написать программу, где:
# Ввод:
# Первый аргумент который сохраняется в одну переменную.(input, от 3 до 23)
# Второй аргумент который сохраняется в другую переменную.(input, от 3 до 23)
# Третий аргумент который является операцией(+, -, *, /)
# Вывод:
# Данная операция должна произойти с использованием первых двух аргументов.

variable_1 = int(input('Переменая 1:'))
variable_2 = int(input('Переменая 2:'))
variable_action = input('Действие ((+, -, *, /)):')
if 3 <= variable_1 <= 23 and 3 <=variable_2 <= 23:
    if variable_action == '+':
        print(variable_1 + variable_2)
    elif variable_action == '-':
        print(variable_1 - variable_2)
    elif variable_action == '*':
        print(variable_1 * variable_2)
    elif variable_action == '/':
        print(variable_1 / variable_2)


        # СДЕЛАТЬ ТЕСТЫ!!!