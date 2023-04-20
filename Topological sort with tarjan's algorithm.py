from typing import List, Dict


def Tarjan_ms(adj_mtx: List[List[int]], start_vertex: int = None) -> List[int]:

    n = len(adj_mtx)
    visited = [False] * n
    on_stack = [False] * n
    stack = []
    order = []

    def dfs(vertex: int):
        nonlocal visited, on_stack, stack, order

        visited[vertex] = True
        on_stack[vertex] = True
        stack.append(vertex)

        for neighbour in range(n):
            if adj_mtx[vertex][neighbour]:
                if not visited[neighbour]:
                    dfs(neighbour)
                elif on_stack[neighbour]:
                    raise ValueError("Graf zawiera cykl. Sortowanie niemożliwe.")

        on_stack[vertex] = False
        order.append(vertex)
        stack.pop()

    if start_vertex is not None:
        dfs(start_vertex)
    else:
        indegrees = [0] * n
        for row in adj_mtx:
            for col, val in enumerate(row):
                if val:
                    indegrees[col] += 1
        found = False
        for vertex, degree in enumerate(indegrees):
            if degree == 0:
                found = True
                dfs(vertex)
        if not found:
            raise ValueError("Graf zawiera cykl. Sortowanie niemożliwe.")

    return order[::-1]


def Tarjan_ln(adj_list: Dict[int, List[int]], start_vertex: int = None) -> List[int]:

    n = len(adj_list)
    visited = [False] * n
    on_stack = [False] * n
    stack = []
    order = []

    def dfs(vertex: int):
        nonlocal visited, on_stack, stack, order

        visited[vertex] = True
        on_stack[vertex] = True
        stack.append(vertex)

        for neighbour in adj_list[vertex]:
            if not visited[neighbour]:
                dfs(neighbour)
            elif on_stack[neighbour]:
                raise ValueError("Graf zawiera cykl. Sortowanie niemożliwe.")

        on_stack[vertex] = False
        order.append(vertex)
        stack.pop()

    if start_vertex is not None:
        dfs(start_vertex)
    else:
        indegrees = {vertex: 0 for vertex in adj_list}
        for vertex in adj_list:
            for neighbour in adj_list[vertex]:
                indegrees[neighbour] += 1
        found = False
        for vertex in adj_list:
            if indegrees[vertex] == 0:
                found = True
                dfs(vertex)
        if not found:
            raise ValueError("Graf zawiera cykl. Sortowanie niemożliwe.")

    return order[::-1]


adj_mtx = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
]

adj_list = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5, 8],
    5: [6, 7],
    6: [10],
    7: [],
    8: [9],
    9: [10],
    10: [],
    11: [],
}

try:
    print(Tarjan_ln(adj_list, start_vertex=3))
    print(Tarjan_ln(adj_list))
except ValueError as e:
    print(e)

try:
    print(Tarjan_ms(adj_mtx, start_vertex=1))
    print(Tarjan_ms(adj_mtx))
except ValueError as e:
    print(e)
