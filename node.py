#Node object containing the shapely box, f, g and the parent node coords
class Node:
    def __init__(self, box_object, f, g, parent):
        self.box_object = box_object
        self.f = f
        self.g = g
        self.parent = parent

#Function to find the valid neighbor nodes of a specific node,
#and the cost of moving to that node (g-cost).
def neighborNodes(node):
    neighbors = []
    #TODO: check for valid nodes, add them to neighbors
    

    cost = 1 #TODO: change cost later if necessary
    for neighbor in neighbors:
        neighbor.g = node.g + cost #update cost
        neighbor.parent = node #if we move to a node, the current node will be its parent
    return neighbors



