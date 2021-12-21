from os import path
from pathlib import Path

import numpy as np


class Bingo:
    def __init__(self, input_file: str = None):
        self.input_stream = open(input_file, 'r').readlines()

    @property
    def drawn_numbers(self) -> np.array:
        return np.fromstring(self.input_stream[0], dtype=int, sep=',')

    @property
    def game_cards(self) -> np.ndarray:
        all_cards = []
        for i in range(2, len(self.input_stream), 6):
            items = []
            for j in range(i, i+5):
                items.append([int(number) for number in self.input_stream[j].split()])
            all_cards.append(np.array(items))
        return np.array(all_cards)


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
