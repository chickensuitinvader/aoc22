"""
Part I
------
Each elf records a value for each item they carry. Elves are separated by newline.
Want to find the elf with the highest total value.

Part II
-------
Same structure as part I.
Want to find the total value of the elves with the three highest values.

Approach: Brute force iteration
"""


def read(fn):
    """Read in newline separated list to a generator per elf"""
    with open(fn, 'r') as fp:
        bag = []
        for ln in fp:
            ln = ln.strip()
            # non empty line, i.e. item with int value
            if ln != '':
                bag.append(int(ln))
            else:
                # empty line signals end of one elf
                elf_value = sum(bag)
                bag = []
                yield elf_value
        # final elf isn't necessarily post-ended by an empty line
        yield sum(bag)

def part_1(fn):
    """Maximise over the elf iterator"""
    print(max(read(fn)))

def part_2(fn):
    """Sum over the top three of the elf iterator
    
    Could do this with sorted and slice, but that could be expensive in memory.
    We instead use a running top three list that gets sorted every iteration 
        (might actually be more expensive computationally).
    """
    max_arr = []
    for elf in read(fn):
        max_arr = sorted(max_arr)
        if len(max_arr) < 3:
            max_arr.append(elf)
        elif max_arr[0] < elf:
            max_arr[0] = elf
    print(sum(max_arr))

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")