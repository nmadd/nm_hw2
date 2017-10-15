from flow import Flow
from parseFacebook import parseFacebookData, createFacebookGraph
from random import randint

testGraph = {0: [(1, 1), (2, 3)], 1: [(2, 2), (3, 1)], 2: [(3, 1)], 3: []}
# 1 -> 5: 6
# 2 -> 5: 1
# 3 -> 5: 7
# 4 -> 5: 6

g = Flow(createFacebookGraph(parseFacebookData('./facebook_combined.txt')))
print(g.maxFlow(6, 87))
# g.printGraph()

# def testGraph():
#     for i in range(0, 100):
#         rand1 = randint(0, 4038)
#         rand2 = randint(0, 4038)
#         print(rand1, rand2, g.maxFlow(rand1, rand2))
#
# testGraph()
