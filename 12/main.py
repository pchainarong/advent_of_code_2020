class Instruction:
    def __init__(self, action, value):
        self.action = action
        self.value = value

    def __str__(self):
        return self.action + ":" + str(self.value)


class Waypoint:
    def __init__(self):
        self.north = 1
        self.east = 10
        self.south = 0
        self.west = 0

    def move(self, instruction):
        if instruction.action == "N":
            self.north += instruction.value
        elif instruction.action == "S":
            self.south += instruction.value
        elif instruction.action == "E":
            self.east += instruction.value
        elif instruction.action == "W":
            self.west += instruction.value
        elif instruction.action == "L":
            self.turn_left(instruction.value)
        elif instruction.action == "R":
            self.turn_right(instruction.value)
        else:
            print("do nothing")

    def turn_left(self, value):
        new_direction_turn = (int)(value / 90) % 4
        for i in range(0, new_direction_turn):
            temp = self.north
            self.north = self.east
            self.east = self.south
            self.south = self.west
            self.west = temp

    def turn_right(self, value):
        new_direction_turn = (int)(value / 90) % 4
        for i in range(0, new_direction_turn):
            temp = self.north
            self.north = self.west
            self.west = self.south
            self.south = self.east
            self.east = temp

    def __str__(self):
        return (
            "Waypoint: N:"
            + str(self.north)
            + " E:"
            + str(self.east)
            + " S:"
            + str(self.south)
            + " W:"
            + str(self.west)
        )

class Ferry:
    def __init__(self):
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0
        self.direction = "E"

    def get_manhattan_distance(self):
        return abs(self.north - self.south) + abs(self.east - self.west)

    def move(self, instruction):
        if instruction.action == "N":
            self.north += instruction.value
        elif instruction.action == "S":
            self.south += instruction.value
        elif instruction.action == "E":
            self.east += instruction.value
        elif instruction.action == "W":
            self.west += instruction.value
        elif instruction.action == "L":
            self.turn_left(instruction.value)
        elif instruction.action == "R":
            self.turn_right(instruction.value)
        elif instruction.action == "F":
            self.move_forward(instruction.value)

    def move_to_waypoint(self, waypoint, instruction):
        if instruction.action == "F":
            self.north += waypoint.north * instruction.value
            self.east += waypoint.east * instruction.value
            self.south += waypoint.south * instruction.value
            self.west += waypoint.west * instruction.value
        else:
            print("do nothing")

    def turn_left(self, value):
        new_direction_turn = (value / 90) % 4
        left_turns = ["N", "W", "S", "E"]
        # find index of current direction
        current_direction_index = left_turns.index(self.direction)
        new_direction = left_turns[
            (int)((current_direction_index + new_direction_turn) % 4)
        ]
        self.direction = new_direction

    def turn_right(self, value):
        new_direction_turn = (value / 90) % 4
        right_turns = ["N", "E", "S", "W"]
        # find index of current direction
        current_direction_index = right_turns.index(self.direction)
        new_index = (int)(current_direction_index + new_direction_turn) % 4
        new_direction = right_turns[new_index]
        self.direction = new_direction

    def move_forward(self, value):
        if self.direction == "N":
            self.north += value
        elif self.direction == "S":
            self.south += value
        elif self.direction == "E":
            self.east += value
        elif self.direction == "W":
            self.west += value
        else:
            print("error")

    def __str__(self):
        return (
            "Ferry: Dir:"
            + self.direction
            + " N:"
            + str(self.north)
            + " E:"
            + str(self.east)
            + " S:"
            + str(self.south)
            + " W:"
            + str(self.west)
        )


def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        line = line.strip()
        action = line[0]
        value = int(line[1:])
        instruction = Instruction(action, value)
        array.append(instruction)
    return array


test_instruction = Instruction("F", 10)
print(test_instruction.action, test_instruction.value)

instructions = read_input("input2.txt")

waypoint = Waypoint()
ferry = Ferry()
print(ferry)

# method 1
# for instruction in instructions:
#     print(instruction)
#     ferry.move(instruction)
#     print(ferry)

# method 2
for instruction in instructions:
    print(instruction)
    waypoint.move(instruction)
    print(waypoint)
    ferry.move_to_waypoint(waypoint, instruction)
    print(ferry)

print(ferry.get_manhattan_distance())
