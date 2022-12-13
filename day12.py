import networkx as nx
import string

order = {s: i for i,s in enumerate(string.ascii_lowercase)}
order['S'] = order['a']
order['E'] = order['z']

def read(fn):
    with open(fn, 'r') as fp:
        return [list(ln.strip()) for ln in fp]

def parse(hill):
    G = nx.DiGraph()

    N = len(hill[0])
    a_nodes = []

    # along rows
    for i, row in enumerate(hill):
        # add nodes
        for j in range(N):
            G.add_node((i, j))

            if row[j] == 'S':
                start_node = (i, j)
                a_nodes.append((i, j))
            elif row[j] == 'E':
                end_node = (i, j)
            elif row[j] == 'a':
                a_nodes.append((i,j))

        # LR edges
        for j, (x,y) in enumerate(zip(row[:-1], row[1:])):
            if order[y] - order[x] >= -1:
                G.add_edge((i, j+1), (i, j))
            if order[x] - order[y] >= -1:
                G.add_edge((i, j), (i, j+1))

    # along cols
    for i, (x, y) in enumerate(zip(hill[:-1], hill[1:])):
        for j in range(N):
            if order[x[j]] - order[y[j]] >= -1:
                G.add_edge((i, j), (i+1, j))
            if order[y[j]] - order[x[j]] >= -1:
                G.add_edge((i+1, j), (i, j))

    return G, start_node, end_node, a_nodes

def shortest_path_length(G, start, end):
    try:
        dist = nx.shortest_path_length(G, start, end)
    except nx.NetworkXNoPath:
        return float('inf')
    
    return dist

def part_1(fn):
    hill = read(fn)
    G, start_node, end_node, _ = parse(hill)

    return shortest_path_length(G, start_node, end_node)

def part_2(fn):
    hill = read(fn)
    G, _, end_node, a_nodes = parse(hill)

    dists = [shortest_path_length(G, nd, end_node) for nd in a_nodes]
    return min(dists)

def main(fn):

    print(part_1(fn))
    print(part_2(fn))

if __name__ == "__main__":
    import sys
    main(sys.argv[1])