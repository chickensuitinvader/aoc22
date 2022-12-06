from collections import deque

def read(fn):
    with open(fn, 'r') as fp:
        ln = fp.readline().strip()
        for char in ln:
            yield char

def part_1(fn):
    working = deque()
    for i, char in enumerate(read(fn)):
        working.append(char)
        if len(set(working)) == 4:
            print(i+1)
            return
        if len(working) == 4:
            working.popleft()
    print('not found')



def part_2(fn):
    working = deque()
    for i, char in enumerate(read(fn)):
        working.append(char)
        if len(set(working)) == 14:
            print(i+1)
            return
        if len(working) == 14:
            working.popleft()
    print('not found')


if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")