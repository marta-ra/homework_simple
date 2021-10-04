# Задача 2
# Реализовать генератор, который будет выводить числа фибоначчи.


# 1 способ, когда числа фибонначчи с 0 начинаются:
def generator_fib(num):
    list_fib = [0, 1]
    while num > 0:
        yield list_fib[0]
        a = sum(list_fib)
        list_fib[0] = sum(list_fib)
        list_fib.reverse()
        num -= 1

print(list(generator_fib(10)))

# 2 способ, когда числа фибонначчи с 1 начинаются:
def generator_fib_2(num):
    fib_1, fib_2 = 0, 1
    while num > 0:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_1
        num -= 1
        
print(list(generator_fib_2(10)))
