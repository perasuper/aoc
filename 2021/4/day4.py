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
    def game_cards(self) -> np.ndarray:
        all_cards = np.array([], dtype=int)
        for i in range(2, len(self.input_stream), 6):
            items = []
            for j in range(i, i+5):
                items.append([int(number) for number in self.input_stream[j].split()])
                new_card = np.array(items)
            # TODO: jotain järkeä tähän paskaan
            if i == 2:  # first card
                all_cards = new_card
            elif i == 8:  # second card
                all_cards = np.stack((all_cards, new_card))
            else:
                all_cards = np.reshape(np.append(all_cards, new_card), (len(all_cards) + 1, 5, 5))
        return all_cards

    def check_cards(self):
        pass


if __name__ == '__main__':
    file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')
    bingo = Bingo(file_i)

    # part 1
    numbers = bingo.drawn_numbers
    cards = bingo.game_cards
    checking_cards = np.zeros_like(bingo.game_cards, dtype=int)
    end = False
    for idx, drawn_number in enumerate(bingo.drawn_numbers):
        checking_cards[np.where(bingo.game_cards == drawn_number)] = 1
        if idx >= 5:
            for x in range(0, 5):
                for id_card, checking_card in enumerate(checking_cards):
                    if all(checking_card[x, :] == 1) or all(checking_card[:, x] == 1):
                        winning_card = cards[id_card, :, :]
                        score = sum(winning_card[np.where(checking_card == 0)]) * drawn_number
                        print(f'BINGO\n{winning_card}\n{checking_card}')
                        print(f'score: {score}')

