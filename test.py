from flow import Flow
from parseFacebook import parseFacebookData, createFacebookGraph

testGraph = {0: [(1, 1), (2, 3)], 1: [(2, 2), (3, 5)], 2: [(3, 1)], 3: [(4, 2),(5, 5)], 4: [(5, 5), (2, 3)], 5:[(1, 5)]}
# 1 -> 5: 6
# 2 -> 5: 1
# 3 -> 5: 7
# 4 -> 5: 6

g = Flow(createFacebookGraph(parseFacebookData('./facebook_combined.txt')))
print(g.maxFlow(430, 483))
# g.printGraph()
