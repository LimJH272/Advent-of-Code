from common_functions import read_file
from time import time

def parse_input(raw_input: str):
    return [[int(n) for n in line.split(',')] for line in raw_input.split('\n')]

def day9_part1(pos_ls: list[list[int]]) -> int:
    areas = [eval('*'.join([str(abs(xi-xj)+1) for xi, xj in zip(pos_ls[i], pos_ls[j])])) for i in range(len(pos_ls)) for j in range(i+1, len(pos_ls))]
    return max(areas)

def day9_part2(pos_ls: list[list[int]]) -> int:
    boundary_pts = set()

    for i in range(len(pos_ls)):
        var_axis = 1 if pos_ls[i-1] == pos_ls[i][0] else 0
        const_val = pos_ls[i][1-var_axis]

        min_val = min(pos_ls[i-1][var_axis], pos_ls[i][var_axis])
        max_val = max(pos_ls[i-1][var_axis], pos_ls[i][var_axis])
        for k in range(min_val, max_val):
            temp = [0,0]
            temp[var_axis] = k
            temp[1-var_axis] = const_val
            boundary_pts.add(tuple(temp))
        
    areas = []
    for i in range(len(pos_ls)):
        for j in range(i+1, len(pos_ls)):
            min_x = min(pos_ls[i][0], pos_ls[j][0])
            max_x = max(pos_ls[i][0], pos_ls[j][0])
            min_y = min(pos_ls[i][1], pos_ls[j][1])
            max_y = max(pos_ls[i][1], pos_ls[j][1])

            if not any((min_x < h < max_x) and (min_y < k < max_y) for h,k in boundary_pts):
                areas.append((max_x-min_x+1) * (max_y-min_y+1))
    
    return max(areas)

if __name__ == '__main__':
    inputs = read_file('../inputs/day9.txt')
    positions = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 9')

    s1 = time()
    part1_ans = day9_part1(positions)
    e1 = time()
    print(f'Part 1 ({e1-s1:.7f}s):', part1_ans)

    s2 = time()
    part2_ans = day9_part2(positions)
    e2 = time()
    print(f'Part 2 ({e2-s2:.7f}s):', part2_ans)