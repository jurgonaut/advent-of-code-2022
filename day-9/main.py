import argparse

def is_touching(head, tail):
    # Get the absolute difference between the head and tail y and x positions
    # Especially in the tricky cases where head = (-2, -1) and tail (-1, -1).
    # The head and tail are touching when the y and x diff are < 2

    diff_y = abs(head[0] - tail[0])
    diff_x = abs(head[1] - tail[1])
    
    print(f"diff y {diff_y} diff x {diff_x}")

    if diff_y < 2 and diff_x < 2:
        return True
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    with open(args.input) as f:
        lines = f.readlines()

    tail_index = 0
    
    positions = [(0, 0)]
    unique_positions = {}

    key = f"{positions[0][0]}|{positions[0][1]}"
    unique_positions[key] = 0

    for line in lines:
        line = line.strip()

        direction, steps = line.split(" ")[0], int(line.split(" ")[1])
        print(f"Direction {direction}, steps {steps}")

        for s in range(0, steps):
            new_x = positions[-1][1]
            new_y = positions[-1][0]

            if direction == "R":
                new_x += 1
            if direction == "L":
                new_x -= 1
            if direction == "U":
                new_y += 1
            if direction == "D":
                new_y -= 1

            positions.append((new_y, new_x))
            print(f"New position position {positions[-1]}, tail position {positions[tail_index]}")

            if len(positions) < 2:
                continue

            if not is_touching(positions[-1], positions[tail_index]):
                tail_index = len(positions) -2
                print(f"Not touching, catching up new {positions[tail_index]}")

                key = f"{positions[tail_index][0]}|{positions[tail_index][1]}"
                if not unique_positions.get(key):
                    unique_positions[key] = 0
 
        print("-------------------------------------------\n")

    print(unique_positions)
    print(f"Unique {len(unique_positions)}")