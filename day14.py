SOURCE= (500, 0)

def read(fn):
    all_points = [SOURCE]
    walls = set()
    with open(fn, 'r') as fp:
        for ln in fp:
            ln = ln.strip().split(' -> ')
            wall = []
            for seg in ln:
                pos = tuple(map(int, seg.split(',')))
                all_points.append(pos)
                wall.append(pos)
            for p0, p1 in zip(wall[:-1], wall[1:]):
                p0, p1 = sorted([p0, p1])
                for x in range(p0[0], p1[0]+1):
                    for y in range(p0[1], p1[1]+1):
                        walls.add((x, y))
    bounds = {'x': (min(v[0] for v in all_points), max(v[0] for v in all_points)),
              'y': (min(v[1] for v in all_points), max(v[1] for v in all_points))}
    return bounds, walls

def sand_fall(pos, filled):
    x, y = pos
    down =  (x, y+1) in filled
    left = (x-1, y+1) in filled
    right = (x+1, y+1) in filled
    if down and left and right:
        return None
    if not down:
        return (x, y+1)
    if not left:
        return (x-1, y+1)
    if not right:
        return (x+1, y+1)
    raise RuntimeError("logic has failed")

def out_of_bounds(pos, bounds):
    x, y = pos
    left =  x < bounds['x'][0]
    right = x > bounds['x'][1]
    down = y > bounds['y'][1]
    # ignore up since particles fall down

    if left or right or down:
        return True

    return False

glyph = {
    True: 'x',
    False: '.',
}

def pprint(state, bounds):
    x0, x1 = bounds['x']
    y0, y1 = bounds['y']

    for y in range(y0, y1+1):
        print(''.join([glyph[(x, y) in state] for x in range(x0, x1+1)]))

def part_1(fn):
    bounds, walls = read(fn)
    IC = len(walls)
    state = walls

    quit = False
    while not quit:
        # new sand particle
        pos = SOURCE
        while pos is not None:
            new = sand_fall(pos, state)
            if new is None:
                state.add(pos)
                break
            if out_of_bounds(new, bounds):
                quit = True
                break
            pos = new

    print(len(state) - IC)
    # pprint(state, bounds)

def part_2(fn):
    bounds, walls = read(fn)
    floor = bounds['y'][1] + 2
    floor_x = (500 - floor - 1, 500 + floor + 1)
    # add floor
    bounds['x'] = (min(bounds['x'][0], floor_x[0]), max(bounds['x'][1], floor_x[1]))
    bounds['y'] = (0, floor)
    walls.update(((x, floor) for x in range(floor_x[0], floor_x[1]+1)))

    IC = len(walls)
    state = walls

    quit = False
    while not quit:
        # new sand particle
        pos = SOURCE
        while pos is not None:
            new = sand_fall(pos, state)
            if new is None:
                if pos == SOURCE:
                    quit = True
                state.add(pos)
                break
            pos = new

    print(len(state) - IC)
    # pprint(state, bounds)

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")
