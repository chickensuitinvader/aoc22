code_for = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',

    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}


beats = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock',
}

loses = {v:k for k,v in beats.items()}

pscore = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

wscore = {
    'win': 6,
    'draw': 3,
    'lose': 0,
}

result = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

def part1(fn):
    score = 0
    with open(fn, 'r') as fp:
        for ln in fp:
            y, m = ln.strip().split(' ')
            cy = code_for[y]
            cm = code_for[m]
            score += pscore[cm]
            if beats[cm] == cy:
                score += wscore['win']
            elif cm == cy:
                score += wscore['draw']
            else:
                score += wscore['lose']
    print(score)

def part2(fn):
    score = 0
    with open(fn, 'r') as fp:
        for ln in fp:
            y, s = ln.strip().split(' ')
            cy = code_for[y]
            r = result[s]
            score += wscore[r]
            if r == 'win':
                score += pscore[loses[cy]]
            elif r == 'draw':
                score += pscore[cy]
            elif r == 'lose':
                score += pscore[beats[cy]]
    print(score)

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part1(sys.argv[1])
    part2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")