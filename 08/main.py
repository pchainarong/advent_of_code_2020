import re


def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(line.strip())
    return array


def part1(commands: list[str]):
    acc = 0
    index = 0
    visited = set(())
    while index not in visited:
        visited.add(index)
        command = commands[index].split(" ")
        operation = command[0]
        argument = int(command[1])
        if operation == "acc":
            acc += argument
            index += 1
        elif operation == "jmp":
            index += argument
        elif operation == "nop":
            index += 1
    return acc

def part2(commands: list[str]):
    print(f"original commands: {commands}")
    #copy commands

    for i in range(len(commands)):
        command = commands[i].split(" ")
        operation = command[0]
        new_commands = commands.copy()

        if operation == "jmp":
            new_commands[i] = "nop " + command[1]
        elif operation == "nop":
            new_commands[i] = "jmp " + command[1]
        print (new_commands)

        acc = 0
        index = 0
        visited = set(())
        while index not in visited and index < len(new_commands):
            visited.add(index)
            command = new_commands[index].split(" ")
            operation = command[0]
            argument = int(command[1])
            if operation == "acc":
                acc += argument
                index += 1
            elif operation == "jmp":
                index += argument
            elif operation == "nop":
                index += 1
        #check if operations completed normally
        if index == len(new_commands):
            return acc

        print(f"i: {i}: index: {index} - len(commands): {len(new_commands)}")

def main():
    commands = read_input("input2.txt")
    #print(part1(commands))
    print(part2(commands))


if __name__ == "__main__":
    main()