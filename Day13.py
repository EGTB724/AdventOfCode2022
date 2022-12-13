import ast

def main():
    with open('day13.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    sum = 0
    for i in range(0, len(lines), 3):
        left = ast.literal_eval(lines[i])
        right = ast.literal_eval(lines[i + 1])

        if compare(left, right) == "Good":
            # print(f"{(i/3) + 1} is good")
            sum += (i/3) + 1

    print(f"Part 1: {int(sum)}")

    ###########################################

    packets = []
    for i in range(0, len(lines), 3):
        packets.append(ast.literal_eval(lines[i]))
        packets.append(ast.literal_eval(lines[i + 1]))

    packets.append(ast.literal_eval("[[2]]"))
    packets.append(ast.literal_eval("[[6]]"))
    for i in range(0, len(packets) - 1):
        for j in reversed(range(i, len(packets) - 1)):
            if compare(packets[j], packets[j + 1]) == "Bad":
                packets[j], packets[j + 1] = packets[j + 1], packets[j]

    index_1 = 0
    index_2 = 0
    for i in range(len(packets)):
        if packets[i] == [[2]]:
            index_1 = i + 1
        elif packets[i] == [[6]]:
            index_2 = i + 1

    print("Part 2:", index_1 * index_2)


def compare(left, right):
    # print(f"Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return "Good"
        elif left > right:
            return "Bad"
        else:
            return "Continue"

    elif isinstance(left, list) and isinstance(right, list):
        length = min(len(left), len(right))
        for i in range(length):
            tmp = compare(left[i], right[i])
            if tmp == "Good":
                # print(f"{left} is smaller than {right}, returning True")
                return "Good"
            elif tmp == "Bad":
                # print(f"{left} is NOT smaller than {right}, returning False")
                return "Bad"

        if len(left) < len(right):
            return "Good"
        elif len(left) > len(right):
            return "Bad"
        else:
            return "Continue"

    else:
        # one list and one integer
        if isinstance(left, int):
            return compare([left], right)
        elif isinstance(right, int):
            return compare(left, [right])
        else:
            print("I should not be here")

if __name__ == "__main__":
    main()
