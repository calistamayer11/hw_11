from Graph import Graph
import unittest


class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""

        f"""
                   400
        Chicago ----------- Boston
           |                   |
           |300                |30
           |                   |
        Philadelphia -------Cape Cod------Stockholm
                        500           4000

        """

        # TODO: Add unittests for public interface of Graph class (except traversal algs)
        self.g = Graph(
            {"Chicago", "Boston", "Philadelphia", "Cape Cod", "Stockholm"},
            {
                ("Chicago", "Boston", 400),
                ("Boston", "Cape Cod", 30),
                ("Cape Cod", "Stockholm", 4000),
                ("Chicago", "Philadelphia", 300),
                ("Philadelphia", "Cape Cod", 500),
            },
        )

    def test_add_vertex(self):
        self.g.add_vertex("Washington")
        self.assertTrue("Washington" in self.g.V)
        self.assertTrue("Washington" in self.g._nbrs.keys())

    def test_remove_vertex(self):
        self.g.remove_vertex("Boston")
        self.assertTrue("Boston" not in self.g.V)
        self.assertTrue("Boston" not in self.g._nbrs.keys())

        self.assertTrue("Boston" not in self.g._nbrs["Chicago"])
        self.assertTrue("Boston" not in self.g._nbrs["Cape Cod"])

        notInEdges = True
        for edge in self.g.E:
            if edge[0] == "Boston" or edge[1] == "Boston":
                notInEdges = False
        self.assertTrue(notInEdges)

    def test_add_edge(self):
        self.g.add_edge("Boston", "Stockholm", 5000)
        self.assertTrue(("Boston", "Stockholm", 5000) in self.g.E)

        self.assertTrue("Boston" in self.g._nbrs["Stockholm"])
        self.assertTrue("Stockholm" in self.g._nbrs["Boston"])

    def test_remove_edge(self):
        self.g.remove_edge("Boston", "Cape Cod")
        self.assertTrue(("Boston", "Cape Cod", 30) not in self.g.E)

        self.assertTrue("Boston" not in self.g._nbrs["Cape Cod"])
        self.assertTrue("Cape Cod" not in self.g._nbrs["Boston"])

    def test_nbrs(self):
        self.num_graph = Graph({3, 7, 2, 4, 5}, {(2, 4, 1), (3, 2, 1), (5, 2, 1)})
        i = 0
        neighbors = [3, 4, 5]
        for neighbor in self.num_graph.nbrs(2):
            self.assertEqual(neighbor, neighbors[i])
            i += 1


class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.

    def setUp(self):
        """ADD DOCSTRING"""

        f"""
                   400
        Chicago ----------- Boston
           |                   |
           |300                |30
           |                   |
        Philadelphia -------Cape Cod------Stockholm
                        500           4000

        """

        # TODO: Add unittests for public interface of Graph class (except traversal algs)
        self.g = Graph(
            {"Chicago", "Boston", "Philadelphia", "Cape Cod", "Stockholm"},
            {
                ("Chicago", "Boston", 400),
                ("Boston", "Cape Cod", 30),
                ("Cape Cod", "Stockholm", 4000),
                ("Chicago", "Philadelphia", 300),
                ("Philadelphia", "Cape Cod", 500),
            },
        )

    # TODO: Which alg do you use here, and why?
    # Alg: Breadth-First Search
    # Why: Finds path with the fewest number of edges
    def test_fewest_flights(self):
        """Tests for fewest flights."""
        # self.g.fewest_flights("Philadelphia")
        # self.assertEqual(
        #     self.g.fewest_flights(
        #         "Philadelphia",
        #         {
        #             "Philadelphia": None,
        #             "Chicago": "Philadelphia",
        #             "Cape Cod": "Philadelphia",
        #             "Boston": "Chicago",
        #             "Stockholm": "Cape Cod",
        #         },
        #     )
        # )
        # self.g.fewest_flights("Philadelphia")
        dic, dist = self.g.fewest_flights("Philadelphia")
        self.assertEqual(
            dic,
            {
                "Philadelphia": 0,
                "Chicago": 1,
                "Cape Cod": 1,
                "Boston": 2,
                "Stockholm": 2,
            },
        )
        self.assertEqual(
            dist,
            {
                "Philadelphia": None,
                "Chicago": "Philadelphia",
                "Cape Cod": "Philadelphia",
                "Boston": "Chicago",
                "Stockholm": "Cape Cod",
            },
        )

    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra's Algorithm
    # Why: Finds shortest path (including weight) between two vertices
    def test_shortest_path(self):
        """Tests for shortest path"""

    # TODO: Which alg do you use here, and why?
    # Alg: Prim's Algorithm
    # Why: Finds shortest path between all vertices
    def test_minimum_salt(self):
        """Finds shortest path between all cities"""


unittest.main()
