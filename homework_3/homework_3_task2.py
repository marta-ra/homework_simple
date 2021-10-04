# Задача 2
# Реализовать генератор, который будет выводить числа фибоначчи.


def generator_fib(num):
    list_fib = [0, 1]
    result_fib = [0,1]
    if num ==0:
        print(result_fib)
    while num > 0:
        yield result_fib
        a = sum(list_fib)
        result_fib.append(a)
        list_fib[0] = sum(list_fib)
        list_fib.append(1)
        list_fib.reverse()
        num -= 1
        


fibonnachi = generator_fib(4)
print(fibonnachi)