import argparse
import copy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    with open(args.input) as f:
        lines = f.readlines()

    current_dir_path = []
    directories = {}

    for line in lines:
        line = line.strip()
        args = line.split(" ")

        if line == "$ cd ..":
            current_dir_path.pop()

        elif line.startswith("$ cd"):
            # If root dir "/" replace it with "" els use the dir name
            args[2] = "" if args[2] == "/" else args[2]
            
            current_dir_path.append(args[2])
            dir_name = "/".join(current_dir_path)
            directories[dir_name] = 0

        elif line[0].isdigit():
            # Make deep copy otherwise the pop() will modify the original list
            tmp_dir_path = copy.deepcopy(current_dir_path)

            # remove the directories from end until we reach the root 
            # and keep adding the size value to the current dir.
            while tmp_dir_path:
                dir_name = "/".join(tmp_dir_path)
                directories[dir_name] += int(args[0])
                tmp_dir_path.pop()

    result_1 = 0
    for key, value in directories.items():
        if value <= 100000:
            result_1 += value
    print(f"Part 1: {result_1}")

    total_space = 70000000
    needed_space = 30000000
    occupied_space = directories.get("")
    unused_space = total_space - occupied_space
    dir_to_delete_size = needed_space - unused_space

    result_2 = directories.get("")
    for key, value in directories.items():
        if value > dir_to_delete_size and value < result_2:
            result_2 = value
    print(f"Part 2: {result_2}")
