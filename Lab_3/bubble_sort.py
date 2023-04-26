from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    swap_flag = False
    unsorted_length = len(container)
    for i in range(1, len(container)):
        for j in range(1, unsorted_length):
            swap_flag = False
            if container[j] < container[j - 1]:
                container[j], container[j - 1] = container[j - 1], container[j]
                swap_flag = True
        unsorted_length -= 1
    if not swap_flag:
        return container
