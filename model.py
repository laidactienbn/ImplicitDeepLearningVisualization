# from Matrices import *
import itertools
import networkx as nx


class Model:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.n_states = len(A)
        self.n_inputs = len(B[0])
        self.n_outputs = len(C)
        subset_sizes = [self.n_inputs, self.n_states, self.n_outputs]
        extents = nx.utils.pairwise(itertools.accumulate((0,) + tuple(subset_sizes)))
        extents = list(extents)
        self.u = list(range(extents[0][0], extents[0][1]))
        self.x = list(range(extents[1][0], extents[1][1]))
        self.y = list(range(extents[2][0], extents[2][1]))
        self.G = self.graph()

    def __str__(self):
        print(self.G, end='')
        return ''


    def graph(self):
        subset_sizes = [self.n_inputs, self.n_states, self.n_outputs]
        extents = nx.utils.pairwise(itertools.accumulate((0,) + tuple(subset_sizes)))
        extents = list(extents)
        layers = [range(start, end) for start, end in extents]
        self.G = nx.DiGraph()
        for (i, layer) in enumerate(layers):
            self.G.add_nodes_from(layer, layer=i)
        self.G = self.input2state()
        self.G = self.state2output()
        self.G = self.state2state()
        return self.G

    def input2state(self):
        for n in range(self.n_states):
            for p in range(self.n_inputs):
                if self.B[n][p]:
                    self.G.add_edge(self.u[p], self.x[n])
        return self.G

    def state2output(self):
        for q in range(self.n_outputs):
            for n in range(self.n_states):
                if self.C[q][n]:
                    self.G.add_edge(self.x[n], self.y[q])
        return self.G

    def state2state(self):
        for n1 in range(self.n_states):
            for n2 in range(self.n_states):
                if self.A[n1][n2]:
                    self.G.add_edge(self.x[n2], self.x[n1])
        return self.G
