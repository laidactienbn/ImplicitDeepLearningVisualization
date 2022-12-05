import networkx as nx
import Matrices
from function import *
from draw import *
from model import *

model = Model(Matrices.A, Matrices.B, Matrices.C, Matrices.D)
print(model)

pos = nx.multipartite_layout(model.G, subset_key="layer")
SG = nx.subgraph(model.G, model.x)
x_pos = nx.circular_layout(SG)
x_pos = layer_to_output(model.G, SG, model.y)

pos = update_pos(pos, x_pos)


SG1 = nx.subgraph(model.G, [8,9,10,11])
SG1_pos = nx.circular_layout(SG1)
pos = update_pos(pos, SG1_pos)

SG2 = nx.subgraph(model.G, [5,6,7])
SG2_pos = nx.circular_layout(SG2)
pos = update_pos(pos, SG2_pos)

SG3 = nx.subgraph(model.G, [3,4])
SG3_pos = nx.circular_layout(SG3)
pos = update_pos(pos, SG3_pos)

draw(model.G, pos)

