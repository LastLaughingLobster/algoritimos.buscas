class Graph:
    def __init__(self):
        self.size = 0
        self.nodes = []
        self._nameCounter = 65 #ASCII CODE
    
    def addNode(self, data = 0, edges = []):
        self.nodes.append({
            "data" : data, 
            "edges" : edges, 
            "name" : self._getNodeName()
            })
    
    def createEdge(self, node1, node2):
        if node1 is None or node2 is None:
            print("Null Pointer Error")
            return
        node1['edges'] = node1['edges'] + [node2]
        node2['edges'] = node2['edges'] + [node1]
    

    def _getNodeName(self):
        out = chr(self._nameCounter)
        self._nameCounter += 1
        return out

    def getNodeByName(self, name):
        for node in self.nodes:
            if node["name"] == name:
                return node
        return None

    def __str__(self):
        return str(self.nodes)
        

    
