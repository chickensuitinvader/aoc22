import numpy as np
import itertools as it

def read(fn):
    with open(fn, 'r') as fp:
        return np.array([list(map(int, ln.strip())) for ln in fp])

def part_1(fn):
    trees = read(fn)

    # brute force
    score = 0
    for i in range(trees.shape[0]):
        for j in range(trees.shape[1]):
            score += (all(trees[i,j] > trees[:i,j]) or
                      all(trees[i,j] > trees[i+1:,j]) or
                      all(trees[i,j] > trees[i,:j]) or
                      all(trees[i,j] > trees[i,j+1:]))
    print(score)

def scene(i, j, trees):
    frags = [trees[:i,j][::-1], trees[i+1:,j], trees[i,:j][::-1], trees[i,j+1:]]
    v = trees[i,j]
    z = 1
    for f in frags:
        s = np.where(v <= f)[0][:1]
        if s.shape[0] == 0:
            z *= len(f)
        else:
            z *= s[0]+1
    return z

def part_2(fn):
    trees = read(fn)

    score = 0
    for i in range(1, trees.shape[0]-1):
        for j in range(1, trees.shape[1]-1):
            z = scene(i, j, trees)
            if z > score:
                score = z
    print(score)

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")