from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.adj_matrix = [[0]*(num_vertices) for i in range(num_vertices)]

    def add(self, src, dest):
        self.adj_matrix[src][dest] = 1
        self.num_edges += 1

    def eulerian_cycle(self):
        start = self.num_vertices-1

        # check if all vertices have even degree
        for i in range(self.num_vertices):
            check1 = 0
            check2 = 0
            for j in range(self.num_vertices):
                if(self.adj_matrix[i][j] == 1):
                    check1 += 1
                if(self.adj_matrix[i][j] == 1):
                    check2 += 1
                    if(start>i):
                        start = i
            if (check1 != check2):
                print("Graf wejściowy nie zawiera cyklu.")
                return False

        stack = []
        path = []
        def eulerian_cycle_util(u):
            stack.append(u)
            for i in range(self.num_vertices):
                if self.adj_matrix[u][i] == 1:
                    self.adj_matrix[u][i] = 0
                    eulerian_cycle_util(i)
            path.append(stack.pop())

        eulerian_cycle_util(start)
        if(len(path) != self.num_edges+1 or path[0] != path[-1] or len(path) <= 1):
            print("Graf wejściowy nie zawiera cyklu.")
            return False
        path.reverse()
        for i in range(self.num_edges+1):
            print(path[i], end=" ")
        print("\n")
        return True


class Graph_mg:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_edges = 0
        self.suc_list = defaultdict(list)
        self.pre_list = defaultdict(list)
        self.graph = [[-1]*(num_vertices+3) for i in range(num_vertices)]

    def add(self, src, dest):
        self.suc_list[src].append(dest)
        self.pre_list[dest].append(src)
        self.num_edges += 1

    def create_graph(self):
        used = defaultdict(list)
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                used[i].append(j)

        #lista nastepnikow
        for i in self.suc_list:
            self.suc_list[i].sort()
            for j in self.suc_list[i]:
                self.graph[i][j] = self.suc_list[i][-1]
                self.graph[i][-3] = self.suc_list[i][0]
                used[i].remove(j)

        #lista poprzednikow
        for i in self.pre_list:
            self.pre_list[i].sort()
            for j in self.pre_list[i]:
                self.graph[i][-2] = self.pre_list[i][0]
                self.graph[i][j] = self.pre_list[i][-1] + self.num_vertices
                used[i].remove(j)

        #lista braku incydencji
        for i in used:
            used[i].sort()
            for j in used[i]:
                self.graph[i][-1] = used[i][0]
                #xd
                if (used[i][-1])*(-1) == 0:
                    self.graph[i][j] = -1
                else:
                    self.graph[i][j] = (used[i][-1])*(-1)

    def eulerian_cycle(self):

        self.create_graph()
        start = self.num_vertices-1

        def is_next(a, b):
            if self.graph[a][b] >= 0 and self.graph[a][b] < self.num_vertices:
                return True
            return False

        # check if all vertices have even degree
        for i in range(self.num_vertices):
            check1 = 0
            check2 = 0
            for j in range(self.num_vertices):
                if(self.graph[i][j] >= 0 and self.graph[i][j] < self.num_vertices):
                    check1 += 1
                if(self.graph[i][j] >= self.num_vertices):
                    check2 += 1
                    if(start>i):
                        start = i
            if (check1 != check2):
                print("Graf wejściowy nie zawiera cyklu.")
                return False

        stack = []
        path = []
        def eulerian_cycle_util(u):
            stack.append(u)
            for i in range(self.num_vertices):
                if is_next(u, i) == True:
                    self.graph[u][i] = -1
                    eulerian_cycle_util(i)
            path.append(stack.pop())

        eulerian_cycle_util(start)
        if(len(path) != self.num_edges+1 or path[0] != path[-1] or len(path) <= 1):
            print("Graf wejściowy nie zawiera cyklu.")
            return False
        path.reverse()
        for i in range(self.num_edges+1):
            print(path[i], end=" ")
        print("\n")
        return True

g = Graph_mg(9)
g.add(3, 1)
g.add(1, 2)
g.add(2, 3)

g2 = Graph(9)
g2.add(3, 1)
g2.add(1, 2)
g2.add(2, 3)

print("Undirected:")
g2.eulerian_cycle()

print("Directed:")
g.eulerian_cycle()
