import argparse


def input_to_coordinates(input):
    coordinates = []

    for line in lines:
        line = line.strip()
        trees = []
        for l in line:
            trees.append(int(l))
        coordinates.append(trees)

    return coordinates


def search_horizontal(start, end, step, row, visible):
    highest = -1
    for i in range(start, end, step):
        if coordinates[row][i] > highest:
            key = f"{row}|{i}"

            if not visible.get(key):
                visible[key] = coordinates[row][i]

            highest = coordinates[row][i]

            if highest == 9:
                break


def search_vertical(start, end, step, col, visible):
    highest = -1
    for i in range(start, end, step):
        if coordinates[i][col] > highest:
            key = f"{i}|{col}"

            if not visible.get(key):
                visible[key] = coordinates[i][col]

            highest = coordinates[i][col]

            if highest == 9:
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    with open(args.input) as f:
        lines = f.readlines()

    coordinates = input_to_coordinates(lines)

    visible = {}

    for y, row in enumerate(coordinates):
        search_horizontal(0, len(coordinates[0]), 1, y, visible)
        search_horizontal(len(coordinates[0])-1, -1, -1, y, visible)

    for x, col in enumerate(coordinates[0]):
        search_vertical(0, len(coordinates), 1, x, visible)
        search_vertical(len(coordinates)-1, -1, -1, x, visible)

    print(f"visible {len(visible)}")

    highest_scenic_score = 0

    for y, row in enumerate(coordinates):
        for x, tree in enumerate(coordinates[y]):
            scenic_value_in_all_directions = [0, 0, 0, 0]

            for u in range(y - 1, -1, -1):
                scenic_value_in_all_directions[0] += 1
                if coordinates[u][x] >= coordinates[y][x]:
                    break

            for l in range(x - 1, - 1, -1):
                scenic_value_in_all_directions[1] += 1
                if coordinates[y][l] >= coordinates[y][x]:
                    break

            for r in range(x + 1, len(coordinates[y])):
                scenic_value_in_all_directions[2] += 1
                if coordinates[y][r] >= coordinates[y][x]:
                    break

            for d in range(y + 1, len(coordinates)):
                scenic_value_in_all_directions[3] += 1
                if coordinates[d][x] >= coordinates[y][x]:
                    break

            current_scenic_value = scenic_value_in_all_directions[0] * scenic_value_in_all_directions[1] * \
                scenic_value_in_all_directions[2] * \
                scenic_value_in_all_directions[3]

            if current_scenic_value > highest_scenic_score:
                highest_scenic_score = current_scenic_value

    print(f"Highest scenic score {highest_scenic_score}")
