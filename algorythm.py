from graph import Graph
from floyd_warshall import floyd_warshall, print_distance_matrix

n = 5
density = 40

graph = Graph.generate_random(n, density)

print("Матриця суміжності:")
graph.print_matrix()

print("\nМатриця найкоротших шляхів Флойд-Уоршелл:")
dist = floyd_warshall(graph)
print_distance_matrix(dist)
