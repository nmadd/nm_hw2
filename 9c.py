from contagion_graph import Graph
from parseFacebook import parseFacebookData, createUndirectedFacebookGraph

g = Graph(createUndirectedFacebookGraph(parseFacebookData('./facebook_combined.txt')))

numOfTests = 100
threshold = .2
numberOfInitialInfected = 10

print('Q Tests:')
for q in [x / 100.0 for x in range(0, 50, 5)]:
    print(g.findAverageBrd(numOfTests, q, numberOfInitialInfected))

print('K Tests:')
for k in range(0, 250, 10):
    print(g.findAverageBrd(numOfTests, threshold, k))
