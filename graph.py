from edge import Edge
import random

class Graph:
    def __init__(self, graphSeedData):
        self.graph = {}
        self.graphSeedData = graphSeedData
        self.flow = 0


    # node (aka vertexes): {1 : [2], 2:[1], 3:[]} etc...
    def addNode(self, node):
        self.graph[node] = []

    def addEdge(self, source, sink, capacity):
        newEdge = Edge(source, sink, capacity)
        newReverseEdge = Edge(sink, source, capacity)
        newEdge.reverseEdge = newReverseEdge
        newReverseEdge.reverseEdge = newEdge
        self.graph[source].append(newEdge)
        self.graph[sink].append(newReverseEdge)

    # create a graph of x size and with y probability that each node is connected
    def initGraph(self):
        for source in self.graphSeedData:
            if source not in self.graph:
                self.addNode(source)
            edgeList = self.graphSeedData[source]
            for edge in edgeList:
                sink, capacity = edge
                if sink not in self.graph:
                    self.addNode(sink)
                self.addEdge(source, sink, capacity)

    def printGraph(self):
        print(self.graph)

    def getGraph(self):
        return self.graph

    # def get_path(self, source, sink, path, visited_paths):
    #     # base case
    #     if source == sink:
    #         return path
    #     for edge in self.graph[source]:
    #         residual = edge.capacity - edge.flow
    #         if residual > 0 and not ()
