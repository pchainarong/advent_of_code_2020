def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(int(line.strip()))
    return array

one_jolt = 0
two_jolt = 0
three_jolt = 0

def get_diff_array(sorted_input_list):
    global one_jolt
    global two_jolt
    global three_jolt
    output_list = []
    start_jolt = 0
    # print(sorted_input_list, len(sorted_input_list) )
    for i in range(len(sorted_input_list)):
        if i == 0:
            diff = sorted_input_list[i] - start_jolt
        else:
            diff = sorted_input_list[i] - sorted_input_list[i-1]

        print(i, sorted_input_list[i], sorted_input_list[i -1], diff)
        if diff == 1:
            one_jolt += 1
        elif diff == 2:
            two_jolt += 1
        elif diff == 3:
            three_jolt += 1

        output_list.append(diff)

    # add last diff, as per description
    three_jolt += 1
    output_list.append(3)

    return output_list


def find_possible_arrangements(diff_arrays):
    possible = 1
    connected_one = 0
    for i in range(len(diff_arrays)):
        if diff_arrays[i] == 1:
            connected_one += 1
        elif diff_arrays[i] == 3:
            if connected_one > 1:
                # print (2 ** connected_one)
                possible *= cheat_operator(connected_one)
            connected_one = 0

        print(i, diff_arrays[i], connected_one, possible)

    return possible

def flag_operator(input):
    if input == 1 or input == 0:
        return 1
    else:
        return input * flag_operator(input - 1)

def cheat_operator(input):
    # define map
    # how this map get calculated?
    possibility_map = {
        1: 1,
        2: 2,
        3: 4,
        4: 7,
        5: 13,
        6: 24,
        7: 44,
        8: 81,
        9: 149,

    }
    return possibility_map[input]

print(flag_operator(5))
print(flag_operator(3))

input_list = read_input("./sample.txt")
print(input_list)
# sort input list
input_list.sort()
print(input_list)
diff_list = get_diff_array(input_list)
print(diff_list)
print(one_jolt)
print(two_jolt)
print(three_jolt)

print(one_jolt * three_jolt)

print(find_possible_arrangements(diff_list))

x = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [x for x in x if x > 5]
print(y)
m = [a for a in x for b in y if a == b]
print(m)
n = [a for a in x for a in y]
print(n)

# this is like a fibonacci, but with sum the previous 3 steps (if existing)
with open('./sample2.txt', 'r') as f:
    adapters = list(map(int, f.read().split('\n')))
adapters.sort()
adapters = adapters + [max(adapters) + 3]

print(adapters)
ans = {}
ans[0] = 1
for a in adapters:
    print(a, ans.get(a - 1, 0), ans.get(a - 2, 0), ans.get(a - 3, 0))
    ans[a] = ans.get(a - 1, 0) + ans.get(a - 2, 0) + ans.get(a - 3, 0)

print(f'Answer: {ans[adapters[-1]]}')