import argparse
import copy

elevation = "abcdefghijklmnopqrstuvwxyz"

def get_neighbors(node):
    y, x = node[0], node[1]
    node_height = coordinates[y][x]
    available_neighbors = []

    directions = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

    for d in directions:
        neighbor_y = d[0]
        neighbor_x = d[1]

        # Check if out of bounds
        if  neighbor_y > len(coordinates) -1 or \
            neighbor_y < 0 or \
            neighbor_x > len(coordinates[0]) -1 or \
            neighbor_x < 0:
            continue
    
        neighbor_height = coordinates[neighbor_y][neighbor_x]
        
        if neighbor_height < node_height -1:
            continue

        available_neighbors.append((neighbor_y, neighbor_x))

    return available_neighbors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    coordinates = []

    start = None
    end = None

    with open(args.input) as f:
        lines = f.readlines()

    for r, line in enumerate(lines):
        line = line.strip()

        row = []
        for c, char in enumerate(line):
            if char == "S":
                start = (r, c)
                row.append(0)
            elif char == "E":
                end = (r, c)
                row.append(25)
            else:
                row.append(int(elevation.find(char)))

        coordinates.append(row)


    part_1 = 0
    part_2 = 0

    queue = [end]
    visited = {end: 0}

    while queue:
        current = queue.pop(0)

        cost = visited.get(current) +1

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                if neighbor == start:
                    part_1 = cost

                y, x = neighbor[0], neighbor[1]
                if coordinates[y][x] == 0:
                    if not part_2:
                        part_2 = cost
                    if part_2 > cost:
                        part_2 = cost
                
                visited[neighbor] = cost
                queue.append(neighbor)

    print(part_1)
    print(part_2)
