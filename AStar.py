import node
from node import Node


# TODO: implement the A* algorithm in here.
# Only needs start and end nodes: (start_j, start_i), (end_j, end_i)
# Returns the path, which can be drawn later (?)
# TODO: make a function that changes coordinates to node indexes, this makes more sense as input
def AStar(start_node, end_node):
    # start_node = start_coords/something
    open_list = [start_node]  # list of nodes in the optimal path, from start to end
    return False


# Constructs a list of all nodes in the optimal path from start to end node
def construct_path(end_node):
    path = [end_node]
    while end_node.parent:
        end_node = end_node.parent
        path.append(end_node)
    return path
