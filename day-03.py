def spiral(square):
    if square <= 0:
        return None

    # absolute distance from the origin
    x = 0
    y = 0

    # control direction as we walk the spiral
    direction = 0 # 0 -> right, 1 -> up, 2 -> left, 3 -> down

    def turn_left(d):
        return (d + 1) % 4

    def next_cell(x, y, d):
        if d == 0:
            dx, dy = (1, 0)
        elif d == 1:
            dx, dy = (0, 1)
        elif d == 2:
            dx, dy = (-1, 0)
        elif d == 3:
            dx, dy = (0, -1)

        return (x + dx, y + dy)

    # all cells that have been walked previously
    cells = set()

    # check if the cell to the left is taken
    def left_vaccant(x, y, d):
        new_d = turn_left(d)
        left_cell = next_cell(x, y, new_d)

        return left_cell not in cells
   

    # walk the spiral till we find our goal square
    pos = 1
    while pos < square:

        # add our cell to visited collection
        cells.add((x, y))

        # move to next cell
        pos += 1

        # we always wanna turn left if we can
        if left_vaccant(x, y, direction):
            direction = turn_left(direction)

        # lets move to our next cell, if we have updated direction
        x, y = next_cell(x, y, direction)

    return abs(x) + abs(y)


def spiral_2(square):
    if square <= 0:
        return None

    # absolute distance from the origin
    x = 0
    y = 0

    # control direction as we walk the spiral
    direction = 3 # 0 -> right, 1 -> up, 2 -> left, 3 -> down

    def turn_left(d):
        return (d + 1) % 4

    def next_cell(x, y, d):
        if d == 0: # right
            dx, dy = (1, 0)
        elif d == 1: # up
            dx, dy = (0, 1)
        elif d == 2: # left
            dx, dy = (-1, 0)
        elif d == 3: # down
            dx, dy = (0, -1)

        return (x + dx, y + dy)


    def adjacent_cells(x, y):
        return [(x + dx, y + dy) for (dy, dx) in [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]]

    # all cells that have been walked previously
    cells = {(0, 0): 1}

    # check if the cell to the left is taken
    def left_vaccant(x, y, d):
        new_d = turn_left(d)
        left_cell = next_cell(x, y, new_d)

        return left_cell not in cells

    def cells_sum(cs):
        return sum([cells.get(c, 0) for c in cs])


    # walk the spiral till we find our goal square
    last_value  = 1
    pos = 1
    while pos < square:
        # move to next cell
        pos += 1

        # we always wanna turn left if we can
        if left_vaccant(x, y, direction):
            direction = turn_left(direction)

        # lets move to our next cell, if we have updated direction
        x, y = next_cell(x, y, direction)

        last_value = cells_sum(adjacent_cells(x, y))
        cells[(x, y)] = last_value

    return last_value


if __name__ == "__main__":
    assert spiral(1) == 0
    assert spiral(12) == 3
    assert spiral(23) == 2
    assert spiral(1024) == 31

    square = 325489
    result = spiral(square)

    print("Part 1:", result)

    # --- PART 2 --- #

    assert spiral_2(1) == 1
    assert spiral_2(2) == 1
    assert spiral_2(3) == 2
    assert spiral_2(4) == 4
    assert spiral_2(5) == 5

    for s in range(1, square):
        r = spiral_2(s)
        if r > square:
             print("Part 2:", r)
             break
   


