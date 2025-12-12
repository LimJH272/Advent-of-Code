from common_functions import read_file
from time import time

def parse_input(raw_input: str):
    temp = [line.split(': ') for line in raw_input.split('\n')]
    return {
        k: [x for x in v.split(' ') if x != '']
        for k,v in temp
    }

def day11_part1(nxt: dict[str, list[str]]) -> int:
    start = 'you'
    target = 'out'
    visited = set()
    curr = [start]

    total = 0
    while len(curr) > 0:
        curr = [n for d in curr for n in nxt[d] if n not in visited or n == target]
        visited.update(curr)
        total += sum(1 for n in curr if n == target)
        curr = [n for n in curr if n != target]
    
    return total

def day11_part2(nxt: dict[str, list[str]]) -> int:
    memo = dict()

    # assume no feedback loops
    def count_paths(curr: str, target: str):
        key = (curr, target)
        if key in memo:
            return memo[key]
        
        result = 1 if curr == target else sum(count_paths(n, target) for n in nxt.get(curr, []))
        memo[key] = result
        return result

    return (
        count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')
    ) + (
        count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')
    )

if __name__ == '__main__':
    inputs = read_file('../inputs/day11.txt')
    next_map = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 11')

    s1 = time()
    part1_ans = day11_part1(next_map)
    e1 = time()
    print(f'Part 1 ({e1-s1:.7f}s):', part1_ans)

    s2 = time()
    part2_ans = day11_part2(next_map)
    e2 = time()
    print(f'Part 2 ({e2-s2:.7f}s):', part2_ans)