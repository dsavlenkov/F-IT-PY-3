from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return []

        # Находим минимальный и максимальный элементы в массиве
    min_elem = min(container)
    max_elem = max(container)

    # Создаем массив для подсчета элементов
    count = [0] * (max_elem - min_elem + 1)

    # Считаем количество каждого элемента в массиве
    for elem in container:
        count[elem - min_elem] += 1

    # Создаем отсортированный массив
    sorted_container = []
    for i in range(len(count)):
        sorted_container.extend([i + min_elem] * count[i])

    return sorted_container
