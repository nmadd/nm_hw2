from contagion_graph import Graph
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

g = Graph({1: [2, 3], 2: [1, 3,4], 3: [1, 2, 4], 4: [1, 3]})
g.initGraph()
g.infectEarlyAdopters(set([2,3]), 'X')
g.brd(.1)
g.printGraph()
