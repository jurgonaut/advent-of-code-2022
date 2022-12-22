import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    args = parser.parse_args()

    x = 1
    cycle = 1
    signal_strength = 0

    crt_column = 0
    crt_row = 0

    screen = []
    for r in range(0, 6):
        row = []
        for column in range(0, 40):
            row.append(" ")
        screen.append(row)

    with open(args.input) as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        command = line.split(" ")
        print(f"{command}")

        for c in command:
            print(f"before cycle {cycle}, strength {x}")

            print(f"crt: row {crt_row} column {crt_column}")
            if crt_column in (x -1, x, x+1):
                screen[crt_row][crt_column] = "█"

            crt_column += 1
            if crt_column > 39:
                crt_column = 0
                crt_row += 1

            if c == "noop":
                cycle += 1
            elif c == "addx":
                cycle += 1
            else:
                cycle += 1
                x += int(c)
            
            print(f"after cycle {cycle}, strength {x}")

            if cycle in (20, 60, 100, 140, 180, 220):
                signal_strength += x * cycle

    print(f"Signal strength: {signal_strength}")

    for row in screen:
        print(row)
    
    