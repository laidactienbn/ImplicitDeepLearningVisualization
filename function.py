import networkx as nx
def center(pos_G, pos_SG):
    x_center = 0
    y_center = 0
    for key in pos_SG.keys():
        x_center += pos_G[key][0]
        y_center += pos_G[key][1]
    x_center = x_center / len(pos_SG.keys())
    y_center = y_center / len(pos_SG.keys())
    return (x_center, y_center)
def size(pos_G):
    max_x = max(pos_G.values(), key=lambda item: item[0])[0]
    max_y = max(pos_G.values(), key=lambda item: item[1])[1]
    min_x = min(pos_G.values(), key=lambda item: item[0])[0]
    min_y = min(pos_G.values(), key=lambda item: item[1])[1]
    return (max_x, max_y, min_x, min_y)
def update_pos(pos_G, pos_SG):
    old_pos = {k: v for (k, v) in pos_G.items() if k in pos_SG.keys()}
    new_pos = {k: v+center(pos_G, pos_SG) for (k, v) in pos_SG.items()}
    old_size = size(old_pos)
    change = tuple(map(lambda i, j: i - j, size(new_pos), old_size))
    for key in pos_G.keys():
        if pos_G[key][0] >= old_size[0]:
            pos_G[key][0] += 3*change[0]
        if pos_G[key][0] <= old_size[2]:
            pos_G[key][0] += 3*change[2]
        if pos_G[key][1] >= old_size[1]:
            pos_G[key][1] += 3*change[1]
        if pos_G[key][1] <= old_size[3]:
            pos_G[key][1] += 3*change[3]

    pos_G.update(new_pos)
    return pos_G


def layer_to_output(graph, subgraph, y):
    hidden_layer = {}
    for node in subgraph:
        output = nx.subgraph(graph, y)
        shortest_path_length = nx.number_of_nodes(graph)

        for i in range(len(list(output))):
            length = len(nx.bidirectional_shortest_path(graph, node, list(output)[i]))
            if length < shortest_path_length:
                shortest_path_length = length
        hidden_layer[node] = shortest_path_length
    num_layer = max(hidden_layer.values())
    for k, v in hidden_layer.items():
        hidden_layer[k] = num_layer - v
    nx.set_node_attributes(subgraph, hidden_layer, 'hidden layer')
    x_pos = nx.multipartite_layout(subgraph, subset_key='hidden layer')
    return x_pos