from os import path
from pathlib import Path

import numpy as np


class Bingo:
    def __init__(self, input_file: str = None):
        self.input_stream = self.__read_input(input_file)

    @staticmethod
    def __read_input(file_name: str) -> list:
        return open(file_name, 'r').readlines()

    @property
    def drawn_numbers(self) -> np.array:
        return np.fromstring(self.input_stream[0], dtype=int, sep=',')

    @property
    def game_boards(self) -> np.ndarray:
        all_boards = np.array([])
        for i in range(2, len(self.input_stream), 6):
            one_board = np.array([])
            items = []
            for j in range(i, i+5):
                items.append([int(number) for number in self.input_stream[j].split()])
                one_board = np.array(items)
            if len(all_boards) == 0:
                all_boards = one_board
            else:
                all_boards = np.stack([all_boards, one_board])
        return all_boards

if __name__ == '__main__':
    file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')
    bingo = Bingo(file_i)
    numbers = bingo.drawn_numbers
    boards = bingo.game_boards
    db = 1

