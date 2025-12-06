from common_functions import read_file

def parse_input(raw_input: str):
    lines = raw_input.split('\n')
    numbers = [line[:] for line in lines[:-1]]
    operators = [op for op in lines[-1].split(' ') if op != '']
    return numbers, operators

def day6_part1(number_rows: list[str], op_ls: list[str]) -> int:
    new_rows = [[n for n in row.split(' ') if n != ''] for row in number_rows]
    total = 0

    for i in range(len(op_ls)):
        total += eval(op_ls[i].join([row[i] for row in new_rows]))
    
    return total

def day6_part2(number_rows: list[str], op_ls: list[str]) -> int:
    groups = []
    temp = []
    for i in range(len(number_rows[0])):
        curr = ''.join([row[i] for row in number_rows]).strip()
        if curr == '':
            if len(temp) > 0:
                groups.append(temp[:])
            temp = []
        else:
            temp.append(curr)
    
    if len(temp) > 0:
        groups.append(temp)
    
    total = 0
    for nums, op in zip(groups, op_ls):
        total += eval(op.join(nums))
    
    return total
        

if __name__ == '__main__':
    inputs = read_file('../inputs/day6.txt')
    numbers, operators = parse_input(inputs)

    print('\nAdvent of Code 2025 - Day 6')

    part1_ans = day6_part1(numbers, operators)
    print('Part 1:', part1_ans)

    part2_ans = day6_part2(numbers, operators)
    print('Part 2:', part2_ans)