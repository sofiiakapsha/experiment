import math

def floyd_warshall(graph):
    n = graph.n
    dist = [l.copy() for l in graph.matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_distance_matrix(dist):
    for l in dist:
        print([("∞" if x == math.inf else x) for x in l])
