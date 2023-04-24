# class Graph:
#     def __init__(self, V=(), E=()):
#         """Initialize a graph"""
#         self._V = set()
#         self._nbrs = {}
#         for v in V:
#             self.add_vertex(v)
#         for e in E:
#             u, v, wt = e
#             self.add_edge(u, v, wt)

#     def add_vertex(self, v):
#         """Adds a vertex to the graph"""
#         self._V.add(v)
#         self._nbrs[v] = {}

#     def remove_vertex(self, v):
#         """Removes a vertex from the graph"""
#         self._V.remove(v)
#         del self._nbrs[v]
#         for u in self._nbrs:
#             if v in self._nbrs[u]:
#                 del self._nbrs[u][v]

#     def add_edge(self, u, v, wt):
#         """Adds an edge to the graph"""
#         self._nbrs[u][v] = wt
#         self._nbrs[v][u] = wt

#     def remove_edge(self, u, v):
#         """Removes an edge from the graph"""
#         del self._nbrs[u][v]
#         del self._nbrs[v][u]

#     def nbrs(self, v):
#         """Returns neighbors of a vertex"""
#         return iter(self._nbrs[v])


# if __name__ == "__main__":
#     G = Graph({1, 2, 3}, {(1, 2, 3), (2, 1, 3), (1, 3, 5)})

#     print("neighbors of 1:", list(G.nbrs(1)))
#     print("neighbors of 2:", list(G.nbrs(2)))
#     print("neighbors of 3:", list(G.nbrs(3)))


class Graph:
    def __init__(self, V=(), E=()):
        """Initialize a graph"""
        self._V = set()
        self._nbrs = {}
        for v in V:
            self.add_vertex(v)
        for e in E:
            u, v, wt = e
            self.add_edge(u, v, wt)

    def add_vertex(self, v):
        """Adds a vertex to the graph"""
        self._V.add(v)
        self._nbrs[v] = {}

    def remove_vertex(self, v):
        """Removes a vertex from the graph"""
        self._V.remove(v)
        del self._nbrs[v]
        for u in self._nbrs:
            if v in self._nbrs[u]:
                del self._nbrs[u][v]

    def add_edge(self, u, v, wt):
        """Adds an edge to the graph"""
        self._nbrs[u][v] = wt
        self._nbrs[v][u] = wt

    def remove_edge(self, u, v):
        """Removes an edge from the graph"""
        del self._nbrs[u][v]
        del self._nbrs[v][u]

    def nbrs(self, v):
        """Returns neighbors of the graph"""
        return iter(self._nbrs[v])


if __name__ == "__main__":
    G = Graph({1, 2, 3}, {(1, 2, 3), (2, 1, 3), (1, 3, 5)})

    print("neighbors of 1:", list(G.nbrs(1)))
    print("neighbors of 2:", list(G.nbrs(2)))
    print("neighbors of 3:", list(G.nbrs(3)))
