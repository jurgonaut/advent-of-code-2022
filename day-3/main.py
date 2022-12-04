import argparse

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def split_rucksack(rucksack):
    rucksack_size = int(len(rucksack) / 2)
    return rucksack[:rucksack_size], rucksack[rucksack_size:]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    parser.add_argument(
        "--first", help="first half solution", action="store_true")
    parser.add_argument(
        "--second", help="second half solution", action="store_true")
    args = parser.parse_args()

    if args.first:
        total_priority = 0
        with open(args.input) as file:
            for line in file:
                compartments_1, compartments_2 = split_rucksack(line.strip())
                common_item = set(compartments_1) & set(compartments_2)
                total_priority += alphabet.find(common_item.pop()) + 1
        print(total_priority)

    if args.second:
        batch = []
        total_priority = 0
        with open(args.input) as file:
            for line in file:
                batch.append(set(line.strip()))
                if len(batch) % 3 == 0:
                    common_item = set(batch[0]) & set(batch[1]) & set(batch[2])
                    total_priority += alphabet.find(common_item.pop()) + 1
                    batch = []
        print(total_priority)
