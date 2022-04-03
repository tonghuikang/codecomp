from template_networkx import networkx as nx
from template_networkx import check_planarity


def test_check_planarity():

    g = nx.Graph()
    for i in range(5):
        for j in range(i + 1, 4):
            g.add_edge(i, j)
    assert check_planarity(g, counterexample=True)[0] == True

    g = nx.Graph()
    for i in range(5):
        for j in range(i + 1, 5):
            g.add_edge(i, j)
    assert check_planarity(g)[0] == False

    g = nx.Graph()
    for i in range(0, 3):
        for j in range(3, 6):
            g.add_edge(i, j)
    assert check_planarity(g)[0] == False

