from contagion_graph import Graph
from parseFacebook import parseFacebookData, createUndirectedFacebookGraph
from random import randint

graph3_1a = Graph({1: [2], 2: [1, 3], 3: [2, 4], 4: [3]})
graph3_1a_early_adopters = {1, 2}
graph3_1b = Graph({1: [2], 2: [1, 3, 4], 3: [2], 4: [2, 5, 6], 5: [4], 6: [4, 7], 7: [6]})
graph3_1b_early_adopters = {1, 2, 3}

print('3_1a Tests:')
for q in [x / 100.0 for x in range(45, 55, 1)]:
    print(graph3_1a.findAverageBrd(1, q, graph3_1a_early_adopters))

print('3_1b Tests:')
for q in [x / 100.0 for x in range(30, 40, 1)]:
    print(graph3_1b.findAverageBrd(1, q, graph3_1b_early_adopters))
