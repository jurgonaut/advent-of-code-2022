import argparse

def find_start_of_marker(input, window_size):
        """
            Parse the input in chunks of window_size, then check if the char is 
            in the unique_chars set. Then if the unique_chars length is equal to the 
            window_size it means we have only unique chars and we found the start marker.
        """

        i = 0

        while (i + window_size) < len(input) +1:
            unique_chars = set()
            
            chunk = input[i:i+window_size]
            
            for char in chunk:
                if char in unique_chars:
                    break
                unique_chars.add(char)

            if len(unique_chars) == window_size:
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
