def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(int(line.strip()))
    return array


def part1_find_wrong_xmas(list: list[int], preamble: int):
    for i in range(preamble, len(list)):
        if not is_sum_of_two(list[i], list[i - preamble : i]):
            return list[i]


def is_sum_of_two(target_number: int, list: list[int]):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == target_number:
                return True
    return False


def part2_find_weakness(encrypt: int, list: list[int]):
    head = 0
    tail = 0
    while tail < len(list):
        sum = 0
        for i in range(head, tail + 1):
            sum += list[i]
        if sum == encrypt:
            return list[head : tail + 1]
        elif sum > encrypt:
            head += 1
            tail = head + 1
        else:
            tail += 1
    return None

def find_sum_min_max_of_list(list: list[int]):
    list.sort()
    return list[0] + list[len(list) - 1]

inputs = read_input("input2.txt")
encrypt = part1_find_wrong_xmas(inputs, 25)

print(encrypt)

weakness_list = part2_find_weakness(encrypt, inputs)
print(weakness_list)
print(find_sum_min_max_of_list(weakness_list))