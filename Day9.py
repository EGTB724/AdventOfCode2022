import math

def main():
    with open('day9.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    # Determine how big the grid needs to be
    max_left, max_up, max_right, max_down = 0, 0, 0, 0
    curr_row, curr_col = 0, 0

    for line in lines:
        line_split = line.split()

        if line_split[0] == "L":
            curr_col -= int(line_split[1])
            if curr_col < max_left:
                max_left = curr_col
        elif line_split[0] == "U":
            curr_row += int(line_split[1])
            if curr_row > max_up:
                max_up = curr_row
        elif line_split[0] == "R":
            curr_col += int(line_split[1])
            if curr_col > max_right:
                max_right = curr_col
        elif line_split[0] == "D":
            curr_row -= int(line_split[1])
            if curr_row < max_down:
                max_down = curr_row

    # print(f"L: {max_left} R: {max_right} U: {max_up} D: {max_down}")

    num_rows = max_up - max_down + 5
    num_cols = max_right - max_left + 5

    grid = [["." for j in range(num_cols)] for i in range(num_rows)]
    head_row, head_col = num_rows - abs(max_down) - 1, abs(max_left)
    tail_row, tail_col = num_rows - abs(max_down) - 1, abs(max_left)

    for line in lines:
        # Process direction for head, move it
        line_split = line.split()

        for i in range(int(line_split[1])):
            # Mark the location of the tail
            grid[tail_row][tail_col] = "#"
            # print_grid(grid, head_row, head_col, tail_row, tail_col)

            if line_split[0] == "L":
                head_col -= 1
            elif line_split[0] == "U":
                head_row -= 1
            elif line_split[0] == "R":
                head_col += 1
            elif line_split[0] == "D":
                head_row += 1

            # Make tail move towards head (if need be)
            if not is_touching(head_row, head_col, tail_row, tail_col):
                if not in_same_row_or_column(head_row, head_col, tail_row, tail_col):
                    # Try diagonals second
                    if is_touching(head_row, head_col, tail_row - 1, tail_col - 1):
                        tail_row, tail_col = tail_row - 1, tail_col - 1

                    elif is_touching(head_row, head_col, tail_row - 1, tail_col + 1):
                        tail_row, tail_col = tail_row - 1, tail_col + 1

                    elif is_touching(head_row, head_col, tail_row + 1, tail_col - 1):
                        tail_row, tail_col = tail_row + 1, tail_col - 1

                    elif is_touching(head_row, head_col, tail_row + 1, tail_col + 1):
                        tail_row, tail_col = tail_row + 1, tail_col + 1

                else:
                    # Try adjacent first, if works, good
                    if is_touching(head_row, head_col, tail_row, tail_col - 1):
                        tail_col = tail_col - 1

                    elif is_touching(head_row, head_col, tail_row - 1, tail_col):
                        tail_row = tail_row - 1

                    elif is_touching(head_row, head_col, tail_row, tail_col + 1):
                        tail_col = tail_col + 1

                    elif is_touching(head_row, head_col, tail_row + 1, tail_col):
                        tail_row = tail_row + 1

    # Mark the location of the tail
    grid[tail_row][tail_col] = "#"
    # print_grid(grid, head_row, head_col, tail_row, tail_col)

    # Get sum of all #'s
    sum = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "#":
                sum += 1

    print("Part 1:", sum)
    ################################################################

    num_rows = 1000
    num_cols = 1000
    grid = [["." for j in range(num_cols)] for i in range(num_rows)]
    rope = [[0 for j in range(10)] for i in range(2)]

    for i in range(2):
        for j in range(10):
            if i == 0:
                rope[i][j] = 500
            if i == 1:
                rope[i][j] = 500

    for line in lines:
        # Process direction for head, move it
        line_split = line.split()

        for i in range(int(line_split[1])):
            # Mark the location of the tail
            grid[rope[0][-1]][rope[1][-1]] = "#"
            # print_grid(grid, head_row, head_col, tail_row, tail_col)

            if line_split[0] == "L":
                rope[0][0] -= 1
            elif line_split[0] == "U":
                rope[1][0] -= 1
            elif line_split[0] == "R":
                rope[0][0] += 1
            elif line_split[0] == "D":
                rope[1][0] += 1

            # Make tail move towards head (if need be)
            for j in range(1, 10):
                if not is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j], rope[1][j]):
                    if not in_same_row_or_column(rope[0][j - 1], rope[1][j - 1], rope[0][j], rope[1][j]):
                        # Try diagonals second
                        if is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j] - 1, rope[1][j] - 1):
                            rope[0][j], rope[1][j] = rope[0][j] - 1, rope[1][j] - 1

                        elif is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j] - 1, rope[1][j] + 1):
                            rope[0][j], rope[1][j] = rope[0][j] - 1, rope[1][j] + 1

                        elif is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j] + 1, rope[1][j] - 1):
                            rope[0][j], rope[1][j] = rope[0][j] + 1, rope[1][j] - 1

                        elif is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j] + 1, rope[1][j] + 1):
                            rope[0][j], rope[1][j] = rope[0][j] + 1, rope[1][j] + 1

                    else:
                        # Try adjacent first, if works, good
                        if is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j], rope[1][j] - 1):
                            rope[1][j] = rope[1][j] - 1

                        elif is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j] - 1, rope[1][j]):
                            rope[0][j] = rope[0][j] - 1

                        elif is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j], rope[1][j] + 1):
                            rope[1][j] = rope[1][j] + 1

                        elif is_touching(rope[0][j - 1], rope[1][j - 1], rope[0][j] + 1, rope[1][j]):
                            rope[0][j] = rope[0][j] + 1

    # Mark the location of the tail
    grid[rope[0][-1]][rope[1][-1]] = "#"
    # print_big_grid(grid, rope)

    # Get sum of all #'s
    sum = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == "#":
                sum += 1

    print("Part 1:", sum)


def is_touching(head_row, head_col, tail_row, tail_col):
    return max(abs(head_row - tail_row), abs(head_col - tail_col)) <= 1

def in_same_row_or_column(head_row, head_col, tail_row, tail_col):
    return head_row == tail_row or head_col == tail_col


def print_grid(grid, head_row, head_col, tail_row, tail_col):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if i == head_row and j == head_col:
                print('H', end=' ')
            elif i == tail_row and j == tail_col:
                print('T', end=' ')
            else:
                print(grid[i][j], end=' ')
        print()
    print()

def print_big_grid(grid, rope):
    num_rows = len(grid)
    num_cols = len(grid[0])

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(1, 10):
                if i == rope[0][0] and j == rope[1][0]:
                    print('H', end=' ')
                elif i == rope[0][k] and j == rope[1][k]:
                    print(k - 1, end=' ')
                else:
                    print(grid[i][j], end=' ')
        print()
    print()


if __name__ == "__main__":
    main()
