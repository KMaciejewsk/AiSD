from typing import List, Dict


class Graph:
    def __init__(self):
        self.adj_list = {}
        self.adj_mtx = []
        self.n = 0

    def add_vertex(self, vertex: int):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            self.n += 1
            for row in self.adj_mtx:
                row.append(0)
            self.adj_mtx.append([0] * self.n)

    def add_edge(self, vertex1: int, vertex2: int):
        self.adj_list[vertex1].append(vertex2)
        self.adj_mtx[vertex1][vertex2] = 1

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


graph = Graph()
for i in range(11):
    graph.add_vertex(i)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(4, 8)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(6, 10)
graph.add_edge(8, 9)
graph.add_edge(9, 10)

try:
    print(Tarjan_ln(graph.adj_list, start_vertex=3))
    print(Tarjan_ln(graph.adj_list))
except ValueError as e:
    print(e)

try:
    print(Tarjan_ms(graph.adj_mtx, start_vertex=3))
    print(Tarjan_ms(graph.adj_mtx))
except ValueError as e:
    print(e)
