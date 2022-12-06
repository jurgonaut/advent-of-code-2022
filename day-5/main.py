import argparse
import re
import copy

def initialize_stacks(initial_state):
    stacks = []

    while True:
        line = initial_state.pop()

        crates = re.finditer(r"\[([A-Z])\]", line)

        for c in crates:
            column = int(c.span()[0] / 4) # every crate takes up 4 chars eg: "[A] "
            value = c.group(1) # get the group 1 inside the "()"
            
            if column >= len(stacks):
                stacks.append([])
            stacks[column].append(value)

        if not initial_state:
            break

    return stacks

def get_move_parameters(line):
    number_of_crates = int(re.search(r"move (\d{1,})", line).group(1))
    from_stack = int(re.search(r"from (\d{1,})", line).group(1)) -1 # offset by 1 to start from 0
    to_stack = int(re.search(r"to (\d{1,})", line).group(1)) -1 # offset by 1 to start from 0

    return number_of_crates, from_stack, to_stack

def move(stacks, moves):
    while True:
        move = moves.pop(0)

        number_of_crates, from_stack, to_stack = get_move_parameters(move)
   
        for i in range(number_of_crates):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)

        if not moves:
            break

def move_2(stacks, moves):
    while True:
        move = moves.pop(0)

        number_of_crates, from_stack, to_stack = get_move_parameters(move)
   
        crates = []
        for i in range(number_of_crates):
            crates.append(stacks[from_stack].pop())

        crates.reverse()
        stacks[to_stack].extend(crates)

        if not moves:
            break

def get_result(stacks):
    solution = ""

    for s in stacks:
        solution += s[-1]

    return solution

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    parser.add_argument(
        "--first", help="first half solution", action="store_true")
    parser.add_argument(
        "--second", help="second half solution", action="store_true")
    args = parser.parse_args()

    file = open(args.input, mode='r')
    input = file.read()
    file.close()

    input_separated = input.split("\n\n")
    initial_state = input_separated[0].split("\n")
    moves = input_separated[1].split("\n")

    columns = initial_state.pop() # Don't really need the column numbers, just remove them.
    stacks = initialize_stacks(initial_state)
    
    if args.first:
        m = copy.deepcopy(moves)
        s = copy.deepcopy(stacks)
        move(s, m)
        print(get_result(s))

    if args.second:
        m = copy.deepcopy(moves)
        s = copy.deepcopy(stacks)
        move_2(s, m)
        print(get_result(s))
