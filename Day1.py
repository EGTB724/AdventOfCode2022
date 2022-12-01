def main():

    lines = []
    with open('day1.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    elf_sums = []
    sum = 0
    for line in lines:
        if line == '':
            elf_sums.append(sum)
            sum = 0
            continue

        sum += int(line)

    sum = 0
    for i in range(3):
        sum += max(elf_sums)
        elf_sums.pop(elf_sums.index(max(elf_sums)))
    print(sum)


if __name__ == "__main__":
    main()