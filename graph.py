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
        newReverseEdge = Edge(sink, source, 0)
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

    def get_path(self, source, sink, path=[], visited_paths=set()):
        # base case
        if source == sink:
            return path
        for edge in self.graph[source]:
            residual = edge.capacity - edge.flow
            if residual > 0 and (edge, residual) not in visited_paths:
                visited_paths.add((edge, residual))
                return self.get_path(edge.sink, sink, path + [edge, residual], visited_paths)

    def maxFlow(self, source, sink):
        result = 0
        path = self.get_path(source, sink)
        while path != None:
            flow = min(residual for edge, residual in path)
            for edge, res in path:
                edge.flow += flow
                edge.reverseEdge.flow -= flow
            result += flow
            path = self.get_path(source, sink)
        return result
