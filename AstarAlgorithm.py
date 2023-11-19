

class Graph():
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {node: {} for node in range(self.num_nodes)}
    def add_node(self):
        pass
    def add_edge(self, node1, node2, weight):
        self.graph[node1][node2] = weight





g = Graph(10)