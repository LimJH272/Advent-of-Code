from common_functions import read_file

def parse_input(raw_input: str):
    ranges_raw, id_list_raw = raw_input.split('\n\n')
    
    ranges = [[int(n) for n in line.split('-')] for line in ranges_raw.split('\n')]
    id_list = [int(line) for line in id_list_raw.split('\n')]

    return ranges, id_list

def day5_part1(ranges: list[list[int]], id_list: list[int]) -> int:
    total = 0
    for i in id_list:
        for lower, upper in ranges:
            if lower <= i <= upper:
                total += 1
                break
    
    return total

def day5_part2(ranges: list[list[int]]) -> int:
    combined_ranges = []
    for lower, upper in ranges:
        candidate = [lower, upper]

        i = 0
        while i < len(combined_ranges):
            l1, u1 = candidate
            l2, u2 = combined_ranges[i]

            if not (u1 < l2 or u2 < l1):
                combined_ranges.pop(i)
                candidate = [min(l1, l2), max(u1, u2)]
            else:
                i += 1
        
        combined_ranges.append(candidate[:])
    
    return sum(u-l+1 for l,u in combined_ranges)



if __name__ == '__main__':
    inputs = read_file('../inputs/day5.txt')
    ranges, id_list = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 5')

    part1_ans = day5_part1(ranges, id_list)
    print('Part 1:', part1_ans)

    part2_ans = day5_part2(ranges)
    print('Part 2:', part2_ans)