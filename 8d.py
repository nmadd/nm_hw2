from flow import Flow
from parseFacebook import parseFacebookData, createFacebookGraph
from random import randint

parsedData = parseFacebookData('./facebook_combined.txt')
fbGraph = createFacebookGraph(parsedData)
flowGraph = Flow(fbGraph)

def testGraph(numOfTests):
    flow = 0
    flowGraph = Flow(fbGraph)
    for i in range(0, numOfTests):
        rand1 = randint(0, 4038)
        rand2 = randint(0, 4038)
        edgeFlow = flowGraph.maxFlow(rand1, rand2)
        flow += edgeFlow
        print('{}) souce: {} sink: {} max flow: {}'.format(i +1, rand1, rand2, edgeFlow))
        # print(rand1, rand2, g.maxFlow(rand1, rand2))
    print('Avg. Flow: {}'.format(flow/float(numOfTests)))

testGraph(100)
