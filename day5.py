from collections import deque
import re

def read(fn):
    with open(fn, 'r') as fp:
        lns = []
        ic_phase = True
        mvs = []
        for ln in fp:
            if ic_phase:
                if ln.strip() != '':
                    lns.append(ln)
                else:
                    keys = [int(i) for i in lns.pop(-1).strip().split()]
                    ic = {k: deque() for k in keys}
                    for lx in lns:
                        for i in keys:
                            j = i-1
                            s = lx[4*j+1]
                            if s != ' ':
                                ic[i].append(s)
                    ic_phase = False
            else:
                mvs.append([int(i) for i in re.match(r"move (.*) from (.*) to (.*)", ln.strip()).groups()])

    return ic, mvs



def part_1(fn):
    ic, mvs = read(fn)

    for n, i, j in mvs:
        for _ in range(n):
            x = ic[i].popleft()
            ic[j].appendleft(x)

    print(''.join(x[0] for x in ic.values()))

def part_2(fn):
    ic, mvs = read(fn)

    for n, i, j in mvs:
        q = []
        for _ in range(n):
            q.append(ic[i].popleft())
        ic[j].extendleft(reversed(q))

    print(''.join(x[0] for x in ic.values()))


if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")