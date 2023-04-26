def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    a = 1
    if not isinstance(n, int):
        raise TypeError("Number must be integer")
    elif n < 0:
        raise ValueError("You cannot calculate factorial from a negative number")
    elif n == 0:
        return 1
    for i in range(1, n + 1):
        a = a * i
    return a
