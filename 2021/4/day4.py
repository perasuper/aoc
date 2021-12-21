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


if __name__ == '__main__':
    file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')
    bingo = Bingo(file_i)
    checking_cards = np.zeros_like(bingo.game_cards, dtype=int)
    won_cards = []
    for idx, drawn_number in enumerate(bingo.drawn_numbers):
        checking_cards[np.where(bingo.game_cards == drawn_number)] = 1
        # Start checking cards after 5 numbers are drawn
        if idx >= 5:
            # use x as index to check all columns and rows
            for x in range(0, 5):
                for id_card, checking_card in enumerate(checking_cards):
                    if (all(checking_card[x, :] == 1) or all(checking_card[:, x] == 1)) and id_card not in won_cards:
                        winning_card = bingo.game_cards[id_card, :, :]
                        score = sum(winning_card[np.where(checking_card == 0)]) * drawn_number
                        # part 1
                        if len(won_cards) == 0:
                            print(f'BINGO ({idx}th number)\n{winning_card}\n{checking_card}')
                            print(f'score: {score}, winning card: {id_card}')
                        # part 2
                        elif len(won_cards) == len(bingo.game_cards) - 1:
                            print(f'\nlast card to get bingo ({idx}th number)\n{winning_card}\n{checking_card}')
                            print(f'score: {score}, winning card: {id_card}')
                        won_cards.append(id_card)
