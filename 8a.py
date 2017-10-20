from flow import Flow
from parseFacebook import parseFacebookData, createFacebookGraph

figure5_1 = {0: [(1, 1), (2, 3)], 1: [(2, 2), (3, 1)], 2: [(3, 1)], 3: []}
figure5_3 = {0: [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], 1: [(7, 1)], 2: [(6, 1), (7, 1)], 3: [(6, 1)], 4: [(8, 1), (10, 1)], 5: [(8, 1), (9,1)], 6:[(11, 1)], 7:[(11, 1)], 8:[(11, 1)], 9:[(11, 1)], 10: [(11, 1)], 11: []}

figure5_1flow = Flow(figure5_1, True)
print('Figure 5.1 max flow: {}'.format(figure5_1flow.maxFlow(0, 3)))

figure5_3flow = Flow(figure5_3, True)
print('Figure 5.3 max flow: {}'.format(figure5_3flow.maxFlow(0, 11)))
