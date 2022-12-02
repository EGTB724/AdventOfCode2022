game_outcomes = {
    "A":{
        "X": 3 + 0,
        "Y": 1 + 3,
        "Z": 2 + 6,
    },
    "B": {
        "X": 1 + 0,
        "Y": 2 + 3,
        "Z": 3 + 6,
    },
    "C": {
        "X": 2 + 0,
        "Y": 3 + 3,
        "Z": 1 + 6,
    }
}

def main():
    lines = []
    with open('day2.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    sum = 0
    for line in lines:
        chars = line.split()
        char1, char2 = chars[0], chars[1]

        global game_outcomes
        sum += game_outcomes[char1][char2]

    print(sum)


if __name__ == "__main__":
    main()
