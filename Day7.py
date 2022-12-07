dir_dict = {}

def main():
    lines = []
    with open('day7.txt') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    root = Node("/", False)
    curr_node = root

    num_lines = len(lines)
    curr_line = 0

    while curr_line < num_lines:
        line_split = lines[curr_line].split()

        if line_split[0] == "$":
            if line_split[1] == "cd":
                if line_split[2] == "/":
                    curr_node = root
                if line_split[2] == "..":
                    curr_node = curr_node.parent
                else:
                    desired_directory = line_split[2]
                    for child in curr_node.children:
                        if child.name == desired_directory:
                            curr_node = child

            elif line_split[1] == "ls":
                curr_line += 1
                while curr_line < num_lines and lines[curr_line].split()[0] != "$":
                    new_entry = lines[curr_line].split()
                    if new_entry[0] == "dir":
                        name = new_entry[1]
                        tmp = Node(name, False)
                        tmp.parent = curr_node
                        curr_node.children.append(tmp)
                    else:
                        size = int(new_entry[0])
                        name = new_entry[1]
                        tmp = Node(name, True, size)
                        tmp.parent = curr_node
                        curr_node.children.append(tmp)
                    curr_line += 1
                curr_line -=1
        curr_line += 1

    # print_file_system(root, 0)

    get_directory_sizes(root)
    global dir_dict
    # print(dir_dict)

    sum = 0
    for key in dir_dict:
        if dir_dict[key] <= 100000:
            sum += dir_dict[key]

    print("Part 1:", sum)

    total_space = 70000000
    update_size = 30000000
    unused_space = total_space - dir_dict["/"]
    space_needed = update_size - unused_space

    dir_dict_sorted = sorted(dir_dict.items(), key=lambda x: x[1])
    for entry in dir_dict_sorted:
        if entry[1] > space_needed:
            print("Part 2:", entry[1])
            break





def print_file_system(root, depth):
    for i in range(depth):
        print("  ", end='')

    if root.isFile:
        print(f" - {root.name} (file, {root.size})")
    else:
        print(f" - {root.name} (dir)")

    for child in root.children:
        print_file_system(child, depth + 1)


def get_directory_sizes(root):
    global dir_dict
    for child in root.children:
        get_directory_sizes(child)

    if root.name == "/":
        return

    if root.isFile:
        parent_dir = root.parent
        parent_full_address = get_node_full_address(parent_dir)
        if dir_dict.get(parent_full_address) == None:
            dir_dict[parent_full_address] = root.size
        else:
            dir_dict[parent_full_address] = dir_dict[parent_full_address] + root.size
        # print(f"I am {root.name} and I'm incrementing {root.parent.name} (current size: {dir_dict[parent_full_address]}) by {root.size}")
    else:
        parent_dir = root.parent
        parent_full_address = get_node_full_address(parent_dir)
        root_full_address = get_node_full_address(root)
        if dir_dict.get(parent_full_address) == None:
            dir_dict[parent_full_address] = dir_dict[root_full_address]
        else:
            dir_dict[parent_full_address] = dir_dict[parent_full_address] + dir_dict[root_full_address]
        # print(f"I am {root.name} and I'm incrementing {root.parent.name} by {dir_dict[root_full_address]}")


def get_node_full_address(node):
    stack = [node.name]

    while node.parent:
        node = node.parent
        stack.append(node.name)

    # print(stack)
    address_string = ""
    for i in range(len(stack)):
        address_string += stack[len(stack) - i - 1]
        address_string += "/"

    if address_string == "//":
        return "/"

    address_string = address_string[1:-1]
    # print(address_string)
    return address_string

class Node:
    def __init__(self, name, isFile, size=0):
        self.name = name
        self.isFile = isFile
        self.size = size
        self.children = []
        self.parent = None

    def addChild(self, Node):
        self.children.append(Node)


if __name__ == "__main__":
    main()
