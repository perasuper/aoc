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
        x = list(range(min(x), max(x)))
        y = list(range(min(y), max(y)))
        if len(x) == 0:
            x = coords[0]
        elif len(y) == 0:
            y = coords[1]
        big_map[x, y] += 1
danger_zone = big_map[np.where(big_map >= 2)]
print(f'{len(danger_zone)} dangerous points')