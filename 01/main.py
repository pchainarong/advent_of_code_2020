###
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

# read file and store in array
file = open("input1.txt", "r")
array = []
for line in file:
    array.append(int(line))
# print out array
print(array)
# sort array from smallest to largest
array.sort()
print(array)


def part1(array):
    # loop through array and find two numbers that add up to 2020
    for i in range(len(array)):
        for j in range(len(array)):

            if j > i and array[i] + array[j] == 2020:
                print(array[i], array[j])
                print(array[i] * array[j])
                # exit part1 function
                return


def part2(array):
    # loop through array and find three numbers that add up to 2020
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if k > j > i and array[i] + array[j] + array[k] == 2020:
                    print(array[i], array[j], array[k])
                    print(array[i] * array[j] * array[k])
                    return


part1(array)
part2(array)
