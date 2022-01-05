import math

if __name__ == '__main__':
    import seacharts
    from numpy import linalg as LA
    import numpy as np
    from shapely.geometry import Point
    from shapely.geometry import box
    import AStar
    import node
    from node import Node

    size = 10000, 10062                # w, h (east, north) distance in meters
    center = 204832, 7090220          # easting/northing (UTM zone 33N)
    files = ['Basisdata_50_Trondelag_25833_Dybdedata_FGDB.gdb']  # Norwegian county database name

    enc = seacharts.ENC(size=size, center=center, files=files, new_data=False)

    #bottom left corner point of map
    corner_point = center[0]-size[0]/2, center[1]-size[1]/2

    #number of nodes for each side
    resolution = 30
    #size in meters of each grid cell
    node_size = size[0]/resolution, size[1]/resolution

    start_coords = (204833, 7090221)
    #enc.draw_circle(start_coords,50,'yellow', thickness=2)
    start_point = Point(start_coords)

    end_coords = (201033, 7094121)
    #enc.draw_circle(end_coords, 50, 'green', thickness=2)
    end_point = Point(end_coords)

    #enc.draw_arrow(start_coords, end_coords, 'orange',
    #               head_size=100, width=20, thickness=2)

    #Diagonal distance since we can move in 8 directions
    #Note: If we limit ourselves to moving in 4 directions, use Manhattan distance.
    #TODO: make h function
    #dx = abs(start_coords[0]-end_coords[0])
    #dy = abs(start_coords[1]-end_coords[1])

    #movement cost c
    c = 1

    #heuristic h
    #h = c*max(dx,dy)
    h = c*start_point.distance(end_point)

    #Euclidean distance when we can move in any direction
    #Note: sqrt is expensive, use h**2 instead.
    #h = math.sqrt((start_coords[0]-end_coords[0])**2
                  #+ (start_coords[1]-end_coords[1])**2)
    #print("h: ", h)





    #exampleNode = Node(1,2,(-1,-1))
    #print(exampleNode.parent)


    #initialize grid of nodes
    nodes = []

    #creates an nxn box object b, draws it in the figure and adds it to the list rectangles
    for i in range(resolution):
        for j in range(resolution):
            #don't think about why it works, it just does
            b = box(corner_point[0] + j * node_size[0], corner_point[1] + i * node_size[1],
                    corner_point[0] + node_size[0] + j*node_size[0], corner_point[1] + node_size[1] + i * node_size[1])

            node = Node(b, 0, 0, (j, i))

            #TODO: case, not if
            #draw grid w. colors
            """
            if b.intersects(enc.land.geometry):
                #enc.draw_polygon(b, 'red', fill=True)
                x=1
            elif b.intersects(enc.shore.geometry):
                #enc.draw_polygon(b, 'orange', fill=True)
                x=1
            else:
                x=1
                #enc.draw_polygon(b, 'cyan', fill=False)

            #draw start and end points
            if b.intersects(start_point):
                #enc.draw_polygon(b, 'green', fill=True)
                x=1
            elif b.intersects(end_point):
                x=1
                #enc.draw_polygon(b, 'green', fill=True)
            """

            nodes.append(node)

    nodes2d = np.reshape(nodes, (resolution, resolution))

    for row in nodes2d:
        for cell in row:
            if cell.box_object.intersects(enc.land.geometry):
                enc.draw_polygon(cell.box_object, 'red', fill=True)

            elif cell.box_object.intersects(enc.shore.geometry):
                enc.draw_polygon(cell.box_object, 'orange', fill=True)
            else:
                enc.draw_polygon(cell.box_object, 'cyan', fill=False)

                # draw start and end points
            if cell.box_object.intersects(start_point):
                enc.draw_polygon(cell.box_object, 'green', fill=True)
            elif cell.box_object.intersects(end_point):
                enc.draw_polygon(cell.box_object, 'green', fill=True)

    enc.show_display()
