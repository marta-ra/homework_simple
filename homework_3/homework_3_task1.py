# Задача 1
# Реализовать декоратор, который будет приводить все аргументы функции к определенному типу данных.
# @validation(<type of data (int, float, str, typle, list)>)
# после чего будет передавать эти значения в функцию.


# Первое решение:
def validation_1(type_arg):
    def actual_decorator(func):       
        def wrapper(*args):
            print(args)
            result = []
            for i in args:
                # т. к. в задании сказано "приводить все аргументы функции к определенному типу данных", то чтобы 
                # преобразовать каждый аргумент в кортеж или список, нужно чтобы тип данных был итерируемый.
                # Я отправляю рандомные данные в data_change_type_1, поэтому решила переводить их в строку, чтобы можно было
                # буквально каждый элемент превратить в отдельный список/кортеж (во втором варианте решения data_change_type_2)
                # используется другой подход - там в целом полученные аргументы погружаются в один список или кортеж
                if type_arg == tuple or type_arg == list:
                    i = str(i)
                i = type_arg(i)
                result.append(i)
            return func(*result)
        return wrapper
    return actual_decorator


# Второе решение:
def validation_2(func):
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


type_argument = int

@validation_1(type_arg=type_argument)
def data_change_type_1(*args):
    return args


@validation_2
def data_change_type_2(type_argument, *args):
    return args

a = data_change_type_1(6.3,7)
print(a)


