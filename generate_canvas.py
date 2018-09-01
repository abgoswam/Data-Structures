import numpy as np

def get_neighbors(canvas, i, j):
    h, w = canvas.shape
    neighbors = []

    if j + 1 < w:
        neighbors.append((i, j + 1))
    if j - 1 >= 0:
        neighbors.append((i, j - 1))
    if i + 1 < h:
        neighbors.append((i + 1, j))
    if i - 1 >= 0:
        neighbors.append((i - 1, j))

    return neighbors


def color_canvas(canvas, i, j, new_color):
    color_i_j = canvas[i, j]
    neighbors_i_j = get_neighbors(canvas, i, j)

    # this is to make sure our invariant is correct
    # we only want to color if new color is different from current pixel
    if color_i_j == new_color:
        return

    canvas[i, j] = new_color
    for neigh in neighbors_i_j:
        color_neigh = canvas[neigh[0], neigh[1]]
        if color_neigh == color_i_j:
            color_canvas(canvas, neigh[0], neigh[1], new_color)

    return


h = int(input("Enter height:"))
w = int(input("Enter width:"))

print("Height:{0} Width:{1}".format(h, w))

# canvas = np.random.randint(0, 2, size=(h, w))
canvas = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 0, 1],
    [1, 0, 2, 2, 0, 1],
    [1, 0, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1]])
print(canvas)
print(canvas.shape)

color_canvas(canvas, 4, 3, 0)
print(canvas)

