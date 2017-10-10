import random

class Graph:
    def __init__(self, initialGraph={}):
        self.nodes = initialGraph

    # nodes (aka vertexes): {1 : [2], 2:[1], 3:[]} etc...
    def addNode(self, node):
        self.nodes[node] = set()

    def addEdge(self, node1, node2):
        self.nodes[node1].add(node2)
        self.nodes[node2].add(node1)

    # create a graph of x size and with y probability that each nodes are connected
    def initGraph(self, size, probability):
        currentNode = 1
        while currentNode <= size:
            self.addNode(currentNode)
            for vert, edges in self.nodes.items():
                if vert != currentNode and random.random() < probability:
                    self.addEdge(vert, currentNode)
            currentNode += 1

    def printGraph(self):
        print(self.nodes)

    def getGraph(self):
        return self.nodes

    # search through graph and find shortest path
    def bfs(self, startingNode, target):
        q = [startingNode]
        history = set()
        pathLengths = {startingNode: 0}

        while len(q) >= 1:
            currentNode = q.pop(0)
            history.add(currentNode)
            for node in self.nodes[currentNode]:
                if node not in history:
                    q.append(node)
                if node not in pathLengths:
                    pathLengths[node] = pathLengths[currentNode] + 1

            if currentNode == target:
                # if the node is not in history, add it to the q
                # in other words, never go backwards - only visit each node once
                if target not in pathLengths:
                    return 'infinity'
                else:
                    result = pathLengths[target]
                    return result
