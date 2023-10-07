class Group:
    def __init__(self):
        self.answers = set(())
        self.count = 0
        self.answers_dict = {}
        self.group_size = 0

    def add_str_answers_part1(self, str):
        #split str into array of chars
        answers_str = str.replace(" ", "")
        array = []
        for i in range(len(answers_str)):
            array.append(answers_str[i])
        #add array to set
        self.answers.update(array)
        self.count = len(self.answers)

    def add_str_answers_part2(self, str):
        #split str into array of chars
        self.group_size += 1
        answers_str = str.replace(" ", "")
        for i in range(len(answers_str)):
            if answers_str[i] in self.answers_dict:
                self.answers_dict[answers_str[i]] += 1
            else:
                self.answers_dict[answers_str[i]] = 1
        #add array to set

    def __str__(self):
        return "Group: " + str(self.answers) + " - Count: " + str(self.count) + " - Dict: " + str(self.answers_dict)


def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    group = Group()
    for line in file:
        if line != "\n":
            #array.append(line.strip())
            group.add_str_answers_part1(line.strip())
            group.add_str_answers_part2(line.strip())
        else:
            array.append(group)
            group = Group()
            continue

    # check if str is not empty at the end of the file
    if group.count != 0:
        array.append(group)

    return array

def part1(array):
    count = 0
    for i in range(len(array)):
        #print(array[i])
        count += array[i].count
    return count

def part2(array):
    count = 0
    for i in range(len(array)):
        #print(array[i].answers_dict)
        for key in array[i].answers_dict:
            if array[i].answers_dict[key] == array[i].group_size:
                count += 1
    return count


g = Group()
g.add_str_answers_part2("a b cd e")
g.add_str_answers_part2("a b c")
print(g)

groups1 = read_input("input1.txt")
print(part1(groups1))

groups2 = read_input("input2.txt")
print(part2(groups2))