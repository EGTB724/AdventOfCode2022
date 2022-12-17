import re
import numpy as np
from tqdm import tqdm
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def main():
    with open('day15.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    sensors = []
    beacons = []
    min_col = max_col = max_row = 0
    for line in lines:
        res = re.split('=|\:|,', line)

        # Indices are backwards again in the input
        sensor_row, sensor_col = int(res[3]), int(res[1])
        beacon_row, beacon_col = int(res[7]), int(res[5])

        sensors.append([sensor_row, sensor_col])
        beacons.append([beacon_row, beacon_col])

        max_col = max(max_col, sensor_col, beacon_col)
        max_row = max(max_row, sensor_row, beacon_row)

        # Apparently the column can be negative which is just super
        min_col = min(min_col, sensor_col, beacon_col)

    min_col = -5000000

    for i in range(len(sensors)):
        sensors[i][1] -= min_col

    for i in range(len(beacons)):
        beacons[i][1] -= min_col

    max_col -= min_col

    NUM_ROWS = max_row + 1
    NUM_COLS = max_col + 10000000
    # grid = np.array([['.' for j in range(NUM_COLS)] for i in range(NUM_ROWS)])


    row_of_interest = 2000000
    available_cols = np.array(['.' for i in range(NUM_COLS)])
    for sensor in sensors:
        if sensor[0] == row_of_interest:
            available_cols[sensor[1]] = "S"

    for beacon in beacons:
        if beacon[0] == row_of_interest:
            available_cols[sensor[1]] = "B"

    # for index, sensor in enumerate(sensors):
    #     expand(grid, sensor[0], sensor[1])


    for i in range(len(sensors)):
        sensor_row, sensor_col = sensors[i][0], sensors[i][1]
        beacon_row, beacon_col = beacons[i][0], beacons[i][1]

        expansion_factor = manhattan_distance(sensor_row, sensor_col, beacon_row, beacon_col)
        vertical_distance = abs(sensor_row - row_of_interest)

        if vertical_distance > expansion_factor:
            continue

        difference = expansion_factor - vertical_distance

        for j in range(sensor_col - difference, sensor_col + difference + 1):
            if available_cols[j] == ".":
                available_cols[j] = "#"

        # print(f"done with {i + 1}")


    sum = 0
    for i in range(NUM_COLS):
        if available_cols[i] == "#":
            sum += 1

    print("Part 1:", sum)

    ##############################################33

    sensors = []
    beacons = []
    # min_col = max_col = max_row = 0
    for line in lines:
        res = re.split('=|\:|,', line)

        # Indices are backwards again in the input
        sensor_row, sensor_col = int(res[3]), int(res[1])
        beacon_row, beacon_col = int(res[7]), int(res[5])

        sensors.append([sensor_row, sensor_col])
        beacons.append([beacon_row, beacon_col])

    NUM_ROWS = 4000000
    NUM_COLS = 4000000
    # grid = np.array([[0 for j in range(NUM_COLS + 1)] for i in range(NUM_ROWS + 1)], dtype=bool)

    polygons = []
    for i in range(len(sensors)):
        sensor_row, sensor_col = sensors[i][0], sensors[i][1]
        beacon_row, beacon_col = beacons[i][0], beacons[i][1]

        expansion_factor = manhattan_distance(sensor_row, sensor_col, beacon_row, beacon_col)

        # Put this into desmos and find the hole by hand... ugh
        print(f"polygon(({sensor_row - expansion_factor},{sensor_col}),({sensor_row},{sensor_col + expansion_factor}),({sensor_row + expansion_factor},{sensor_col}),({sensor_row},{sensor_col - expansion_factor}))")



def manhattan_distance(sensor_row, sensor_col, beacon_row, beacon_col):
    return abs(sensor_row - beacon_row) + abs(sensor_col - beacon_col)

def expand(grid, sensor_row, sensor_col):
    keep_going = True
    explored = [(sensor_row, sensor_col)]
    explore_this_iter = [(sensor_row, sensor_col)]
    explore_next_iter = []

    while keep_going:
        for point in explore_this_iter:
            row, col = point[0], point[1]

            if grid[row, col] == "B":
                keep_going = False
                # continue

            if grid[row, col] == ".":
                grid[row, col] = "#"

            if row != 0 and (row - 1, col) not in explored:
                explored.append((row - 1, col))
                explore_next_iter.append((row - 1, col))

            if col != 0 and (row, col - 1) not in explored:
                explored.append((row, col - 1))
                explore_next_iter.append((row, col - 1))

            if row < len(grid) - 1 and (row + 1, col) not in explored:
                explored.append((row + 1, col))
                explore_next_iter.append((row + 1, col))

            if col < len(grid[0]) - 1 and (row, col + 1) not in explored:
                explored.append((row, col + 1))
                explore_next_iter.append((row, col + 1))


        explore_this_iter = explore_next_iter
        explore_next_iter = []









if __name__ == "__main__":
    main()
