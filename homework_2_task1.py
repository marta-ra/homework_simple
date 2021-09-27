# Задача 1
# Напишите программу, которая делает следующее:
# Ввод:
# Первый аргумент который сохраняется в одну переменную.
# Второй аргумент который сохраняется в другую переменную.
# Вывод:
# Разницу между этими переменными(положительная, без знака), если они являются числами(int,float) в диапазоне от 3 до 21, либо, если один или оба аргумента являются строкой(str)
# или не входят в диапазон, то тогда просто из сложить(как строки).


variable_1 = int(input('Переменая 1:'))
variable_2 = float(input('Переменая 2:'))
# print(type(variable_1))
# print(type(variable_1))
result = lambda variable_1, variable_2: abs(variable_1 - variable_2) if (type(variable_1) is int or type(variable_1) is float) and (type(variable_2) is int or type(variable_2) is float) and (3<=variable_1<=21) and (3<=variable_2<=21) else (variable_1+variable_2 if type(variable_1) is str and type(variable_2) is str else None)
# second solution:
# if (type(variable_1) is int or type(variable_1) is float) and (type(variable_2) is int or type(variable_2) is float) and (3<=variable_1 and variable_2 <=21):
#     print(abs(variable_1 - variable_2))
# elif type(variable_1) is str and type(variable_2) is str:
#     print(variable_1 + variable_2)

# print(result(variable_1,variable_2))



# СДЕЛАТЬ ТЕСТЫ!!!