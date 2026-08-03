def logging(function):
    def wrapper(*args, **kwargs):
        print(f'Вызов функции "{function.__name__}" с аргументами {args}')
        result = function(*args, **kwargs)
        print(f' Функция вернула: {result}')
        return result
    return wrapper


if __name__ == '__main__':
    @logging
    def summ(a, b):
        return a + b

    summ(6, 8)