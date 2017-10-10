from edge import Edge
import random

class Graph:
    def __init__(self, initialGraph={}):
        self.graph = initialGraph
        self.flow = 0

    # node (aka vertexes): {1 : [2], 2:[1], 3:[]} etc...
    def addNode(self, node):
        self.graph[node] = set()

    def createEdge(self, source, sink, capacity):
        newEdge = Edge(source, sink, capacity)
        newReverseEdge = Edge(sink, source, capacity)
        newEdge.reverseEdge = newReverseEdge
        return newEdge
        # self.graph[source].append(newEdge)

    # create a graph of x size and with y probability that each node is connected
    def initGraph(self):
        for vert in self.graph:
            edgeList = self.graph[vert]
            edgeListLength = len(edgeList)
            for i in range(0, edgeListLength):
                edge = edgeList[i]
                edgeList[i] = self.createEdge(edge[0], edge[1], edge[2])
                print(edgeList[i].reverseEdge.sink)

    def printGraph(self):
        print(self.graph)

    def getGraph(self):
        return self.graph

    def get_path(self, source, sink, path, visited_paths):
        # base case
        if source == sink:
            return path
        for edge in self.graph[source]:
            residual = edge.capacity - edge.flow
            if residual > 0 and not ()
