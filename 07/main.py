import re


def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(line.strip())
    return array

class Bag:
    def __init__(self, color, size):
        self.color = color
        self.container = []
        self.size = size

    def append(self, bag):
        self.container.append(bag)

    def __str__(self):
        container_str = ""
        for i in range(len(self.container)):
            container_str += str(self.container[i]) + ", "
        if (len(self.container) > 0 ):
            return "Bag: '" + self.color + "' - Size: " + str(self.size) + " - Contains: " + container_str
        else:
            return "Bag: '" + self.color + "' - Size: " + str(self.size)

    def __eq__(self, other):
        return self.color == other.color

    def __hash__(self):
        return hash(self.color)

def init_bag_rules(array):
    rules: set[Bag] = set(())
    for i in range(len(array)):
        rule = array[i]
        print(rule)

        # split rule into 2 parts
        parts = rule.split("contain")
        print(parts)
        # get color
        color = parts[0].replace("bags", "").strip()
        # create bag object
        bag = Bag(color, 1)
        # get contains
        if (parts[1].strip() != "no other bags."):
            contains = parts[1].split(",")
            for j in range(len(contains)):
                # get color
                color = contains[j].replace("bags", "").replace("bag", "").replace(".", "").strip()
                size = int(re.search(r'\d+', color).group())
                # create bag object
                color = color.replace(str(size), "").strip()
                contained_bag = Bag(color, size)
                print(contained_bag)
                bag.append(contained_bag)
            print(bag)
        else:
            contains = []

        print(bag)
        rules.add(bag)
    return rules


def dfs_find_shiny_bag(bag_rules: set[Bag], target_bag: Bag, result_bag: set):
    count = 0
    if target_bag not in bag_rules:
        return count
    else:
        #get object from set
        bag = get_bag(bag_rules, target_bag)
        for sub_bag in bag.container:
            if sub_bag.color == "shiny gold":
                count += 1
                result_bag.add(target_bag)
            count += dfs_find_shiny_bag(bag_rules, sub_bag, result_bag)

    return count

def dfs_count_inside_bags(bag_rules: set[Bag], target_bag: Bag):
    acc = 0
    if target_bag not in bag_rules:
        print("Bag not found")
        return acc
    else:
        bag = get_bag(bag_rules, target_bag)
        if len(bag.container) == 0:
            return 0
        else:
            for sub_bag in bag.container:
                print(f"There are {sub_bag.size} {sub_bag.color} bags in {bag.color} {bag.size}bag")
                acc += sub_bag.size
                bag_inside_count = dfs_count_inside_bags(bag_rules, sub_bag)
                acc += bag_inside_count * sub_bag.size
                print(f"Accumulated {acc} bags")
    return acc

def get_bag(bag_rules: set[Bag], target_bag: Bag):
    if target_bag not in bag_rules:
        return None
    else:
        #get object from set
        for bag in bag_rules:
            if bag.color == target_bag.color:
                return bag
        return None

def part1(bag_rules: set[Bag]):
    print('-------------------')
    result_set = set(())
    count = 0
    for bag in bag_rules:
        if dfs_find_shiny_bag(bag_rules, bag, result_set) > 0:
            count += 1
            print(f"Found {count} bags that can contain shiny gold bags: {result_set}")

    return count

def part2(bag_rules: set[Bag]):
    print('-------------------')
    count = 0
    for bag in bag_rules:
        if bag.color == "shiny gold":
            print("Found shiny gold bag")
            count = dfs_count_inside_bags(bag_rules, bag)
            break

    return count


array = read_input("input1.txt")
bag_rules = init_bag_rules(array)
# print(bag_rules)
print(Bag("shiny gold", 1) in bag_rules)
print(part1(bag_rules))


array = read_input("input2.txt")
bag_rules = init_bag_rules(array)
# print(bag_rules)

# print(Bag("shiny gold", 1) in bag_rules)

print(part2(bag_rules))

#get object from set with provided key or object
# for bag in bag_rules:
#     if bag.color == "shiny gold":
#         print(bag)
#         break