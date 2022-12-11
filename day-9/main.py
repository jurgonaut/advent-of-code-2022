import argparse
import copy

class TailNode():
    def __init__(self, start_y, start_x, pos):
        self.y = start_y
        self.x = start_x
        self.position = pos
        self.next = None

    def __repr__(self):
        return f'pos: {self.position} y: {self.y}, x: {self.x}'

def are_nodes_touching(node_1, node_2):
    # Get the absolute difference between the head and tail y and x positions
    # Especially in the tricky cases where head = (-2, -1) and tail (-1, -1).
    # The head and tail are touching when the y and x diff are < 2

    diff_y = abs(node_1.y - node_2.y)
    diff_x = abs(node_1.x - node_2.x)
    
    if diff_y < 2 and diff_x < 2:
        return True
    return False

def get_nodes_diff(node_1, node_2):
    # Get the diff in y and x position between nodes, in other words
    # get the direction in which node 2 need to move to arrive at the 
    # correct position. Before returning we need to normalize the result, 
    # we don't want values larger that 1

    diff_y = node_1.y - node_2.y
    diff_x = node_1.x - node_2.x

    if diff_x > 1:
        diff_x = 1
    if diff_x < -1:
        diff_x = -1

    if diff_y > 1:
        diff_y = 1
    if diff_y < -1:
        diff_y = -1

    return diff_y, diff_x

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    with open(args.input) as f:
        lines = f.readlines()

    # Create starting position for tail and 
    # initialize all the tail nodes
    tail_start = TailNode(0, 0, 0)
    
    current = None
    for i in range(0, 9):
        if not current:
            current = tail_start

        current.next = TailNode(0, 0, i+1)
        current = current.next

    # initialize unique positions, we are using 
    # the formant y|x for storing the keys
    unique_positions_part_1 = {"0|0": 0}
    unique_positions_part_2 = {"0|0": 0}

    # Staring position for the rope head
    y, x = 0, 0

    for line in lines:
        line = line.strip()

        direction, steps = line.split(" ")[0], int(line.split(" ")[1])
        
        for s in range(0, steps):
            if direction == "R":
                x += 1
            if direction == "L":
                x -= 1
            if direction == "U":
                y += 1
            if direction == "D":
                y -= 1

            next_node = TailNode(y, x, -1)

            current = tail_start

            while current.next:
                if are_nodes_touching(next_node, current):
                    break
                
                tmp = current

                diff_y, diff_x = get_nodes_diff(next_node, current)

                current.y = current.y + 1 * diff_y
                current.x = current.x + 1 * diff_x

                if current.position == 0:
                    key = f"{current.y}|{current.x}"
                    if not unique_positions_part_1.get(key):
                        unique_positions_part_1[key] = 0

                if current.position == 8:
                    key = f"{current.y}|{current.x}"
                    if not unique_positions_part_2.get(key):
                        unique_positions_part_2[key] = 0

                next_node = tmp
                current = current.next

    print(f"Part 1: {len(unique_positions_part_1)}, part 2: {len(unique_positions_part_2)}")