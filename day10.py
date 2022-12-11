def read(fn):
    with open(fn, 'r') as fp:
        for ln in fp:
            op, *val = ln.strip().split(' ')
            yield op, [int(v) for v in val]

def check(t):
    return t in (20, 60, 100, 140, 180, 220)

def part_1(fn):
    t = 1
    x = 1
    s = 0
    for op, val in read(fn):
        if check(t):
            s += x * t
        t += 1
        if op == 'noop':
            pass
        elif op == 'addx':
            if check(t):
                s += x * t
            t += 1
            x += val[0]
    print(s)

def render(t, x, screen):
    p = (t-1) % 40
    is_visible = p in (x-1, x, x+1)
    if is_visible:
        screen[-1].append('#')
    else:
        screen[-1].append('.')
    if p == 39:
        screen.append([])

def part_2(fn):
    screen = [[]]
    t = 1
    x = 1
    for op, val in read(fn):
        render(t, x, screen)
        t += 1
        if op == 'noop':
            pass
        elif op == 'addx':
            render(t, x, screen)
            t += 1
            x += val[0]
    for row in screen:
        print(''.join(row))


if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")