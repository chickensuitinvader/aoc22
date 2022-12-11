from math import prod
import warnings

warnings.filterwarnings('error')

class Monkey():
    def __init__(self, id):
        self.id = id
        self.items = []
        self.test = 1
        self.operation = lambda x: x
        self.test_true = -1
        self.test_false = -1

    def build_operation(self, s):
        op = s[10]
        arg = s[12:]
        def operation(x):
            if arg == 'old':
                y = x
            else:
                y = int(arg)

            if op == '+':
                return (x + y)
            elif op == '*':
                return (x * y)

        self.operation = operation

def read(fn):
    monkeys = dict()
    with open(fn, 'r') as fp:
        for ln in fp:
            ln = ln.strip()
            if ln.startswith("Monkey"):
                id = ln.removeprefix("Monkey").removesuffix(":")
                monkey = Monkey(int(id))
                monkeys[int(id)] = monkey
            elif ln.startswith("Starting items:"):
                monkey.items = [int(v) for v in ln.removeprefix("Starting items:").split(',')]
            elif ln.startswith("Operation:"):
                monkey.build_operation(ln.removeprefix("Operation: "))
            elif ln.startswith("Test:"):
                monkey.test = int(ln.removeprefix("Test: divisible by "))
            elif ln.startswith("If true"):
                monkey.test_true = int(ln.removeprefix("If true: throw to monkey "))
            elif ln.startswith("If false"):
                monkey.test_false = int(ln.removeprefix("If false: throw to monkey "))
    return monkeys

def part_1(fn):
    monkeys = read(fn)
    inspects = dict.fromkeys(monkeys.keys(), 0)

    for round in range(20):
        for mid, monkey in monkeys.items():
            inspects[mid] += len(monkey.items)
            for item in monkey.items:
                worry = monkey.operation(item) // 3
                if worry % monkey.test == 0:
                    monkeys[monkey.test_true].items.append(worry)
                else:
                    monkeys[monkey.test_false].items.append(worry)
            monkey.items = []


    print(prod(sorted(list(inspects.values()))[-2:]))


def part_2(fn):
    monkeys = read(fn)
    inspects = dict.fromkeys(monkeys.keys(), 0)

    base = prod([m.test for m in monkeys.values()])

    for round in range(10_000):
        for mid, monkey in monkeys.items():
            inspects[mid] += len(monkey.items)
            for item in monkey.items:
                worry = monkey.operation(item) % base
                if worry % monkey.test == 0:
                    monkeys[monkey.test_true].items.append(worry)
                else:
                    monkeys[monkey.test_false].items.append(worry)
            monkey.items = []

    print(prod(sorted(list(inspects.values()))[-2:]))

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")