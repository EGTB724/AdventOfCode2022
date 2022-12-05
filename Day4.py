def main():
    lines = []
    with open('day4.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    num_complete_overlaps = 0
    num_partial_overlaps = 0
    for line in lines:
        line_split = line.split(',')
        start_1, stop_1 = line_split[0].split('-')
        start_2, stop_2 = line_split[1].split('-')

        if is_complete_overlap((int(start_1), int(stop_1)), (int(start_2), int(stop_2))):
            num_complete_overlaps += 1

        if is_partial_overlap((int(start_1), int(stop_1)), (int(start_2), int(stop_2))):
            num_partial_overlaps += 1

    print("Part 1:", num_complete_overlaps)
    print("Part 2:", num_partial_overlaps)


def is_complete_overlap(range_1, range_2):
    # Check if 1 overlaps 2
    if range_1[0] <= range_2[0] and range_1[1] >= range_2[1]:
        return True

    # Check if 2 overlaps 1
    if range_2[0] <= range_1[0] and range_2[1] >= range_1[1]:
        return True

    # Else, return false
    return False


def is_partial_overlap(range_1, range_2):
    if range_1[0] <= range_2[0] <= range_1[1]:
        return True

    if range_1[0] <= range_2[1] <= range_1[1]:
        return True

    if range_2[0] <= range_1[0] <= range_2[1]:
        return True

    if range_2[0] <= range_1[1] <= range_2[1]:
        return True

    # Else, return false
    return False


if __name__ == "__main__":
    main()
