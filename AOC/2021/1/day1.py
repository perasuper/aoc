from os import path
from pathlib import Path

if __name__ == '__main__':

    # part 1
    with open(path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
        prev = []
        increased = 0
        for line in f:
            if prev and int(line) > prev:
                increased += 1
            prev = int(line)
        print(increased)

    # part 2
    with open(path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
        window4 = []
        increased = 0
        for line in f:
            window4.append(int(line))
            if len(window4) == 5:
                window4.pop(0)
                if sum(window4[:3]) < sum(window4[1:]):
                    increased += 1
        print(increased)
