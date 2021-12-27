from os import path
from pathlib import Path
from itertools import product

import numpy as np


class Heightmap:
    def __init__(self, input_text: str):
        self.map = self._text2map(input_text)

    @staticmethod
    def _text2map(text_input: str) -> np.ndarray:
        with open(text_input) as f:
            arr = []
            for line in f:
                arr.append([int(num) for num in line.strip()])
            return np.array(arr)

    @property
    def low_points(self) -> np.ndarray:
        lows = np.zeros_like(self.map)
        for row, col in product(range(self.map.shape[0]), range(self.map.shape[1])):
            if self._is_low_point(row, col):
                lows[row, col] = self.map[row, col] + 1
        return lows

    @property
    def basins(self) -> np.ndarray:
        basin_map = np.zeros_like(self.map)
        low_points = np.nonzero(heightmap.low_points)
        for row, col in zip(low_points[0], low_points[1]):
            basin_map[row, col] = self._basin_size(np.copy(self.map), row, col)
        return basin_map

    @staticmethod
    def _basin_size(map_cpy: np.ndarray, row: int, col: int) -> int:
        size = 0
        if (0 <= row < map_cpy.shape[0]) and (0 <= col < map_cpy.shape[1]):
            if map_cpy[row, col] < 9 and map_cpy[row, col] != -1:
                map_cpy[row, col] = -1
                size = 1
                size += Heightmap._basin_size(map_cpy, row - 1, col)
                size += Heightmap._basin_size(map_cpy, row + 1, col)
                size += Heightmap._basin_size(map_cpy, row, col - 1)
                size += Heightmap._basin_size(map_cpy, row, col + 1)
        return size

    def _is_low_point(self, row: int, col: int) -> bool:
        for row_step, col_step in self._get_step_range(row, col):
            if self.map[row, col] >= self.map[row+row_step, col+col_step]:
                return False
        return True

    def _get_step_range(self, row: int, col: int) -> list:
        step_range = []
        # points with 4 neighbours
        if (0 < row < self.map.shape[0]-1) and (0 < col < self.map.shape[1]-1):
            step_range = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # edge rows
        if (row == 0) and (0 < col < self.map.shape[1] - 1):
            step_range = [(0, -1), (0, 1), (1, 0)]
        elif (row == self.map.shape[0]-1) and (0 < col < self.map.shape[1]-1):
            step_range = [(0, -1), (0, 1), (-1, 0)]
        elif (col == 0) and (0 < row < self.map.shape[0] - 1):
            step_range = [(0, 1), (-1, 0), (1, 0)]
        elif (col == self.map.shape[1]-1) and (0 < row < self.map.shape[0]-1):
            step_range = [(0, -1), (-1, 0), (1, 0)]

        # corner points
        if (row, col) == (0, 0):
            step_range = [(1, 0), (0, 1)]
        elif (row, col) == (0, self.map.shape[1]-1):
            step_range = [(1, 0), (0, -1)]
        elif (row, col) == (self.map.shape[0]-1, 0):
            step_range = [(-1, 0), (0, 1)]
        elif (row, col) == (self.map.shape[0]-1, self.map.shape[1]-1):
            step_range = [(-1, 0), (0, -1)]

        return step_range


if __name__ == '__main__':

    file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')
    heightmap = Heightmap(file_i)

    # pt 1
    print(f'pt1 sum of risk levels: {np.sum(heightmap.low_points)}')
    map_cpy = np.copy(heightmap.map)

    # pt 2
    basins = heightmap.basins[np.nonzero(heightmap.basins)]
    basins.sort()
    print(f'pt2 product of three biggest basins: {np.prod(basins[-3:])}')
