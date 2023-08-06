"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

answer: 2
"""


# create a class
class Password:
    def __init__(self, min, max, letter, password):
        self.min = min
        self.max = max
        self.letter = letter
        self.test_password = password

    def __str__(self):
        return (
            "min: "
            + str(self.min)
            + " max: "
            + str(self.max)
            + " letter: "
            + self.letter
            + " password: "
            + self.test_password
        )

    def check_password(self):
        # check if password is valid
        # check if letter is in password
        if self.letter in self.test_password:
            # check if letter appears between min and max times
            count = 0
            for i in range(len(self.test_password)):
                if self.test_password[i] == self.letter:
                    count += 1
            if count >= self.min and count <= self.max:
                return True
        return False

    def check_password_position(self):
        # check if password is valid
        # check if letter is in password
        if self.letter in self.test_password:
            # check if letter appears between min and max times
            if (
                self.test_password[self.min - 1] == self.letter
                and self.test_password[self.max - 1] != self.letter
            ):
                return True
            if (
                self.test_password[self.min - 1] != self.letter
                and self.test_password[self.max - 1] == self.letter
            ):
                return True
        return False


def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        # split line into 3 parts
        parts = line.split(" ")
        # split parts[0] into 2 parts
        min_max = parts[0].split("-")
        # create password object
        password = Password(int(min_max[0]), int(min_max[1]), parts[1][0], parts[2])
        # add password object to array
        array.append(password)
    return array


def part1(array):
    count = 0
    for i in range(len(array)):
        print(array[i])

        print(array[i].check_password())
        if array[i].check_password():
            count += 1
    return count


def part2(array):
    count = 0
    for i in range(len(array)):
        print(array[i])
        print(array[i].check_password_position())
        if array[i].check_password_position():
            count += 1
    return count


array = read_input("input2.txt")
count = part2(array)
print(count)
