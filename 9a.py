from contagion_graph import Graph
from parseFacebook import parseFacebookData, createUndirectedFacebookGraph
from random import randint
#############
# Contagion in an undirected graph
##
###

# @Params: set of early adopts earlyAdopters, threshold q (such that a certain choice X will spread to a node if more than q fraction of its neighbors are playing it)
# @Steps:
# - loop through graph and infect early adopters
# - loop through early adopters and infect all neighbors that are above threshold
#   - use queue to loop through neighbors
#   - track history of visited nodes to make sure not repeating nodes
# - return once queue is empty

###
##
#

def createEarlyAdopterSet(num):
    randomSet = []
    for i in range(0, num):
        x = randint(0, 4038)
        randomSet.append(x)
    return set(randomSet)

g = Graph({1: [2, 3], 2: [1, 3,4], 3: [1, 2, 4], 4: [1, 3]})
g = Graph(createUndirectedFacebookGraph(parseFacebookData('./facebook_combined.txt')))
g.initGraph()
g.infectEarlyAdopters(createEarlyAdopterSet(100), 'X')
threshold = .2
g.brd(threshold)
print('threshold', threshold)
print('X: ', g.countChoice('X'))
print('Y:', g.countChoice('Y'))
