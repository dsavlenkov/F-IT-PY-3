"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError("List is empty")
    min_ = arr[0]
    min_index = 0
    for i in range(len(arr)):
        if arr[i] < min_:
            min_ = arr[i]
            min_index = i
    return min_index
