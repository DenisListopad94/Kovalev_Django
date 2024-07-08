import functools
from random import randint

@functools.lru_cache(maxsize=None)  # maxsize=None означает, что кэш не ограничен по размеру
def recursive_positive_sum(numbers):
    if not numbers:
        return 0
    head, *tail = numbers
    if head > 0:
        return head + recursive_positive_sum(tuple(tail))
    else:
        return recursive_positive_sum(tuple(tail))


numbers_list = [randint(-50,50) for i in range(10)]
result = recursive_positive_sum(tuple(numbers_list))
print(f"Сумма положительных чисел списка {numbers_list}: {result}")