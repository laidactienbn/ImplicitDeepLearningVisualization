import matplotlib.pyplot as plt
import networkx as nx
def draw(graph, pos):
    subset_color = [
        "gold",
        "violet",
        "limegreen",
    ]
    color = [subset_color[data["layer"]] for v, data in graph.nodes(data=True)]
    nx.draw(graph, pos, node_color=color, with_labels=True)
    plt.axis("equal")
    plt.show()
