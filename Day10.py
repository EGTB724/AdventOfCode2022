def main():
    with open('day10.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    num_cycles = 220
    num_instructions = len(lines)
    index = 1
    instruction_queue = []
    reg_x = 1
    special_indices = [20, 60, 100, 140, 180, 220]

    sum = 0
    while index <= num_cycles:
        if index <= num_instructions:
            # There is another instruction to grab
            line_split = lines[index - 1].split()

            if line_split[0] == "addx":
                instruction_queue.append([int(line_split[1]), 1])

            elif line_split[0] == "noop":
                instruction_queue.append([0, 0])

        if index in special_indices:
            # print(f"During Cycle {index}. X: {reg_x}. Strength: {index * reg_x}")
            sum += index * reg_x

        if instruction_queue:
            # There are instructions in the queue waiting to be executed
            if instruction_queue[0][1] == 0:
                reg_x += instruction_queue[0][0]
                instruction_queue.pop(0)

            # Decrement the timers in the queue
            else:
                instruction_queue[0][1] = instruction_queue[0][1] - 1

        # Print the value of the single register
        # print(f"End of cycle {index + 1}, X: {reg_x}")
        index += 1

    print("Part 1:", sum)

    print("Part 2: READ BELOW")

    num_cycles = 240
    num_instructions = len(lines)
    index = 1
    instruction_queue = []
    reg_x = 1
    special_indices = [40, 80, 120, 160, 200, 240]
    # pixel_string = ["." for i in range(220)]
    pixel_string = ""

    while index <= num_cycles:
        if index <= num_instructions:
            # There is another instruction to grab
            line_split = lines[index - 1].split()

            if line_split[0] == "addx":
                instruction_queue.append([int(line_split[1]), 1])

            elif line_split[0] == "noop":
                instruction_queue.append([0, 0])

        if (index - 1) % 40 in [reg_x - 1, reg_x, reg_x + 1]:
            pixel_string += "#"
        else:
            pixel_string += "."

        if index in special_indices:
            # print(''.join(pixel_string[index - 40: index]))
            # pixel_string = ["." for i in range(40)]
            # print(pixel_string)
            for i in range(len(pixel_string)):
                if i % 5 == 0:
                    print('  ', end='')
                if pixel_string[i] == "#":
                    print(pixel_string[i], end='')
                else:
                    print(' ', end='')
            print()
            pixel_string = ""



        if instruction_queue:
            # There are instructions in the queue waiting to be executed
            if instruction_queue[0][1] == 0:
                reg_x += instruction_queue[0][0]
                instruction_queue.pop(0)

            # Decrement the timers in the queue
            else:
                instruction_queue[0][1] = instruction_queue[0][1] - 1

        # Print the value of the single register
        # print(f"End of cycle {index + 1}, X: {reg_x}")
        index += 1


if __name__ == "__main__":
    main()
