from common_functions import read_file

def parse_banks(raw_input: str) -> list[str]:
    return raw_input.split('\n')

def day3_part1(banks: list[str]) -> int:
    total = 0

    for bank in banks:
        mid = str(max(int(c) for c in bank))
        mid_pos = bank.index(mid)
        left = str(max(int(c) for c in bank[:mid_pos])) if mid_pos > 0 else ''
        right = str(max(int(c) for c in bank[mid_pos+1:])) if mid_pos < len(bank)-1 else ''
        largest = max(int(left+mid), int(mid+right))
        total += largest

    return total

def day3_part2() -> int:
    total = 0

    for bank in banks:
        length = len(bank)
        curr = ''
        start = 0
        while len(curr) < 12:
            end = length - (12 - len(curr))
            query = bank[start:end+1]
            largest = max(int(c) for c in query)
            curr += str(largest)
            start = query.index(str(largest))+1+start

        total += int(curr)

    return total


if __name__ == '__main__':
    inputs = read_file('../inputs/day3.txt')
    banks = parse_banks(inputs)

    print('\nAdvent of Code 2025 - Day 3')

    part1_ans = day3_part1(banks)
    print('Part 1:', part1_ans)

    part2_ans = day3_part2()
    print('Part 2:', part2_ans)