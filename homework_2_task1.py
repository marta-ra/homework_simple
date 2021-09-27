# Задача 1
# Напишите программу, которая делает следующее:
# Ввод:
# Первый аргумент который сохраняется в одну переменную.
# Второй аргумент который сохраняется в другую переменную.
# Вывод:
# Разницу между этими переменными(положительная, без знака), если они являются числами(int,float) в диапазоне от 3 до 21, либо, если один или оба аргумента являются строкой(str)
# или не входят в диапазон, то тогда просто из сложить(как строки).


def task1(variable_1, variable_2):
    result = lambda variable_1, variable_2: abs(variable_1 - variable_2) if (type(variable_1) is int or type(variable_1) is float) and (type(variable_2) is int or type(variable_2) is float) and 3<=variable_1<=21 and 3<=variable_2<=21 else (variable_1+variable_2 if type(variable_1) is str and type(variable_2) is str else None)
    answer = result(variable_1, variable_2)
    # second solution:
    # if (type(variable_1) is int or type(variable_1) is float) and (type(variable_2) is int or type(variable_2) is float) and 3<=variable_1<=21 and 3<=variable_2 <=21:
    #     answer = abs(variable_1 - variable_2)
    # elif type(variable_1) is str and type(variable_2) is str:
    #     answer = variable_1 + variable_2
    return answer

# variable_1 = input('Переменая 1:')
# variable_2 = input('Переменая 2:')
# print(task1(variable_1, variable_2))

