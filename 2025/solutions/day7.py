from common_functions import read_file

def parse_input(raw_input: str):
    lines = raw_input.split('\n')
    start = lines[0].index('S')
    splitters = [[j for j in range(len(line)) if line[j] == '^'] for i in range(1, len(lines)) if '^' in (line := lines[i])]
    return start, splitters

def day7_part1(start: int, splitters: list[int]) -> int:
    curr = set([start])
    count = 0

    for row in splitters:
        temp = set()
        for loc in curr:
            if loc in row:
                temp.update([loc-1, loc+1])
                count += 1
            else:
                temp.add(loc)
        curr = temp
    
    return count


def day7_part2() -> int:
    curr = {start: 1}

    for row in splitters:
        temp = dict()
        for loc in curr:
            if loc in row:
                temp[loc-1] = curr[loc] if (loc-1) not in temp else temp[loc-1] + curr[loc]
                temp[loc+1] = curr[loc] if (loc+1) not in temp else temp[loc+1] + curr[loc]
            else:
                temp[loc] = curr[loc] if loc not in temp else temp[loc] + curr[loc]
        curr = temp
    
    return sum(curr.values())
        

if __name__ == '__main__':
    inputs = read_file('../inputs/day7.txt')
    start, splitters = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 7')

    part1_ans = day7_part1(start, splitters)
    print('Part 1:', part1_ans)

    part2_ans = day7_part2()
    print('Part 2:', part2_ans)