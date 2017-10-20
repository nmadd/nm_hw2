import random
from contagion_node import Node
from random import randint

class Graph:
    def __init__(self, graphSeedData):
        self.graphSeedData = graphSeedData
        self.graph = {}
        self.initGraph()

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

    def infectEarlyAdopters(self, earlyAdoptersSet, flippedChoice="X", startingChoice="Y"):
        for node in self.graph.values():
            node.choice = startingChoice
        for val in earlyAdoptersSet:
            self.graph[val].choice = flippedChoice

    def flipOrStay(self, q):
        flipped = False
        for node in self.graph.values():
            x = 0
            y = 0
            if node.choice != 'X':
                for neighbor in node.edges:
                    if self.graph[neighbor].choice == 'X':
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
        return (self.countChoice('X'), self.countChoice('Y'))

    def findAverageBrd(self, numOfIterations, threshold, numOfEarlyAdopters):
        # k = set of early adopters
        totalX = 0
        totalY = 0
        for i in range(0, numOfIterations):
            k = self.createEarlyAdopterSet(numOfEarlyAdopters) if type(numOfIterations) is int else numOfEarlyAdopters         
            self.infectEarlyAdopters(k)
            choices = self.brd(threshold)
            totalX += choices[0]
            totalY += choices[1]
        return 'Infection Rate: {}% X: {} Y: {} Q: {} K: {} Num of Tests: {}'.format(round((totalX/float((totalX + totalY))) * 100, 2), totalX/numOfIterations, totalY/numOfIterations, threshold, numOfEarlyAdopters, numOfIterations)
        # print(float(totalX/numOfIterations), float(totalY/numOfIterations))

    def createEarlyAdopterSet(self, num):
        randomSet = []
        for i in range(0, num):
            x = randint(0, 4038)
            randomSet.append(x)
        return set(randomSet)

    def countChoice(self, choice):
        return [x.choice for x in self.graph.values()].count(choice)


    def printGraph(self):
        print(self.graph)

    def getGraph(self):
        return self.graph
