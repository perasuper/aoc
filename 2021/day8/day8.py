from os import path
from pathlib import Path

import numpy as np


def diff(a, b):
    return "".join([i for i in a if i not in b])


counts = [0] * 4

file_i = path.join(Path(__file__).parent.absolute(), 'example.txt')
with open(file_i) as f:
    for line in f:
# line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
        numbers = [''] * 10
        signal = line.split('|')[0].split()
        output = line.split('|')[1].split()
        signal_digit_lengths = np.char.str_len(signal)
        # counts = [counts[0] + (signal_digit_lengths == 2).sum(), counts[1] + (signal_digit_lengths == 4).sum(), counts[2] +
        #           (signal_digit_lengths == 3).sum(), counts[3] + (signal_digit_lengths == 7).sum()]


        numbers[7] = list(filter(lambda x: len(x) == 3, signal))[0]
        numbers[1] = list(filter(lambda x: len(x) == 2, signal))[0]
        numbers[4] = list(filter(lambda x: len(x) == 4, signal))[0]
        numbers[8] = list(filter(lambda x: len(x) == 7, signal))[0]


        five_longs = np.unique(list(filter(lambda x: len(x) == 5, signal)))
        six_longs = np.unique(list(filter(lambda x: len(x) == 6, signal)))

        for num in five_longs:
            if len(diff(num, numbers[4])) == 3:
                numbers[2] = num
            elif len(diff(num, numbers[4])) == 2:
                if all(l in num for l in numbers[7]):
                    numbers[3] = num
                else:
                    numbers[5] = num

        for num in six_longs:
            if all(l in num for l in numbers[7]):
                if len(diff(num, numbers[4])) == 3:
                    numbers[0] = num
                elif len(diff(num, numbers[4])) == 2:
                    numbers[9] = num
            else:
                numbers[6] = num

        assert all(len(n) >= 2 for n in numbers), 'Some numbers were not decoded'

        output_decoded = ''
        for o in output:
            for idx, num in enumerate(numbers):
                if all(l in num for l in o):
                    output_decoded += str(idx)
                    break
        print(output_decoded)

