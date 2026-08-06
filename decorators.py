from time import perf_counter
from functools import wraps
from datetime import datetime

def logging(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'Вызов функции "{function.__name__}" с аргументами {args}')
        result = function(*args, **kwargs)
        print(f' Функция вернула: {result}')
        return result
    return wrapper

def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        elapsed = perf_counter() - start
        print(f'"{function.__name__}" выполнилась за {elapsed:.6f} сек.')
        return result
    return wrapper

def validate_positive(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        all_values = list(args) + list(kwargs.values())
        for i in all_values:
            if isinstance(i, (int, float)) and i < 0:
                raise ValueError(f'В параметрах функции: {function.__name__} отрицательное число: {i}')
        result = function(*args, **kwargs)
        return result
    return wrapper

def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        all_values = list(args) + list(kwargs.values())
        now = datetime.now()
        with open('calls.log', 'a', encoding='utf-8') as file:
            file.writelines(f'Сработала функция "{function.__qualname__}",\n'
                            f'Переданы агрументы "{all_values[1::]}",\n'
                            f'дата и время - {now.strftime("%d.%m.%y %H:%M")}\n\n')
        return result
    return wrapper

if __name__ == '__main__':
    @logging
    def summ(a, b):
        return a + b

    summ(6, 8)