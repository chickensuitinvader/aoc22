from collections import deque
import re
import os

def osjoin(a, b):
    return f"{a if not a in ['/', None] else ''}/{b}"

def osparent(a):
    if a == '/':
        return None
    else:
        return os.path.dirname(a)

def build_fs(fn):
    at_dir = '/'
    fs = {at_dir: 0}
    with open(fn, 'r') as fp:
        ln = fp.readline().strip()
        while len(ln):
            if ln.startswith("$ cd"):
                to = ln[5:]
                if to == '/':
                    at_dir = '/'
                elif to == '..':
                    at_dir = osparent(at_dir)
                else:
                    at_dir = osjoin(at_dir, to)
                ln = fp.readline().strip()
            elif ln.startswith("$ ls"):
                ln = fp.readline().strip()
                while len(ln) and ln[0] != '$':
                    sz, nm = ln.split(' ')
                    if sz == 'dir':
                        fs[osjoin(at_dir, nm)] = 0
                    else:
                        par = at_dir
                        while par is not None:
                            fs[par] += int(sz)
                            par = osparent(par)
                    ln = fp.readline().strip()
            else:
                print(f"Trouble Parsing: {ln}")
                ln = fp.readline().strip()

    return fs

def part_1(fs):
    print(sum(fi for fi in fs.values() if fi < 100_000))

def part_2(fn):
    unused = 70_000_000 - fs['/']
    req = 30_000_000 - unused
    ord_list = sorted(v for v in fs.values() if v >= req)
    print(ord_list[0])

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    fs = build_fs(sys.argv[1])
    part_1(fs)
    part_2(fs)
    print(f"Took {time.perf_counter() - tic} s")