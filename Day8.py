def main():
    with open('day8.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    NUM_ROWS = len(lines)
    NUM_COLS = len(lines[0])

    grid = [[0 for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            grid[i][j] = int(lines[i][j])

    sum = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if isVisible(grid, i, j, NUM_ROWS, NUM_COLS):
                sum += 1

    print("Part 1:", sum)

    best_score = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            score = scenic_score(grid, i, j, NUM_ROWS, NUM_COLS)
            best_score = max(score, best_score)

    print("Part 2:", best_score)


def isVisible(grid, row, col, num_rows, num_cols):
    # Check if we're on an edge
    if row == 0 or row == num_rows - 1:
        return True

    if col == 0 or col == num_cols - 1:
        return True

    # If not on edge, go out in all four directions
    val = grid[row][col]

    # Go up
    iter_visible = True
    curr_row = row - 1
    while curr_row >= 0:
        if not grid[curr_row][col] < val:
            iter_visible = False
            break
        curr_row -= 1

    if iter_visible:
        return True

    # Go down
    iter_visible = True
    curr_row = row + 1
    while curr_row <= num_rows - 1:
        if not grid[curr_row][col] < val:
            iter_visible = False
            break
        curr_row += 1

    if iter_visible:
        return True

    # Go left
    iter_visible = True
    curr_col = col - 1
    while curr_col >= 0:
        if not grid[row][curr_col] < val:
            iter_visible = False
            break
        curr_col -= 1

    if iter_visible:
        return True

    # Go right
    iter_visible = True
    curr_col = col + 1
    while curr_col <= num_cols - 1:
        if not grid[row][curr_col] < val:
            iter_visible = False
            break
        curr_col += 1

    if iter_visible:
        return True

    return False


def scenic_score(grid, row, col, num_rows, num_cols):
    # Check if we're on an edge
    if row == 0 or row == num_rows - 1:
        return 0

    if col == 0 or col == num_cols - 1:
        return True

    # If not on edge, go out in all four directions
    val = grid[row][col]

    # Go up
    num_up = 0
    curr_row = row - 1
    while curr_row >= 0:
        if not grid[curr_row][col] < val:
            num_up += 1
            break
        num_up += 1
        curr_row -= 1

    # Go down
    num_down = 0
    curr_row = row + 1
    while curr_row <= num_rows - 1:
        if not grid[curr_row][col] < val:
            num_down += 1
            break
        num_down += 1
        curr_row += 1

    # Go left
    num_left = 0
    curr_col = col - 1
    while curr_col >= 0:
        if not grid[row][curr_col] < val:
            num_left += 1
            break
        num_left += 1
        curr_col -= 1

    # Go right
    num_right = 0
    curr_col = col + 1
    while curr_col <= num_cols - 1:
        if not grid[row][curr_col] < val:
            num_right += 1
            break
        num_right += 1
        curr_col += 1

    return num_up * num_down * num_left * num_right


if __name__ == "__main__":
    main()
