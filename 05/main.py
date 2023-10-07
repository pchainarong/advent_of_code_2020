def read_input(file_name):
    # read file and store in array
    file = open(file_name, "r")
    array = []
    for line in file:
        array.append(line.strip())
    return array

class Seat:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.id = row * 8 + column

    def __str__(self):
        return "row: " + str(self.row) + " column: " + str(self.column) + " id: " + str(self.id)

def convert_seat_str(str):
    # convert str to binary
    row_str = str[0:7]
    column_str = str[7:10]
    row_binary = row_str.replace("F", "0").replace("B", "1")
    column_binary = column_str.replace("L", "0").replace("R", "1")
    print(row_binary, column_binary)
    # convert binary to decimal and convert decimal to row and column
    row = int(row_binary, 2)
    column = int(column_binary, 2)
    # create seat object
    seat = Seat(row, column)
    return seat

def part1(array):
    max_id = 0
    for i in range(len(array)):
        seat = convert_seat_str(array[i])
        if seat.id > max_id:
            max_id = seat.id
    return max_id

def part2(array):
    output_array = []
    for i in range(len(array)):
        seat = convert_seat_str(array[i])
        output_array.append(seat)

    output_array.sort(key=lambda x: x.id)
    for i in range(len(output_array)):
        #71 is the first seat id when we print out the sorted array
        print(i, output_array[i], (i + 71) - output_array[i].id)
        if (i + 71) - output_array[i].id != 0:
            return output_array[i].id - 1


seats = read_input("input2.txt")
print("result :", part2(seats))