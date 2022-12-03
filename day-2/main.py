import argparse

# A = Rock
# B = Paper
# C = Scissors


class Shape():
    def __init__(self, shape, wins_to, loses_to):
        self.shape = shape
        self.wins_to = wins_to
        self.loses_to = loses_to

    def __repr__(self):
        return f"Shape: {self.shape}, wins to: {self.wins_to}, loses to: {self.loses_to}"


def calculate_first(input_1, input_2, shapes):
    input_2_shape = find_shape(input_2, shapes)

    if input_2_shape.shape == input_1:
        return calculate_shape_score(input_2) + 3
    elif input_2_shape.wins_to == input_1:
        return calculate_shape_score(input_2) + 6
    elif input_2_shape.loses_to == input_1:
        return calculate_shape_score(input_2)


def calculate_second(input_1, outcome, shapes):
    input_1_shape = find_shape(input_1, shapes)

    if outcome == "Y":  # draw
        return calculate_shape_score(input_1_shape.shape) + 3
    elif outcome == "X":  # loose
        return calculate_shape_score(input_1_shape.wins_to)
    elif outcome == "Z":  # wind
        return calculate_shape_score(input_1_shape.loses_to) + 6


def find_shape(input, shapes):
    for s in shapes:
        if s.shape == normalize_input(input):
            return s


def normalize_input(input):
    input_map = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    normalize_input = input_map.get(input)
    if normalize_input:
        return normalize_input
    return input


def calculate_shape_score(shape):
    shape_score_map = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    return shape_score_map.get(normalize_input(shape))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    parser.add_argument(
        "--first", help="first half solution", action="store_true")
    parser.add_argument(
        "--second", help="second half solution", action="store_true")
    args = parser.parse_args()

    shapes = [
        Shape("A", "C", "B"),
        Shape("B", "A", "C"),
        Shape("C", "B", "A")
    ]

    if args.first:
        total_score = 0
        with open(args.input) as file:
            for line in file:
                player_1 = line.split()[0]
                player_2 = line.split()[1]
                total_score += calculate_first(player_1, player_2, shapes)
        print(total_score)

    if args.second:
        total_score = 0
        with open(args.input) as file:
            for line in file:
                player_1 = line.split()[0]
                outcome = line.split()[1]
                score = calculate_second(player_1, outcome, shapes)
                total_score += score
        print(total_score)
