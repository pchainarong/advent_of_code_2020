import re


class Passport:
    # define public members
    byr = None  # Birth Year
    iyr = None  # Issue Year
    eyr = None  # Expiration Year
    hgt = None  # Height
    hcl = None  # Hair Color
    ecl = None  # Eye Color
    pid = None  # Passport ID
    cid = None  # Country ID

    @staticmethod
    def is_range_valid(value, min, max):
        if int(value) < min or int(value) > max:
            return False
        return True

    def is_byr_valid(self):
        if len(self.byr) != 4:
            return False
        return Passport.is_range_valid(self.byr, 1920, 2002)

    def is_iyr_valid(self):
        if len(self.iyr) != 4:
            return False
        return Passport.is_range_valid(self.iyr, 2010, 2020)

    def is_eyr_valid(self):
        if len(self.eyr) != 4:
            return False
        return Passport.is_range_valid(self.eyr, 2020, 2030)

    def is_hgt_valid(self):
        if self.hgt[-2:] == "cm":
            return Passport.is_range_valid(self.hgt[:-2], 150, 193)
        elif self.hgt[-2:] == "in":
            return Passport.is_range_valid(self.hgt[:-2], 59, 76)
        return False

    def is_hcl_valid(self):
        match = re.search("^#[0-9a-f]{6}$", self.hcl)
        if match:
            return True
        return False

    def is_ecl_valid(self):
        try:
            if ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].index(self.ecl) >= 0:
                return True
        except ValueError:
            return False
        return False

    def is_pid_valid(self):
        match = re.search("^[0-9]{9}$", self.pid)
        if match:
            return True
        return False

    def is_valid(self):
        if (
            self.byr == None
            or self.iyr == None
            or self.eyr == None
            or self.hgt == None
            or self.hcl == None
            or self.ecl == None
            or self.pid == None
        ):
            return False
        return True

    def is_valid_and_present(self):
        if (
            self.byr == None
            or self.iyr == None
            or self.eyr == None
            or self.hgt == None
            or self.hcl == None
            or self.ecl == None
            or self.pid == None
        ):
            print("missing field")
            return False
        if not self.is_byr_valid():
            print("byr invalid")
            return False
        if not self.is_iyr_valid():
            print("iyr invalid")
            return False
        if not self.is_eyr_valid():
            print("eyr invalid")
            return False
        if not self.is_hgt_valid():
            print("hgt invalid")
            return False
        if not self.is_hcl_valid():
            print("hcl invalid")
            return False
        if not self.is_ecl_valid():
            print("ecl invalid")
            return False
        if not self.is_pid_valid():
            print("pid invalid")
            return False
        print("valid")
        return True

    def __str__(self):
        return (
            "byr: "
            + str(self.byr)
            + " iyr: "
            + str(self.iyr)
            + " eyr: "
            + str(self.eyr)
            + " hgt: "
            + str(self.hgt)
            + " hcl: "
            + str(self.hcl)
            + " ecl: "
            + str(self.ecl)
            + " pid: "
            + str(self.pid)
            + " cid: "
            + str(self.cid)
        )


def string_to_passport(str):
    # split string into array
    array = str.split(" ")
    # create passport object
    passport = Passport()
    # loop through array
    for i in range(len(array)):
        # split array[i] into 2 parts
        parts = array[i].split(":")
        # check if parts[0] is a valid member of passport
        if hasattr(passport, parts[0]):
            # set passport member to parts[1]
            setattr(passport, parts[0], parts[1])
    return passport


def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    str = ""
    for line in file:
        if line != "\n" and line != "\r\n":
            # remove newline character
            line = line.replace("\r\n", "")
            line = line.replace("\n", "")
            # add line to str
            str += " " + line
        else:
            # create passport object
            passport = string_to_passport(str)
            # add passport object to array
            array.append(passport)
            print(passport)
            str = ""
            continue

    # check if str is not empty at the end of the file
    if str != "":
        # create passport object
        passport = string_to_passport(str)
        # add passport object to array
        array.append(passport)
        print(passport)
        str = ""

    return array


def part1(passports):
    count = 0
    for i in range(len(passports)):
        if passports[i].is_valid():
            count += 1
    return count


def part2(passports):
    count = 0
    for i in range(len(passports)):
        if passports[i].is_valid_and_present():
            count += 1
    return count


passports = read_input("input2.txt")
print(part2(passports))
