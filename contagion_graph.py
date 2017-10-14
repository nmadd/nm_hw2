import random
from contagion_node import Node

class Graph:
    def __init__(self, graphSeedData):
        self.graphSeedData = graphSeedData
        self.graph = {}

    # create a graph of x size and with y probability that each graph are connected
    def initGraph(self):
        for val in self.graphSeedData:
            self.addVert(val)
        for val in self.graphSeedData:
            for edge in self.graphSeedData[val]:
                self.addEdge(val, edge)


    # graph (aka vertexes): {1 : [2], 2:[1], 3:[]} etc...
    def addVert(self, val):
        self.graph[val] = Node(val)

    def addEdge(self, node1, node2):
        self.graph[node1].edges.add(node2)
        self.graph[node2].edges.add(node1)

    def infectEarlyAdopters(self, earlyAdoptersSet, choice):
        for val in earlyAdoptersSet:
            self.graph[val].choice = choice

    def flipOrStay(self, q):
        flipped = False
        for node in self.graph.values():
            x = 0
            y = 0
            if node.choice != 'X':
                for edge in node.edges:
                    if self.graph[edge].choice == 'X':
                        x += 1
                    else:
                        y += 1
            if (x + y) > 0 and x/ float(x + y) > q:
                node.choice = 'X'
                flipped = True
        return flipped

    def brd(self, q):
        while self.flipOrStay(q):
            continue


    def printGraph(self):
        print(self.graph)

    def getGraph(self):
        return self.graph
