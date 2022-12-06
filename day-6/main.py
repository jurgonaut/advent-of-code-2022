import argparse

def find_start_of_marker(input, window_size):
        i = 0

        while (i + window_size) < len(input) +1:
            chunk = input[i:i+window_size]

            # Check if the set from chunk contains the same number of chars 
            # as the window size, this means that there are only unique chars
            # in the chunk and we found the start marker.
            if (len(set(chunk))) == window_size:
                return i+window_size

            i += 1

        raise RuntimeError("Couldn't find start marker")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    parser.add_argument(
        "--first", help="first half solution", action="store_true")
    parser.add_argument(
        "--second", help="second half solution", action="store_true")
    args = parser.parse_args()

    file = open(args.input,mode='r')
    input = file.read()
    file.close()

    if args.first:
        start_marker = find_start_of_marker(input, 4)
        print(f"First part start marker: {start_marker}")

    if args.second:
        start_marker = find_start_of_marker(input, 14)
        print(f"Second part start marker: {start_marker}")
