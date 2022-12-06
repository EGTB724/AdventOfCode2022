def main():
    lines = []
    with open('day6.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    signal = lines[0]
    for i in range(3, len(signal)):
        if not has_repeats(signal[i-3:i+1]):
            print("Part 1:", i + 1)
            break

    for i in range(13, len(signal)):
        if not has_repeats(signal[i-13:i+1]):
            print("Part 2:", i + 1)
            break

def has_repeats(substring):
    return len(set(substring)) != len(substring)

if __name__ == "__main__":
    main()
