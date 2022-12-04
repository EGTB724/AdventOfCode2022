def main():
    lines = []
    with open('day3.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    sum = 0
    for line in lines:
        c1 = line[0:len(line)//2]
        c2 = line[len(line)//2:]

        # print(line, c1, c2)
        for char1 in c1:
            if char1 in c2:
                c2 = c2.replace(char1, ' ')

                if char1.islower():
                    # print(ord(char1) - 96)
                    sum += (ord(char1) - 96)
                else:
                    # print(ord(char1) - 38)
                    sum += (ord(char1) - 38)

    print("Part 1:", sum)

    sum = 0
    for index in range(0, len(lines), 3):
        str1 = lines[index]
        str2 = lines[index + 1]
        str3 = lines[index + 2]

        for char1 in str1:
            if char1 in str2 and char1 in str3:
                # print(str1, str2, str3, char1)
                str2 = str2.replace(char1, ' ')
                str3 = str3.replace(char1, ' ')

                if char1.islower():
                    # print(ord(char1) - 96)
                    sum += (ord(char1) - 96)
                else:
                    # print(ord(char1) - 38)
                    sum += (ord(char1) - 38)

    print("Part 2:", sum)

if __name__ == "__main__":
    main()
