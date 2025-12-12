from common_functions import read_file
from time import time

def parse_input(raw_input: str):
    temp = raw_input.split('\n\n')
    presents = [[[1 if c == '#' else 0 for c in list(row)] for row in r.split(':\n')[1].split('\n')] for r in temp[:-1]]
    dim_nums =[row.split(': ') for row in temp[-1].split('\n')]
    raw_dims, raw_nums = list(zip(*dim_nums))
    dims = [tuple(map(int, d.split('x'))) for d in raw_dims]
    num_presents = [tuple(map(int, c.split(' '))) for c in raw_nums]

    return presents, dims, num_presents

def day12_part1(present_ls: list[list[list[int]]], dim_ls: list[list[int]], num_ls: list[list[int]]) -> int:
    def rotate_left(present: list[list[int]]):
        h, w = len(present), len(present[0])
        return [[present[i][w-j-1] for i in range(h)] for j in range(w)]

    def rotate_right(present: list[list[int]]):
        h, w = len(present), len(present[0])
        return [[present[h-i-1][j] for i in range(h)] for j in range(w)]

    def flip_horizontal(present: list[list[int]]):
        h, w = len(present), len(present[0])
        return [[present[h-i-1][j] for j in range(w)] for i in range(h)]

    def flip_vertical(present: list[list[int]]):
        h, w = len(present), len(present[0])
        return [[present[i][w-j-1] for j in range(w)] for i in range(h)]
    
    def flip_diagonal_left(present: list[list[int]]):
        h, w = len(present), len(present[0])
        return [[present[h-i-1][w-j-1] for i in range(h)] for j in range(w)]
    
    def flip_diagonal_right(present: list[list[int]]):
        h, w = len(present), len(present[0])
        return [[present[i][j] for i in range(h)] for j in range(w)]
    
    present_combis = [[
        present[:],
        rotate_right(present),
        rotate_right(rotate_right(present)),
        rotate_left(present),
        flip_horizontal(present),
        flip_vertical(present),
        flip_diagonal_left(present),
        flip_diagonal_right(present),
    ] for present in present_ls]

    areas = [sum(n for r in present for n in r) for present in present_ls]

    memo = dict()

    def fit_presents(present_idx_ls: list[int], placed: set[tuple[int]], height: int, width: int):
        print(len(present_idx_ls))
        if len(present_idx_ls) == 0:
            return True
        
        presents_to_try = present_combis[present_idx_ls[0]]

        for present in presents_to_try:
            h,w = len(present), len(present[0])

            for i in range(height-h+1):
                for j in range(width-w+1):
                    key = (i,j,h,w)
                    if key in memo:
                        target = memo[key]
                    else:
                        target = [(pi, pj, i+pi, j+pj) for pi in range(h) for pj in range(w)]
                        memo[key] = target
                    
                    can_fit = all(not (present[pi][pj] == 1 and (ti, tj) in placed) for pi, pj, ti, tj in target)

                    if can_fit:
                        for pi, pj, ti, tj in target:
                            if present[pi][pj] == 1:
                                placed.add((ti, tj))
                        
                        if fit_presents(present_idx_ls[1:], set() | placed, height, width):
                            return True

        return False    
    
    total = 0
    for dim, num_presents in zip(dim_ls, num_ls):
        height, width = dim
        if height * width < sum(n * areas[i] for i,n in enumerate(num_presents)):
            continue
        if height * width >= sum(num_presents) * 9:
            total += 1
            continue

        present_queue = [i for i,n in enumerate(num_presents) for _ in range(n)]
        if fit_presents(present_queue, set(), height, width):
            total += 1

    return total

def day12_part2(present_ls: list[list[list[str]]], dim_ls: list[list[int]], num_ls: list[list[int]]) -> int:
    pass

if __name__ == '__main__':
    inputs = read_file('../inputs/day12.txt')
    presents, dims, num_presents = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 12')

    s1 = time()
    part1_ans = day12_part1(presents, dims, num_presents)
    e1 = time()
    print(f'Part 1 ({e1-s1:.7f}s):', part1_ans)

    s2 = time()
    part2_ans = day12_part2(presents, dims, num_presents)
    e2 = time()
    print(f'Part 2 ({e2-s2:.7f}s):', part2_ans)