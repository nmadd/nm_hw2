class Node:
    def __init__(self, val, choice='Y'):
        self.val = val
        self.choice = choice
        self.edges = set()

    def __repr__(self):
        return "<Node val:%s choice:%s edges:%s>" % (self.val, self.choice, self.edges)
