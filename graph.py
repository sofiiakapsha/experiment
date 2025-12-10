import random
import math

class Graph:
    def __init__(self, n):
        self.n = n
        self.matrix = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            self.matrix[i][i] = 0

    def add_edge(self, u, v, w):
        if u == v:
            return
        self.matrix[u][v] = w

    @staticmethod
    def generate_random(n, density, min_w=1, max_w=10):
        graph = Graph(n)
        max_edges = n * (n - 1)
        target_edges = int(max_edges * (density / 100))
        all_edges = [(u, v) for u in range(n) for v in range(n) if u != v]
        selected = random.sample(all_edges, target_edges)
        for (u, v) in selected:
            w = random.randint(min_w, max_w)
            graph.add_edge(u, v, w)
        return graph

    def print_matrix(self):
        for l in self.matrix:
            print(l)


