from classy.Graph import Graph


def main():
    showDephSearchImplementation()
    

def showDephSearchImplementation():
    g = Graph()
    g.addNode("Batata") #A
    g.addNode("Feijao") #B
    g.addNode("Arroz")  #C
    g.addNode("Carne")  #D
    g.addNode("Leite")  #E
    g.createEdgeByName('A', 'B')
    g.createEdgeByName('A', 'C')
    g.createEdgeByName('B', 'C')
    g.createEdgeByName('C', 'A')
    g.createEdgeByName('C', 'D')
    g.createEdgeByName('D', 'D')
    g.createEdgeByName('E', 'D')

    nodeToSearch = g.getNodeByName('D')
    targetNode = 'E'

    print("DFS Starting by node {}".format(nodeToSearch["name"]))
    g.dephSearchFirst(nodeToSearch, targetNode)

main()
