import numpy as np

def main():
    with open('day14.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    max_height = 0
    max_width = 0
    paths = []
    for line in lines:
        path = []

        line_split = line.split()
        for i in range(0, len(line_split), 2):
            tmp = line_split[i].split(",")
            path.append((int(tmp[0]), int(tmp[1])))
            max_width = max(int(tmp[0]), max_width)
            max_height = max(int(tmp[1]), max_height)

        paths.append(path)

    # Extend height by two so we know when sand has fallen in the "abyss"
    grid = np.array([['.' for j in range(max_width + 1)]for i in range(max_height + 2)])

    for path in paths:
        for i in range(1, len(path)):
            # Order is reversed in input... annoying
            start_col, start_row = path[i - 1][0], path[i - 1][1]
            end_col, end_row = path[i][0], path[i][1]

            grid[min(start_row, end_row): max(start_row, end_row) + 1, min(start_col, end_col):max(start_col, end_col) + 1] = "#"

    sand_col, sand_row = 500, 0

    sum = 0
    while True:
        drop_sand(grid, sand_row, sand_col)
        if "o" in grid[-1]:
            break
        sum += 1

    print("Part 1:", sum)

################################

    # Extend height by two so we know when sand has fallen in the "abyss"
    grid = np.array([['.' for j in range(max_width + 1000)]for i in range(max_height + 3)])

    for path in paths:
        for i in range(1, len(path)):
            # Order is reversed in input... annoying
            start_col, start_row = path[i - 1][0], path[i - 1][1]
            end_col, end_row = path[i][0], path[i][1]

            grid[min(start_row, end_row): max(start_row, end_row) + 1, min(start_col, end_col):max(start_col, end_col) + 1] = "#"

    grid[-1] = "#"

    sand_col, sand_row = 500, 0

    sum = 0
    while True:
        drop_sand(grid, sand_row, sand_col)
        sum += 1
        if grid[sand_row, sand_col] == "o":
            break

    print("Part 2:", sum)


def drop_sand(grid, sand_row, sand_col):
    curr_row = sand_row
    curr_col = sand_col

    while True:
        if can_go_down(grid, curr_row, curr_col):
            curr_row += 1
        elif can_go_down_left(grid, curr_row, curr_col):
            curr_row += 1
            curr_col -= 1
        elif can_go_down_right(grid, curr_row, curr_col):
            curr_row += 1
            curr_col += 1
        else:
            break

    grid[curr_row, curr_col] = "o"


def can_go_down(grid, curr_row, curr_col):
    return curr_row < grid.shape[0] - 1 and grid[curr_row + 1, curr_col] not in ["#", "o"]


def can_go_down_left(grid, curr_row, curr_col):
    return curr_row < grid.shape[0] - 1 and grid[curr_row + 1, curr_col - 1] not in ["#", "o"]


def can_go_down_right(grid, curr_row, curr_col):
    return curr_row < grid.shape[0] - 1 and grid[curr_row + 1, curr_col + 1] not in ["#", "o"]


if __name__ == "__main__":
    main()
