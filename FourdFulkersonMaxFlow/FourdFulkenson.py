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

with open("test" + str(input()) + ".in") as f:
    graph = f.readlines()
    for i in range(0, len(graph)):
        graph[i] = graph[i].strip().split(" ")
        for j in range(0, len(graph[i])):
            graph[i][j] = int(graph[i][j])

E = graph.pop(0).pop(0)

g = Graph(graph)
source = 0
answer = []
for i in range(0, E):
    answer.append(g.FordFulkerson(source, i))
print('maximum flow is %d'
      '' % max(answer))

