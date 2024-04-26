class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]
        for edge in edges:
            self.adjList[edge.source].append(edge)

def DFS(graph, v, discovered, departure, time):
    discovered[v] = True
    for edge in graph.adjList[v]:
        u = edge.dest
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)
    departure[time] = v
    time = time + 1
    return time

def findShortestDistance(graph, source, N):
    departure = [-1] * N
    discovered = [False] * N
    time = 0
    for i in range(N):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
    cost = [float('inf')] * N
    cost[source] = 0
    for i in reversed(range(N)):
        v = departure[i]
        for e in graph.adjList[v]:
            u = e.dest
            w = e.weight
            if cost[v] != float('inf') and cost[v] + w < cost[u]:
                cost[u] = cost[v] + w
    for i in range(N - 1):
        print(f"dist({source}, {i}) = {cost[i]}")

if __name__ == '__main__':
    N = int(input("enter no of vertices: "))
    edges=[]
    x = int(input("enter no of edges: "))
    print("enter as follows: starting, ending, weight")
    for i in range(0,x):
            a,b,c = map(int,input("").split())
            edges.append(Edge(a,b,c))
    graph = Graph(edges, N)
    source = int(input("enter starting vertex: "))
    findShortestDistance(graph, source, N)
