import math
def main():
    with open('day11.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    monkeys = []
    for i in range(0, len(lines), 7):
        id = int(lines[i].split()[1].replace(":",""))
        items = [int(item.replace(",","")) for item in lines[i + 1].split(":")[1].split()]
        operation = lines[i + 2].split()[4]

        if lines[i + 2].split()[5] == "old":
            amount = "old"
        else:
            amount = int(lines[i + 2].split()[5])

        divisibility_test = int(lines[i + 3].split()[3])
        true_monkey = int(lines[i + 4].split()[5])
        false_monkey = int(lines[i + 5].split()[5])

        monkeys.append(Monkey(id, items, operation, amount, divisibility_test, true_monkey, false_monkey))

    # print(f"Before start:")
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.id}: {monkey.items}")

    round_number = 1
    while round_number <= 20:
        for monkey in monkeys:
            for index, item in enumerate(monkey.items):
                monkey.inspect_item(index)
                monkey.bored_of_item(index)
                if monkey.items[index] % monkey.divisibility_test == 0:
                    monkeys[monkey.true_monkey].items.append(monkey.items[index])
                else:
                    monkeys[monkey.false_monkey].items.append(monkey.items[index])
            monkey.items = []


        # print(f"After round {round_number}")
        # for monkey in monkeys:
        #     print(f"Monkey {monkey.id}: {monkey.items}")
        round_number += 1


    # print("ITERATIONS OVER")
    inspection_array = []
    for monkey in monkeys:
        inspection_array.append(monkey.items_inspected)
        # print(f"Monkey {monkey.id}: {monkey.items_inspected}")

    monkey_business = 1
    for _ in range(2):
        monkey_business *= max(inspection_array)
        inspection_array.remove(max(inspection_array))

    print("Part 1:", monkey_business)

    ########################################################

    monkeys = []
    lcm = 1
    for i in range(0, len(lines), 7):
        id = int(lines[i].split()[1].replace(":",""))
        items = [int(item.replace(",","")) for item in lines[i + 1].split(":")[1].split()]
        operation = lines[i + 2].split()[4]

        if lines[i + 2].split()[5] == "old":
            amount = "old"
        else:
            amount = int(lines[i + 2].split()[5])

        divisibility_test = int(lines[i + 3].split()[3])
        true_monkey = int(lines[i + 4].split()[5])
        false_monkey = int(lines[i + 5].split()[5])

        monkeys.append(Monkey(id, items, operation, amount, divisibility_test, true_monkey, false_monkey))
        lcm *= divisibility_test

    # print(f"Before start:")
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.id}: {monkey.items}")

    round_number = 1
    while round_number <= 10000:
        for monkey in monkeys:
            for index, item in enumerate(monkey.items):
                monkey.special_inspect_item(index, lcm)
                if monkey.items[index] % monkey.divisibility_test == 0:
                    monkeys[monkey.true_monkey].items.append(monkey.items[index])
                else:
                    monkeys[monkey.false_monkey].items.append(monkey.items[index])
            monkey.items = []


        # print(f"After round {round_number}")
        # for monkey in monkeys:
        #     print(f"Monkey {monkey.id}: {monkey.items}")
        round_number += 1


    # print("ITERATIONS OVER")
    inspection_array = []
    for monkey in monkeys:
        inspection_array.append(monkey.items_inspected)
        # print(f"Monkey {monkey.id}: {monkey.items_inspected}")

    monkey_business = 1
    for _ in range(2):
        monkey_business *= max(inspection_array)
        inspection_array.remove(max(inspection_array))

    print("Part 2:", monkey_business)

class Monkey:
    def __init__(self, id, items, operation, amount, divisibility_test, true_monkey, false_monkey):
        self.id = id
        self.items = items
        self.items_inspected = 0
        self.operation = operation
        self.amount = amount
        self.divisibility_test = divisibility_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def inspect_item(self, index):
        self.items_inspected += 1
        if self.amount == "old":
            if self.operation == "+":
                self.items[index] += self.items[index]
            elif self.operation == "-":
                self.items[index] -= self.items[index]
            elif self.operation == "*":
                self.items[index] *= self.items[index]
            elif self.operation == "/":
                self.items[index] /= self.items[index]
        else:
            if self.operation == "+":
                self.items[index] += self.amount
            elif self.operation == "-":
                self.items[index] -= self.amount
            elif self.operation == "*":
                self.items[index] *= self.amount
            elif self.operation == "/":
                self.items[index] /= self.amount

    def special_inspect_item(self, index, lcm):
        self.items_inspected += 1
        if self.amount == "old":
            if self.operation == "+":
                self.items[index] += self.items[index]
            elif self.operation == "-":
                self.items[index] -= self.items[index]
            elif self.operation == "*":
                self.items[index] *= self.items[index]
            elif self.operation == "/":
                self.items[index] /= self.items[index]
        else:
            if self.operation == "+":
                self.items[index] += self.amount
            elif self.operation == "-":
                self.items[index] -= self.amount
            elif self.operation == "*":
                self.items[index] *= self.amount
            elif self.operation == "/":
                self.items[index] /= self.amount
        self.items[index] = self.items[index] % lcm

    def bored_of_item(self, index):
        self.items[index] = self.items[index] // 3

if __name__ == "__main__":
    main()
