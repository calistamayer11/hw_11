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

    def remove_edge(self, u, v, wt=0):
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

    def fewest_flights(self, city):
        tree_dict = {}
        tree_nbr_flights = {}
        to_visit = [(None, city)]
        while to_visit:
            a, b = to_visit.pop(0)
            if b not in tree_dict:
                tree_dict[b] = a
                if a is None:
                    tree_nbr_flights[b] = 0
                else:
                    tree_nbr_flights[b] = 1 + tree_nbr_flights[a]
                for n in self.nbrs(b):
                    to_visit.append((b, n))
        return tree_dict, tree_nbr_flights

    def _weight(self, u, v):
        for edge in self.E:
            if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
                return edge[2]
        return 0

    def shortest_path(self, city):
        dict_distance = {u: float("inf") for u in self.V}
        dict_distance[city] = 0
        trav_tree = {city: None}

        dict_nbr_distance = {city: 0}

        while dict_nbr_distance:
            current_city, lowest_value = list(dict_nbr_distance.items())[0]
            for city in dict_nbr_distance.keys():
                if dict_nbr_distance[city] < lowest_value:
                    lowest_value = dict_nbr_distance[city]
                    current_city = city

            del dict_nbr_distance[current_city]

            for neighbor in self.nbrs(current_city):

                dist_to_city = self._weight(current_city, neighbor)

                if dict_distance[neighbor] > dict_distance[current_city] + dist_to_city:
                    trav_tree[neighbor] = current_city
                    dict_distance[neighbor] = dict_distance[current_city] + dist_to_city
                    dict_nbr_distance[neighbor] = int(dict_distance[neighbor])

            return trav_tree, dict_distance

    def minimum_salt(self, city):
        tree_dict = {}
        dict_dist = {}
        toVisit = [(None, city, 0)]
        while toVisit:
            prioritized = toVisit.pop()
            a = prioritized[0]
            b = prioritized[1]
            if b not in tree_dict:
                tree_dict[b] = a
                if a is None:
                    dict_dist[b] = 0
                else:
                    dict_dist[b] = self._weight(a, b)
                for neighbor in self.nbrs(b):
                    toVisit = self._sort_priority(
                        (b, neighbor, self._weight(b, neighbor)), toVisit
                    )
        return tree_dict, dict_dist

    def _sort_priority(self, entry, L):
        if len(L) == 0:
            return [entry]
        index = len(L)
        for i in range(len(L)):
            if entry[2] > L[i][2]:
                index = i
                break
        newList = L[:index]
        newList.append(entry)
        newList = newList + L[index:]
        return newList


if __name__ == "__main__":
    G = Graph({"Boston", "New York", "Philadelphia"})
    g = Graph(
        {"Chicago", "Boston", "Philadelphia", "Cape Cod", "Stockholm"},
        {
            ("Chicago", "Boston", 400),
            ("Boston", "Cape Cod", 30),
            ("Cape Cod", "Stockholm", 4000),
            ("Chicago", "Philadelphia", 300),
            ("Philadelphia", "Cape Cod", 500),
        },
    )
    G.add_edge("Boston", "New York", 500)
    G.add_edge("Boston", "Philadelphia", 1000)
    G.add_edge("New York", "Philadelphia", 4000)
    # print(g.fewest_flights("Philadelphia")[0])
    dic, dist = g.fewest_flights("Philadelphia")
    print(dist)
    print(dic)
    print("\n)")
    # print(g.fewest_flights("Chicago"[0]))
    # print(G.shortest_path("Boston"))
