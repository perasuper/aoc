from os import path
from pathlib import Path

import numpy as np

file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')
with open(file_i) as f:
    locations = np.array([int(x) for x in f.readline().strip().split(",")])


def consumption_part2(point, distance):
    return sum(list(range(1, abs(point-distance)+1)))


pt2 = np.vectorize(consumption_part2)


mean = int(sum(locations) / len(locations))
search_range = 0  # how many samples tested on both sides of mean (140 pt1, 0 (ie. mean for pt2))
search_window = list(range(mean-search_range, mean+search_range+1))

lowest = (9999999999, 0)
not_changed_in = 0
for idx, x in enumerate(search_window):
    # fuel_consumption = sum(abs(locations - x))   # pt1
    fuel_consumption = sum(pt2(locations, x))  # pt2
    if fuel_consumption < lowest[0]:
        lowest = (fuel_consumption, search_window[idx])
        not_changed_in = 0
    not_changed_in += 1
    if not_changed_in >= 10:
        break
    print(f'fuel_consumption (x={x}): {fuel_consumption}')
print(f'lowest {lowest[0]} for point {lowest[1]}')
print(f'mean {mean}')
