from classy.Graph import Graph


def main():
    g = Graph()
    g.addNode(3)
    g.addNode(4)
    g.createEdge(g.getNodeByName('A'), g.getNodeByName('B'))
    a = g.getNodeByName('A')
    print("NODE --> {}".format(a))





main()