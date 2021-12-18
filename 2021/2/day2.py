from os import path
from pathlib import Path

if __name__ == '__main__':
    # part 1
    with open(path.join(Path(__file__).parent.absolute(), 'input.txt'), 'r') as f:
        horizontal_pos = 0
        depth = 0
        for line in f:
            direction = line.split()[0]
            units = int(line.split()[1])
            if direction == 'forward':
                horizontal_pos += units
            elif direction == 'up':
                depth -= units
            elif direction == 'down':
                depth += units
        print(f'horizontal: {horizontal_pos} | depth {depth} | multiplied {horizontal_pos*depth}')

    # part 2
    with open(path.join(Path(__file__).parent.absolute(), 'input.txt'), 'r') as f:
        horizontal_pos = 0
        depth = 0
        aim = 0
        for line in f:
            direction = line.split()[0]
            units = int(line.split()[1])
            if direction == 'forward':
                horizontal_pos += units
                depth += aim * units
            elif direction == 'up':
                aim -= units
            elif direction == 'down':
                aim += units
        print(f'horizontal: {horizontal_pos} | depth {depth} | multiplied {horizontal_pos*depth}')
