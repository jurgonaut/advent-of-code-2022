import argparse
import re
import copy

def initialize_stacks_2(line, stacks):
    crates = re.finditer(r"\[([A-Z])\]", line)

    # the crates object has roughly this structure: {group: Z, span: [0,3]}, {group: M, span: [4,7]}, ....
    for c in crates:
        column = int(c.span()[0] / 4) # every crate takes up 4 chars eg: "[A] "
        value = c.group(1) # get the group 1 inside the "()"
        
        if column >= len(stacks):
            stacks.append([])
        stacks[column].append(value)

def get_move_parameters(line):
    number_of_crates = int(re.search(r"move (\d{1,})", line).group(1))
    from_stack = int(re.search(r"from (\d{1,})", line).group(1)) -1 # offset by 1 to start from 0
    to_stack = int(re.search(r"to (\d{1,})", line).group(1)) -1 # offset by 1 to start from 0

    return number_of_crates, from_stack, to_stack

def move(stacks, move):
    number_of_crates, from_stack, to_stack = get_move_parameters(move)
   
    crates = stacks[from_stack][-number_of_crates:]
    del stacks[from_stack][-number_of_crates:]
    crates.reverse()
    stacks[to_stack].extend(crates)

def move_2(stacks, move):
    number_of_crates, from_stack, to_stack = get_move_parameters(move)
   
    crates = stacks[from_stack][-number_of_crates:]
    del stacks[from_stack][-number_of_crates:]
    stacks[to_stack].extend(crates)

def get_result(stacks):
    solution = ""

    for s in stacks:
        solution += s[-1]

    return solution

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    file = open(args.input, mode='r')
    input = file.read()
    file.close()

    input_separated = input.split("\n\n")
    initial_state = input_separated[0].split("\n")
    moves = input_separated[1].split("\n")

    stacks_1 = []
    for s in initial_state[::-1]: # Loop from end, so in our case from the column numbers to the top of the crates 
        initialize_stacks_2(s, stacks_1)

    # Need to create a deep copy because otherwise the moves override themselves.
    stacks_2 = copy.deepcopy(stacks_1)
    
    for m in moves:
        move(stacks_1, m)
        move_2(stacks_2, m)

    print(get_result(stacks_1))
    print(get_result(stacks_2))
