import math

def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(line.strip())
    return array

# Part 1
def part1():
    lines = read_input("input1.txt")
    start_time = (int)(lines[0])
    bus_ids = [(int)(x) for x in lines[1].split(",") if x != "x"]
    print(start_time, bus_ids)

    target_bus = 0
    target_time = 0
    for bus_id in bus_ids:
        next_bus_after_time = (int)((start_time // bus_id) * bus_id) + bus_id
        if (next_bus_after_time < target_time or target_time == 0):
            target_time = next_bus_after_time
            target_bus = bus_id
        print(bus_id, next_bus_after_time, target_time, target_bus)

    print(target_bus, target_time, target_bus * (target_time - start_time))

# part1()

# Part 2
class Bus:
    def __init__(self, id, offset):
        self.id = id
        self.offset = offset

    def is_prime(self):
        for i in range(2, int(math.sqrt(self.id)) + 1):
            if self.id % i == 0:
                return False
        return True

    def __str__(self):
        return "Bus: " + str(self.id) + " Offset: " + str(self.offset)

lines = read_input("input2.txt")
bus_inputs = [x for x in lines[1].split(",")]

# bus_inputs = [x for x in '17,x,13,19'.split(",")] # 3417
# bus_inputs = [x for x in '67,7,59,61'.split(",")] # 754018
# bus_inputs = [x for x in '67,x,7,59,61'.split(",")] # 779210
# bus_inputs = [x for x in '67,7,x,59,61'.split(",")] # 1261476
# bus_inputs = [x for x in '1789,37,47,1889'.split(",")] # 1202161486

buses = []
for i in range(len(bus_inputs)):
    if bus_inputs[i] != "x":
        buses.append(Bus((int)(bus_inputs[i]), i))


step = 1
for bus in buses:
    print(bus)
    print(bus.is_prime())


bus_no_offset = buses[0]
start_time = 0
step = bus_no_offset.id
# start from the second bus and this consider all bus_ids are prime number
for i in range(1, len(buses)):
    bus = buses[i]
    while (start_time + bus.offset) % bus.id != 0:
        start_time += step
    step *= bus.id
    print(bus, start_time)

print(start_time)

def solve_2(data):
    data = [(i, int(bus_id)) for i, bus_id in enumerate(data[1].split(',')) if bus_id != 'x']
    print(data)
    jump = data[0][1]
    time_stamp = 0
    # we can do this because all numbers are prime
    for delta, bus_id in data[1:]:
        print(delta, bus_id, jump, time_stamp)
        while (time_stamp + delta) % bus_id != 0:
            time_stamp += jump
        jump *= bus_id
    return time_stamp

#print(lines)
#print(solve_2(lines))