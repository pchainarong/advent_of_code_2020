def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        # convert line string to array
        line_array = []

        for i in range(len(line)):
            if line[i] == "\n":
                continue
            line_array.append(line[i])

        array.append(line_array)
    return array


def part1(map, start_point, move_pattern):
    count = 0
    print(start_point)
    print(move_pattern)
    print(len(map))
    next_point = start_point
    step = 0
    while True:
        step += 1
        # get next point
        next_point = [next_point[0] + move_pattern[0], next_point[1] + move_pattern[1]]
        # if next point is end of map, return count
        if next_point[1] >= len(map):
            return count

        # re adjust when next point is end of line
        if next_point[0] >= len(map[next_point[1]]):
            next_point[0] = next_point[0] % len(map[next_point[1]])

        # if next point is tree, count += 1
        if map[next_point[1]][next_point[0]] == "#":
            count += 1

        # if the loop is over than maxlimit 1000 then we exit the loop
        if step > 1000:
            return count


def part2(map, start_point, move_patterns):
    count = 1
    for i in range(len(move_patterns)):
        result = part1(map, start_point, move_patterns[i])

        print("result : {r}".format(r=result))
        count *= result
    return count


start_point = [0, 0]
move_pattern = [3, 1]  # right, down
geology = read_input("input1.txt")
print(part1(geology, start_point, move_pattern))


move_patterns = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
print(part2(geology, start_point, move_patterns))
