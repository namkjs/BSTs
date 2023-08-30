import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout


def add_edges(graph, node):
    if node is not None:
        if node.left is not None:
            graph.add_edge(node.key, node.left.key)
            add_edges(graph, node.left)
        if node.right is not None:
            graph.add_edge(node.key, node.right.key)
            add_edges(graph, node.right)

def plot_tree(root):
    graph = nx.DiGraph()
    add_edges(graph, root)
    pos = graphviz_layout(graph)
    nx.draw(graph,pos, with_labels=True, arrows=False)
    plt.show()
