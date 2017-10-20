from contagion_graph import Graph
from parseFacebook import parseFacebookData, createUndirectedFacebookGraph
from random import randint

g = Graph(createUndirectedFacebookGraph(parseFacebookData('./facebook_combined.txt')))

numOfTests = 100
threshold = .1
k = 10

print(g.findAverageBrd(numOfTests, threshold, k))
