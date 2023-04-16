import numpy as np
class Graph:

    def __init__(self, graph_resid):
        self.graph_resid = graph_resid  # Остаточный граф
        self.ROW = len(graph_resid)

    def BFS(self, s, t, parent):

        # Помечаем все вершины как не посещённые
        visited = [False] * self.ROW

        # очередь
        q = []

        # Mark the source node as visited and enqueue it
        q.append(s)
        visited[s] = True


        while q:


            vertex = q.pop(0)


            for ind, val in enumerate(self.graph_resid[vertex]):
                if visited[ind] == False and val > 0:
                    q.append(ind)
                    visited[ind] = True
                    parent[ind] = vertex
                    if ind == t:
                        return True

        return False

    def FordFulkerson(self, source, sink):

        parent = [-1] * self.ROW

        max_flow = 0

        while self.BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph_resid[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph_resid[u][v] -= path_flow
                self.graph_resid[v][u] += path_flow
                v = parent[v]

        return max_flow


# создаём граф

graph = []
with open("test" + str(input()) + ".in") as f:
    for line in f:
        graph.append([int(x) for x in line.split()])

new_graph = np.array([[0]*(graph[0][0]+graph[0][1]+2)]*(graph[0][0]+graph[0][1]+2))
for i in range(0, len(new_graph)):
    for j in range(0, len(new_graph[i])):
        if i == j:
            continue
        if i == 0 and j <= graph[0][0]:
            new_graph[i][j] = 1
        if i > (graph[0][0]) and j == len(new_graph)-1:
            new_graph[i][j] = 1
        if i < graph[0][0]+1 and j == 0:
            new_graph[i][j] = -1
        if i == len(new_graph)-1 and j > graph[0][0]:
            new_graph[i][j] = -1

for x in range(1, len(graph)):
    for y in range(1,len(graph[x])):
        new_graph[x][graph[0][0]+graph[x][y]+1]=1

print(new_graph)


sink = sum(graph.pop(0)) + 2

g = Graph(graph)
source = 0
print('maximum flow is %d' % g.FordFulkerson(source, sink))