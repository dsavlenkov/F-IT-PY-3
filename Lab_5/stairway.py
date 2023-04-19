from typing import Union

import networkx as nx


def create_stairway_graph(stairway: tuple) -> nx.DiGraph:
    """
    Создает взвешенный направленный граф между ступенями заданной лестницы.
    Вес ребра между ступенями равен соответствующей стоимости перехода.

    :param stairway: Список стоимостей ступеней
    :return: Взвешенный направленный граф NetworkX
    """
    G = nx.DiGraph()
    n = len(stairway)
    for i in range(n):
        G.add_node(i, weight=stairway[i])
        if i < n-1:
            G.add_edge(i, i+1, weight=0)  # переход на следующую ступень
        if i < n-2:
            G.add_edge(i, i+2, weight=stairway[i+2])  # перепрыгивание через одну ступень
    return G


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # используем алгоритм Дейкстры для поиска кратчайшего пути от нулевой до последней ступени
    shortest_paths = nx.dijkstra_path(graph, source=0, target=len(graph.nodes()) - 1, weight='weight')
    # суммируем стоимости ступеней по кратчайшему пути
    return sum(graph[u][v]['weight'] for u, v in zip(shortest_paths[:-1], shortest_paths[1:]))


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = create_stairway_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
