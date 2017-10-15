from flow import Flow
from parseFacebook import parseFacebookData, createFacebookGraph
from random import randint

testGraph = {0: [(1, 1), (2, 3)], 1: [(2, 2), (3, 1)], 2: [(3, 1)], 3: []}
# 1 -> 5: 6
# 2 -> 5: 1
# 3 -> 5: 7
# 4 -> 5: 6
parsedData = parseFacebookData('./facebook_combined.txt')
fbGraph = createFacebookGraph(parsedData)
flowGraph = Flow(fbGraph)
print(flowGraph.maxFlow(87, 6))

flowGraph = Flow(fbGraph)
print(flowGraph.maxFlow(6, 87))

def testGraph():
    flow = 0
    num = 0
    flowGraph = Flow(fbGraph)
    for i in range(0, 1000):
        rand1 = randint(0, 4038)
        rand2 = randint(0, 4038)
        flow += flowGraph.maxFlow(rand1, rand2)
        num += 1
        # print(rand1, rand2, g.maxFlow(rand1, rand2))
    print("num")
    print(num)
    print("ave")
    print(flow/num)

testGraph()
