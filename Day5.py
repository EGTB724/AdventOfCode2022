def main():
    lines = []
    with open('day5.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    # I'm just gonna build the initial state by hand as opposed to trying to dynamically read it from the file
    # Think of it as an array of stacks
    NUM_COLS = 9
    grid = [[] for i in range(NUM_COLS)]

    grid[0] = list("WDGBHRV")
    grid[1] = list("JNGCRF")
    grid[2] = list("LSFHDNJ")
    grid[3] = list("JDSV")
    grid[4] = list("SHDRQWNV")
    grid[5] = list("PGHCM")
    grid[6] = list("FJBGLZHC")
    grid[7] = list("SJR")
    grid[8] = list("LGSRBNVM")

    for line in lines:
        line_split = line.split()
        amt = int(line_split[1])
        start = int(line_split[3])
        stop = int(line_split[5])

        start_index, stop_index = start - 1, stop - 1

        tmp = grid[start_index][-amt:]
        del grid[start_index][-amt:]
        grid[stop_index] += reversed(tmp)

    part_1 = ""
    for i in range(NUM_COLS):
        part_1 += grid[i][-1]

    print("Part 1:", part_1)

    grid[0] = list("WDGBHRV")
    grid[1] = list("JNGCRF")
    grid[2] = list("LSFHDNJ")
    grid[3] = list("JDSV")
    grid[4] = list("SHDRQWNV")
    grid[5] = list("PGHCM")
    grid[6] = list("FJBGLZHC")
    grid[7] = list("SJR")
    grid[8] = list("LGSRBNVM")

    for line in lines:
        line_split = line.split()
        amt = int(line_split[1])
        start = int(line_split[3])
        stop = int(line_split[5])

        start_index, stop_index = start - 1, stop - 1

        tmp = grid[start_index][-amt:]
        del grid[start_index][-amt:]
        grid[stop_index] += tmp

    part_2 = ""
    for i in range(NUM_COLS):
        part_2 += grid[i][-1]

    print("Part 2:", part_2)

if __name__ == "__main__":
    main()
