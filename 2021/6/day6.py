from os import path
from pathlib import Path

import numpy as np


file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')

with open(file_i, 'r') as f:
    fishes = np.fromstring(f.readline(), dtype=int, sep=',')

for d in range(0, 256):
    fishes -= 1
    fishes = np.append(fishes, np.ones(np.count_nonzero(fishes == -1), dtype=int) * 8)
    fishes[np.where(fishes == -1)] = 6

print(f'{len(fishes)} fishes')


