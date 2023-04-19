def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if not isinstance(n, int):
        raise TypeError("Number must be integer")
    if n == 0:
        return 1
    elif n > 0:
        return factorial_recursive(n - 1) * n
    else:
        raise ValueError("You can't calculate factorial from negative number")
