import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_all(G):
    for x in range(1,G.number_of_nodes()+1):
        dijkstra_one_to_all(G,x)
    return

def plotGraph(G):
    node_size = [2500 for node in G.nodes]
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=labels)

    options = {
        'width': 1.0,
        'arrowstyle': '-|>',
        'arrowsize': 12,
    }
    nx.draw_networkx(G, pos, arrows=True,
                        with_labels=True, node_size=node_size, **options)

    plt.show()
    return

def dijkstra_one_to_all(G,origem):

    for x in range(1,G.number_of_nodes()+1):
        if x!= origem:
            try:
                length = nx.shortest_path_length(G, source=origem, target=x, weight='weight')
                print("Length of the shortest path from ",origem, " to ",x," : " , length)
            except nx.exception.NetworkXNoPath:
                print('No path from',origem,' to ',x)
    path = nx.shortest_path(G, source=origem, weight='weight')
    del path[origem]
    print("All shortest paths from ",origem,": " ,path )
    return

def dijkstra_one_to_one(G,origem,destino):
    if destino!= origem:
        try:
            length = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')
            print("Length of the shortest path from ",origem, " to ",destino," : " , length)
            path = nx.shortest_path(G, source=origem, target=destino, weight='weight')
            print("The shortest paths from ",origem,"to ",destino," : " ,path )
        except nx.exception.NetworkXNoPath:
            print('No path from',origem,' to ',destino)
    else:
        print("origem = destino")
    return

edges = [(1,2, {'weight':4}),
        (1,3,{'weight':2}),
        (2,3,{'weight':1}),
        (2,4, {'weight':5}),
        (3,4, {'weight':8}),
        (3,5, {'weight':10}),
        (4,5,{'weight':2}),
        (4,6,{'weight':8}),
        (5,6,{'weight':5})]
edge_labels = {(1,2):4, (1,3):2, (2,3):1, (2,4):5, (3,4):8, (3,5):10, (4,5):2, (4,6):8, (5,6):5}
   
        
G = nx.DiGraph()
for i in range(1,7):
    G.add_node(i)
G.add_edges_from(edges)

dijkstra_all(G)
plotGraph(G)

