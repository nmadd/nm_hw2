# parse raw facebook data and return list of tuples
def parseFacebookData(file_path):
    graphData = []
    data = open(file_path)
    lines = data.read().splitlines()
    for line in lines:
        graphData.append(line.split())
    return graphData

# take parsed facebook data and create a graph dictionary, which can then be used in the Graph class constructor
def createFacebookGraph(rawData):
    graph = {}
    for pair in rawData:
        node1 = int(pair[0])
        node2 = int(pair[1])
        if node1 not in graph:
            graph[node1] = set()
        # if node2 not in graph:
        #     graph[node2] = set()
        graph[node1].add(node2)
        # graph[node2].add(node1)
    return graph
