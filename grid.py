
def geometry():
    print('grid populator')

    w_grid, h_grid = 400,400

    origin_x = (500 - w_grid)/2
    origin_y = (500 - h_grid)/2

    plots = []

    x1 = origin_x
    y1 = origin_y

    w = w_grid/3
    h = h_grid/3

    i = 0

    while i < 3:
        y2 = y1 + h
        j = 0
        while j < 3:
            x2 = x1 + w
            coords = [[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
            plots.append(coords)
            x1 = x2
            j+=1
        x1 = origin_x
        y1 = y2
        i+=1

    for p in plots:
        print(p)

    # plots = [[50,0],[0,0,],[0,0,],[50,50]]

    return plots
    