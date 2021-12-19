from os import path
from pathlib import Path

import numpy as np


def array2bin(arr: np.array):
    assert all([n in (0, 1) for n in arr]), f'all values in {arr} should be either 0 or 1'
    binstr = '0b'
    for n in arr:
        binstr += str(n)
    return binstr


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
            oxygen_gen_id = np.where(diagnostic_report[:, 0] == oxy_most_common)
            co2_scrub_id = np.where(diagnostic_report[:, 0] == co2_least_common)
            oxygen_gen = diagnostic_report[oxygen_gen_id[0], :]
            co2_scrub = diagnostic_report[co2_scrub_id[0], :]
            db = 1
        else:
            if len(oxygen_gen) > 1:
                count_oxy = np.bincount(oxygen_gen[:, i])
                oxy_most_common = 0 if count_oxy[0] > count_oxy[1] else 1
                oxygen_gen_id = np.where(oxygen_gen[:, i] == oxy_most_common)
                oxygen_gen = oxygen_gen[oxygen_gen_id[0], :]
            if len(co2_scrub) > 1:
                count_co2 = np.bincount(co2_scrub[:, i])
                co2_least_common = 0 if count_co2[0] <= count_co2[1] else 1
                co2_scrub_id = np.where(co2_scrub[:, i] == co2_least_common)
                co2_scrub = co2_scrub[co2_scrub_id[0], :]

    oxygen_gen = array2bin(oxygen_gen[0])
    co2_scrub = array2bin(co2_scrub[0])
    product = int(oxygen_gen, 2) * int(co2_scrub, 2)
    print(product)
    print(bin(product))
