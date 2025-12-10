from common_functions import read_file
from time import time
from sympy import Matrix
import numpy as np

def parse_input(raw_input: str):
    lines = raw_input.split('\n')

    out = []
    for line in lines:
        diag_start = None
        diag_end = None
        btn_start = []
        btn_end = []
        joltage_start = None
        joltage_end = None

        for i in range(len(line)):
            curr = line[i]
            if curr == '[':
                diag_start = i
            elif curr == ']':
                diag_end = i
            elif curr == '(':
                btn_start.append(i)
            elif curr == ')':
                btn_end.append(i)
            elif curr == '{':
                joltage_start = i
            elif curr == '}':
                joltage_end = i
    
        if any([
            diag_start is None,
            diag_end is None,
            len(btn_start) == 0,
            len(btn_end) == 0,
            joltage_start is None,
            joltage_end is None
        ]):
            raise Exception('WTF')
        
        diag = [c == '#' for c in line[diag_start+1:diag_end]]
        btns = [list(map(int, line[s+1:e].split(','))) for s,e in zip(btn_start, btn_end)]
        joltages = list(map(int, line[joltage_start+1:joltage_end].split(',')))

        out.append([diag, btns, joltages])

    return out


def day10_part1(configs: list[list[bool] | list[int] | list[list[int]]]) -> int:
    total = 0
    for diagram, btns, joltages in configs:
        btns = [[k in b for k in range(len(diagram))] for b in btns]
        target = tuple(diagram)
        start = tuple([False for _ in range(len(diagram))])
        visited = set()
        next_nodes = set([start])

        depth = 0
        found = False
        while not found:
            depth += 1
            temp = set([tuple([n^b for n,b in zip(node, btn)]) for node in next_nodes for btn in btns])
            temp = set([n for n in temp if n not in visited])
            found = target in temp
            next_nodes = set() | temp
            visited |= temp
        
        total += depth

    return total

def day10_part2(configs: list[list[bool] | list[int] | list[list[int]]]) -> int:
    total = 0
        

    return total

if __name__ == '__main__':
    inputs = read_file('../inputs/day10.txt')
    lines = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 10')

    s1 = time()
    part1_ans = day10_part1(lines)
    e1 = time()
    print(f'Part 1 ({e1-s1:.7f}s):', part1_ans)

    s2 = time()
    part2_ans = day10_part2(lines)
    e2 = time()
    print(f'Part 2 ({e2-s2:.7f}s):', part2_ans)