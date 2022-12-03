def read(fn):
    with open(fn, 'r') as fp:
        pass

def part_1(fn):
    pass

def part_2(fn):
    pass

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")