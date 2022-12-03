def read(fn):
    with open(fn, 'r') as fp:
        cx = []
        for ln in fp:
            ln = ln.strip()
            if ln != '':
                cx.append(int(ln))
            else:
                s = sum(cx)
                cx = []
                yield s
        yield sum(cx)

def part_1(fn):
    print(max(read(fn)))

def part_2(fn):
    max_arr = []
    for v in read(fn):
        max_arr = sorted(max_arr)
        if len(max_arr) < 3:
            max_arr.append(v)
        elif max_arr[0] < v:
            max_arr[0] = v
    print(sum(max_arr))

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")