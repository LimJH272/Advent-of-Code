from common_functions import read_file

def parse_map(raw_input: str) -> list[str]:
    return raw_input.split('\n')

def day4_part1(m: list[str]) -> int:
    height = len(m)
    width = len(m[0])

    total = 0
    for i in range(height):
        for j in range(width):
            if m[i][j] == '@':
                candidates = [
                    (i-1, j-1),
                    (i-1, j),
                    (i-1, j+1),
                    (i, j-1),
                    (i, j+1),
                    (i+1, j-1),
                    (i+1, j),
                    (i+1, j+1),
                ]
                candidates = [(h,k) for h,k in candidates if 0 <= h < height and 0 <= k < width]

                if sum(1 for h,k in candidates if m[h][k] == '@') < 4:
                    total += 1
    
    return total

def day4_part2(m: list[str]) -> int:
    height = len(m)
    width = len(m[0])

    new_map = [list(row) for row in m]

    total = 0 
    last_removed = height * width
    while last_removed > 0:
        curr = 0
        for i in range(height):
            for j in range(width):
                if new_map[i][j] == '@':
                    candidates = [
                        (i-1, j-1),
                        (i-1, j),
                        (i-1, j+1),
                        (i, j-1),
                        (i, j+1),
                        (i+1, j-1),
                        (i+1, j),
                        (i+1, j+1),
                    ]
                    candidates = [(h,k) for h,k in candidates if 0 <= h < height and 0 <= k < width]

                    if sum(1 for h,k in candidates if new_map[h][k] == '@') < 4:
                        curr += 1
                        new_map[i][j] = '.'
        
        total += curr
        last_removed = curr
    
    return total

if __name__ == '__main__':
    inputs = read_file('../inputs/day4.txt')
    roll_map = parse_map(inputs)

    print('\nAdvent of Code 2025 - Day 4')

    part1_ans = day4_part1(roll_map)
    print('Part 1:', part1_ans)

    part2_ans = day4_part2(roll_map)
    print('Part 2:', part2_ans)