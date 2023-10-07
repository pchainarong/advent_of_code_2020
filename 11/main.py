
def read_input_to_seat_array(file_name):
    """
    Reads a file containing seat information and returns a 2D array of seats.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A 2D array of seats, where each seat is represented by a character.
    """
    # read file and store in array
    file = open(file_name, "r")
    seat_array = []
    for line in file:
        seat_array.append(list(line.strip()))
    return seat_array


def print_seat_array(seat_array):
    for row in seat_array:
        print("".join(row))

def count_adjacent_occupied(seat_array, row, column):
    """
    Counts the number of adjacent seats that are occupied.

    Args:
        seat_array (list): A 2D list representing the seating arrangement.
        row (int): The row index of the seat to check.
        column (int): The column index of the seat to check.

    Returns:
        int: The number of adjacent seats that are occupied.
    """
    occupied = 0
    rows = len(seat_array)
    columns = len(seat_array[0])

    # Check all adjacent seats
    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, column-1), min(columns, column+2)):
            if i == row and j == column:
                continue
            if seat_array[i][j] == "#":
                occupied += 1

    return occupied

def count_visible_occupied(seat_array, row, column):
    occupied = 0
    rows = len(seat_array)
    columns = len(seat_array[0])

    # Check all visible seats
    dimensions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
    for dimension in dimensions:
        i = row
        j = column
        while True:
            i += dimension[0]
            j += dimension[1]
            if i < 0 or i >= rows or j < 0 or j >= columns:
                # if out of bounds, stop
                break
            if seat_array[i][j] == "#":
                # if occupied, add to count and stop
                occupied += 1
                break
            elif seat_array[i][j] == "L":
                # if first empty, stop
                break

    return occupied


def check_if_in_diagonal(seat_row, seat_column, row, column):
    if seat_row == row or seat_column == column:
        return True
    elif abs(seat_row - row) == abs(seat_column - column):
        return True
    else:
        return False

def count_occupied(seat_array):
    occupied = 0
    rows = len(seat_array)
    columns = len(seat_array[0])

    for row in range(rows):
        for column in range(columns):
            if seat_array[row][column] == "#":
                occupied += 1

    return occupied

#define main method
def main():
    # read input
    seat_array = read_input_to_seat_array("input2.txt")
    print_seat_array(seat_array)

    # get number of rows and columns
    rows = len(seat_array)
    columns = len(seat_array[0])
    print(rows, columns)
    print(count_adjacent_occupied(seat_array, 3, 3))
    print(check_if_in_diagonal(0, 0, 3, 3))
    print(check_if_in_diagonal(0, 1, 3, 3))

    test_array = ['#.##.##.##', '#######.##', '#.#.#..#..']
    print(count_visible_occupied(test_array, 0, 2))
    print(count_visible_occupied(test_array, 0, 9))

    changed = True
    while changed:
        changed = False
        new_seat_array = []
        for row in range(rows):
            new_seat_array.append([])
            for column in range(columns):
                if seat_array[row][column] == ".":
                    new_seat_array[row].append(".")
                else:
                    # method 1
                    # occupied = count_adjacent_occupied(seat_array, row, column)
                    # method 2
                    occupied = count_visible_occupied(seat_array, row, column)
                    if seat_array[row][column] == "L" and occupied == 0:
                        new_seat_array[row].append("#")
                        changed = True
                    elif seat_array[row][column] == "#" and occupied >= 5:
                        new_seat_array[row].append("L")
                        changed = True
                    else:
                        new_seat_array[row].append(seat_array[row][column])

        seat_array = new_seat_array
        # print_seat_array(seat_array)
        # print('')

    print(count_occupied(seat_array))


main()