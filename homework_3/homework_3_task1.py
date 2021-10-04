# Задача 1
# Реализовать декоратор, который будет приводить все аргументы функции к определенному типу данных.

# @validation(<type of data (int, float, str, typle, list)>)

# после чего будет передавать эти значения в функцию.

def validation(func):
    def wrapper(type_arg, *args):
        result = []
        if type_arg == str:
            for i in args:
                i = str(i)
                result.append(i)
            return func(type_arg, *result)
        elif type_arg == int:
            for i in args:
                i = int(i)
                result.append(i)
            return func(type_arg, *result)
        elif type_arg == float:
            for i in args:
                i = float(i)
                result.append(i)
            return func(type_arg, *result)
        elif type_arg == list:
            for i in args:
                result.append(i)
            return func(type_arg, result)
        elif type_arg == tuple:
            for i in args:
                result.append(i)
            result = tuple(result)
            return func(type_arg, result)
    return wrapper



@validation
def data_change_type(type_arg, *args):
    return args

# a = data_change_type(int, 6.3,7)
# print(a)