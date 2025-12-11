from common_functions import read_file
from time import time
from functools import lru_cache

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
    start = 'svr'
    target = 'out'
    memo = dict()

    def path_search(curr: str):
        key = curr[:]
        if key in memo:
            return memo[key]
        
        # last = curr[-1]
        # if last == target:
        #     result = 1 if 'dac' in curr and 'fft' in curr else 0
        #     if result == 1:
        #         print(curr)
        #     memo[key] = result
        #     return result
        
        nxt_paths = []
        for n in nxt.get(curr, []):
            if n == target:
                nxt_paths.append([curr, n])
            else:
                paths = [[curr] + path for path in path_search(n) if curr not in path]
                nxt_paths.extend(paths)
    
        memo[key] = nxt_paths[:]
        return nxt_paths[:]
    
    # def path_search(start: str, target: str, visited: list[str]) -> int:
    #     if (start, tuple(visited)) in memo:
    #         return memo[(start, tuple(visited))]
        
    #     if start in visited:
    #         memo[(start, tuple(visited))] = 0
    #         return 0

    #     new_visited = visited + [start]
    #     if start == target:
    #         result = 1 if 'dac' in new_visited and 'fft' in new_visited else 0
    #         memo[(start, tuple(visited))] = result
    #         return result
        
    #     result = sum(path_search(n, target, new_visited[:]) for n in nxt[start])
    #     memo[(start, tuple(visited))] = result
    #     return result
    
    return len([path for path in path_search(start) if 'dac' in path and 'fft' in path])
    # return path_search(start, target, [])

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