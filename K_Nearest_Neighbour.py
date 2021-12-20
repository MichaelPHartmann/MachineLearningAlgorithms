# Only import what we need for data visualisation
import matplotlib.pyplot as plt

def squareroot(num):
    result = num ** (1 / 2)
    return result

class kNearestNeighbour():
    # We will use cylinders and weight to predict build location of cars
    def __init__(self, k=5):
        self.nodes = []
        self.node_distances = []
        self.nodes_closest = []
        self.k = k
        self.test_node = None

    class node():
        def __init__(self, feature_a, feature_b, label=None):
            # Cylinders will be the X axis
            self.a = feature_a
            # Weight will be the Y axis
            self.b = feature_b
            self.label = label
            self.coordinates = (self.a, self.b)
            self.index = self.a * self.b

    def submit_training_data(self, a, b, label):
        g = self.node(a, b, label)
        self.nodes.append(g)
        return g

    def make_test_node(self, a, b):
        h = self.node(a, b)
        self.test_node = h

    def compute_two_d_euclidean_distance(self, p, q):
        # Takes two node objects
        euclidean_distance = squareroot(((q.a - p.a)**2) + ((q.b - p.b)**2))
        return euclidean_distance

    def nearest_neighbours(self):
        # Find distances of all nodes
        for n in self.nodes:
            distance = self.compute_two_d_euclidean_distance(n, self.test_node)
            self.node_distances.append((n, distance))
        self.node_distances.sort(key=lambda tup: tup[1])
        self.nodes_closest = []
        for i in range(self.k):
            self.nodes_closest.append(self.node_distances[i][0])
        return self.nodes_closest

    def label_test_node(self):
        label_freguency = {}
        for n in self.nodes_closest:
            if n.label in label_freguency.keys():
                 label_freguency[n.label] += 1
            else:
                label_freguency[n.label] = 1
        highest_frequency = 0
        top_label = 0
        for l, f in label_freguency.items():
            if f > highest_frequency:
                highest_frequency = f
                top_label = l
        self.test_node.label = top_label
        return top_label

    def add_test_node_train_nodes(self):
        a = self.test_node.a
        b = self.test_node.b
        label = self.test_node.label
        self.submit_training_data(a, b, label)

    def train_drain_node(self, a, b):
        self.make_test_node(a, b)
        self.nearest_neighbours()
        # print(F"The nearest neighbours are {self.nodes_closest}")
        self.label_test_node()
        self.add_test_node_train_nodes()

    def visualise_data(self):
        x = []
        y = []
        colors = []
        for node in self.nodes:
            x.append(node.a)
            y.append(node.b)
            colors.append(node.label)
        plt.scatter(x,y, c=colors)
        plt.show()
