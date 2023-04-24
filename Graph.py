class Graph:
    def __init__(self, V=set(), E=set()):
        """Initialize a graph"""
        self.V = V
        self.E = E
        self._nbrs = {}
        for v in V:
            self.add_vertex(v)
        for e in E:
            u, v, wt = e
            self.add_edge(u, v, wt)

    def add_vertex(self, v):
        """Adds a vertex to the graph"""
        self.V.add(v)
        self._nbrs[v] = set()

    def remove_vertex(self, v):
        """Removes a vertex from the graph"""
        self.V.remove(v)
        del self._nbrs[v]
        for u in self._nbrs:
            if v in self._nbrs[u]:
                self.remove_edge(u, v)

    def add_edge(self, u, v, wt):
        """Adds an edge to the graph"""
        self._nbrs[v].add(u)
        self._nbrs[u].add(v)
        self.E.add((u, v, wt))

    def remove_edge(self, u, v):
        """Removes an edge from the graph"""
        for e in self.E:
            if e[0] == u and e[1] == v:
                self.E.remove((u, v, e[2]))
                break
            elif e[0] == v and e[1] == u:
                self.E.remove((v, u, e[2]))
                break

        if u in self._nbrs.keys():
            self._nbrs[u].remove(v)
        if v in self._nbrs.keys():
            self._nbrs[v].remove(u)

    def nbrs(self, v):
        """Returns neighbors of the graph"""
        return iter(self._nbrs[v])


if __name__ == "__main__":
    G = Graph({"Boston", "New York", "Philadelphia"})
    G.add_edge("Boston", "New York", 500)
    G.add_edge("Boston", "Philadelphia", 1000)
    G.add_edge("New York", "Philadelphia", 4000)
    print(G.E)
    print(G._nbrs)
    print(G.V)
    G.remove_edge("Boston", "New York")
    print(G.E)
    print("\n")
    G.remove_vertex("Boston")
    print(G.E)
