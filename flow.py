from edge import Edge
import random
import sys

sys.setrecursionlimit(5000)

class Flow:
    def __init__(self, graphSeedData):
        self.graph = {}
        self.graphSeedData = graphSeedData
        self.flow = 0
        self.initGraph()



    # node (aka vertexes): {1 : [{source: 1, sink: 2, capacity: 4, flow: 0}], 2:[1], 3:[]} etc...
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
            sink = None
            capacity = None
            for edge in edgeList:
                if type(edge) == tuple:
                    sink, capacity = edge
                else:
                    sink = edge
                    capacity = 1
                if sink not in self.graph:
                    self.addNode(sink)
                self.addEdge(source, sink, capacity)

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
            # check that vert has not been previously visited (keep moving forward)
            if residual > 0 and edge.sink not in visited_paths:
                visited_paths.add(source)
                result = self.get_path(edge.sink, sink, path + [(edge, residual)], visited_paths)
                if result != None:
                    return result

    def maxFlow(self, source, sink):
        result = 0
        path = self.get_path(source, sink, [], set())
        while path != None:
            flow = min(residual for edge, residual in path) if len(path) > 0 else 0
            for edge, res in path:
                edge.flow += flow
                edge.reverseEdge.flow -= flow
            result += flow
            path = self.get_path(source, sink, [], set())
        return result
