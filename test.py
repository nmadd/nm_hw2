from graph import Graph

testGraph = {1: [(1, 2, 1), (1, 3, 3)], 2: [(2, 3, 2), (2, 4, 1)], 3: [(3, 4, 1)], 4: []}

g = Graph(testGraph)
g.initGraph()
g.printGraph()