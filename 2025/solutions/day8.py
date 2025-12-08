from common_functions import read_file
from time import time

def parse_input(raw_input: str):
    return [[int(n) for n in line.split(',')] for line in raw_input.split('\n')]

def day8_part1(pos_ls: list[list[int]]) -> int:
    pos_dis = [(i, j, sum((x1-x2) ** 2 for x1, x2 in zip(pos_ls[i], pos_ls[j])) ** 0.5) for i in range(len(pos_ls)) for j in range(i+1, len(pos_ls))]
    top_pos_dis = sorted(pos_dis, key=lambda t: t[2])[:1000]

    circuits: list[set[int]] = []
    for i, j, dis in top_pos_dis:
        if len(circuits) == 0:
            circuits.append(set([i,j]))
        else:
            k_ls = []
            for k in range(len(circuits)):
                s = circuits[k]
                if i in s or j in s:
                    k_ls.append(k)
                if len(k_ls) == 2:
                    break
            
            if len(k_ls) == 2:
                k1, k2 = k_ls
                s1 = circuits.pop(k1)
                s2 = circuits.pop(k2-1)
                circuits.append(s1 | s2)
            elif len(k_ls) == 1:
                circuits[k_ls[0]].update([i,j])
            else:
                circuits.append(set([i,j]))   
        
    sorted_circuit_lens = sorted([len(c) for c in circuits], reverse=True)
    
    return eval('*'.join([str(l) for l in sorted_circuit_lens[:3]]))

def day8_part2(pos_ls: list[list[int]]) -> int:
    pos_dis = [(i, j, sum((x1-x2) ** 2 for x1, x2 in zip(pos_ls[i], pos_ls[j])) ** 0.5) for i in range(len(pos_ls)) for j in range(i+1, len(pos_ls))]
    top_pos_dis = sorted(pos_dis, key=lambda t: -t[2])

    circuits: list[set[int]] = []
    while not (len(circuits) == 1 and len(circuits[0]) == len(pos_ls)):
        i, j, dis = top_pos_dis.pop()
    
        if len(circuits) == 0:
            circuits.append(set([i,j]))
        else:
            k_ls = []
            for k in range(len(circuits)):
                s = circuits[k]
                if i in s or j in s:
                    k_ls.append(k)
                if len(k_ls) == 2:
                    break

            if len(k_ls) == 2:
                k1, k2 = k_ls
                s1 = circuits.pop(k1)
                s2 = circuits.pop(k2-1)
                circuits.append(s1 | s2)
            elif len(k_ls) == 1:
                circuits[k_ls[0]].update([i,j])
            else:
                circuits.append(set([i,j]))  
    
    return pos_ls[i][0] * pos_ls[j][0]
        

if __name__ == '__main__':
    inputs = read_file('../inputs/day8.txt')
    positions = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 8')

    s1 = time()
    part1_ans = day8_part1(positions)
    e1 = time()
    print(f'Part 1 ({e1-s1:.7f}s):', part1_ans)

    s2 = time()
    part2_ans = day8_part2(positions)
    e2 = time()
    print(f'Part 2 ({e2-s2:.7f}s):', part2_ans)