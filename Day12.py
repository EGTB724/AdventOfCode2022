def main():
    with open('day12.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    NUM_ROWS = len(lines)
    NUM_COLS = len(lines[0])
    grid = [['' for j in range(NUM_COLS)] for i in range(NUM_ROWS)]

    start_row = start_col = end_row = end_col = None
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if lines[i][j] == "S":
                start_row, start_col = i, j
                grid[i][j] = "a"
            elif lines[i][j] == "E":
                end_row, end_col = i, j
                grid[i][j] = "z"
            else:
                grid[i][j] = lines[i][j]

    queue = []
    discovered = []

    queue.append((start_row, start_col, 0))
    discovered.append((start_row, start_col))

    while queue:
        # Pop it
        curr_row, curr_col, distance = queue.pop(0)

        # See if we've found a number or not
        if curr_row == end_row and curr_col == end_col:
            print(f"Part 1: {distance}")
            break

        # Explore
        # Check if we can go left
        if curr_col > 0 and valid_move_1(grid[curr_row][curr_col], grid[curr_row][curr_col - 1]) and (curr_row, curr_col - 1) not in discovered:
            queue.append((curr_row, curr_col - 1, distance + 1))
            discovered.append((curr_row, curr_col - 1))

        # Check if we can go up
        if curr_row > 0 and valid_move_1(grid[curr_row][curr_col], grid[curr_row - 1][curr_col]) and (curr_row - 1, curr_col) not in discovered:
            queue.append((curr_row - 1, curr_col, distance + 1))
            discovered.append((curr_row - 1, curr_col))

        # Check if we can go right
        if curr_col < NUM_COLS - 1 and valid_move_1(grid[curr_row][curr_col], grid[curr_row][curr_col + 1]) and (curr_row, curr_col + 1) not in discovered:
            queue.append((curr_row, curr_col + 1, distance + 1))
            discovered.append((curr_row, curr_col + 1))

        # Check if we can go down
        if curr_row < NUM_ROWS - 1 and valid_move_1(grid[curr_row][curr_col], grid[curr_row + 1][curr_col]) and (curr_row + 1, curr_col) not in discovered:
            queue.append((curr_row + 1, curr_col, distance + 1))
            discovered.append((curr_row + 1, curr_col))

    ##################################################

    queue = []
    discovered = []

    # Start at the end, move until we find an 'a'
    start_row, start_col = end_row, end_col

    queue.append((start_row, start_col, 0))
    discovered.append((start_row, start_col))

    while queue:
        # Pop it
        curr_row, curr_col, distance = queue.pop(0)

        # See if we've found a number or not
        if grid[curr_row][curr_col] == "a":
            print(f"Part 2: {distance}")
            break

        # Explore
        # Check if we can go left
        if curr_col > 0 and valid_move_2(grid[curr_row][curr_col], grid[curr_row][curr_col - 1]) and (curr_row, curr_col - 1) not in discovered:
            queue.append((curr_row, curr_col - 1, distance + 1))
            discovered.append((curr_row, curr_col - 1))

        # Check if we can go up
        if curr_row > 0 and valid_move_2(grid[curr_row][curr_col], grid[curr_row - 1][curr_col]) and (curr_row - 1, curr_col) not in discovered:
            queue.append((curr_row - 1, curr_col, distance + 1))
            discovered.append((curr_row - 1, curr_col))

        # Check if we can go right
        if curr_col < NUM_COLS - 1 and valid_move_2(grid[curr_row][curr_col], grid[curr_row][curr_col + 1]) and (curr_row, curr_col + 1) not in discovered:
            queue.append((curr_row, curr_col + 1, distance + 1))
            discovered.append((curr_row, curr_col + 1))

        # Check if we can go down
        if curr_row < NUM_ROWS - 1 and valid_move_2(grid[curr_row][curr_col], grid[curr_row + 1][curr_col]) and (curr_row + 1, curr_col) not in discovered:
            queue.append((curr_row + 1, curr_col, distance + 1))
            discovered.append((curr_row + 1, curr_col))


def valid_move_1(start_val, end_val):
    # end must be no more than one higher than start
    # it can be as much lower, though
    return ord(end_val) - ord(start_val) <= 1


def valid_move_2(start_val, end_val):
    # end must be no more than one higher than start
    # it can be as much lower, though
    return ord(start_val) - ord(end_val) <= 1

if __name__ == "__main__":
    main()
