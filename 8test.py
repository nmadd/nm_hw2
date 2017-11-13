from flow import Flow
from parseFacebook import parseFacebookData, createFacebookGraph
from random import randint

parsedData = parseFacebookData('./facebook_combined.txt')
fbGraph = createFacebookGraph(parsedData)


flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(2783, 2186)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(1603, 2136)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(756, 3423)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(1360, 1205)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(638, 2647)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(731, 3384)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(3883, 3244)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(473, 2598)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(3602, 2783)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(2754, 3922)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(1240, 447)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(2885, 3305)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(59, 3712)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(513, 2051)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(892, 342)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(471, 1775)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(274, 1491)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(1240, 3659)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(3141, 388)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(2356, 3033)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(2756, 1473)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(3778, 2437)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(454, 118)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(2115, 2276)
print('flow: {}'.format(edgeFlow))

flowGraph = Flow(fbGraph)
edgeFlow = flowGraph.maxFlow(1979, 1405)
print('flow: {}'.format(edgeFlow))
