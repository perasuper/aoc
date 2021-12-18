from os import path
from pathlib import Path

import numpy as np

if __name__ == '__main__':
    # part 1
    diagnostic_report = np.array([])
    with open(path.join(Path(__file__).parent.absolute(), 'input.txt'), 'r') as f:
        for line in f:
            new_binary = np.array([char for char in line.replace('\n', '')]).astype(int)
            if len(diagnostic_report) == 0:
                diagnostic_report = np.append(diagnostic_report, new_binary)
            else:
                diagnostic_report = np.vstack((diagnostic_report, new_binary)).astype(int)

    gammarate = '0b'
    epsilon_rate = '0b'
    for i in range(0, diagnostic_report.shape[1]):
        count = np.bincount(diagnostic_report[:, i])
        dig_gamma, dig_epsilon = ('0', '1') if count[0] > count[1] else ('1', '0')
        gammarate += dig_gamma
        epsilon_rate += dig_epsilon

        product = int(gammarate, 2) * int(epsilon_rate, 2)

    output = f'gamma rate: { gammarate} | epsilon rate:  {epsilon_rate}' + \
             f'\nmultiplication: {gammarate } * {epsilon_rate} = {bin(product)} (dec:{product})'
    print(output)

    # part 2
    oxygen_gen = []
    co2_scrub = []
    for i in range(0, diagnostic_report.shape[1]):
        if i == 0:
            count_oxy = np.bincount(diagnostic_report[:, 0])
            count_co2 = count_oxy
            oxy_most_common = 0 if count_oxy[0] > count_oxy[1] else 1
            co2_least_common = 0 if oxy_most_common == 1 else 1
        else:
            count_oxy = np.bincount(oxygen_gen[:, i])
            count_co2 = np.bincount(co2_scrub[:, i])
            oxy_most_common = 0 if count_oxy[0] > count_oxy[1] else 1
            co2_least_common = 0 if count_co2[0] < count_co2[1] else 1
            oxygen_gen = np.where(oxygen_gen == oxy_most_common)
            co2_scrub = np.where(co2_scrub == co2_least_common)
        count_ones = count[0]
        count_zeros = count[1]


