from os import path
from pathlib import Path

import numpy as np

file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')


big_map = np.zeros((1000, 1000), dtype=int)
with open(file_i, 'r') as f:
    for line in f:
        coords = [int(n) for n in line.replace('-> ', '').replace(',', ' ').split()]
        x = [coords[0], coords[2]]
        y = [coords[1], coords[3]]
        x = list(range(min(x), max(x) + 1)) if x[0] != x[1] else x[0]
        y = list(range(min(y), max(y) + 1)) if y[0] != y[1] else y[0]
        # part 1
        if coords[0] == coords[2] or coords[1] == coords[3]:
            big_map[y, x] += 1
        # part 2 - comment the else clause for part 1 result
        else:
            if coords[0] > coords[2]:
                x.reverse()
            if coords[1] > coords[3]:
                y.reverse()
            big_map[y, x] += 1
danger_zone = big_map[np.where(big_map >= 2)]
print(f'{danger_zone.size} dangerous points')
