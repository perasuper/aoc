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
        for i in range(0, diagnostic_report.shape[1]-1):
            count = np.bincount(diagnostic_report[:, i])
            dig_gamma = 0 if count[0] > count[1] else 1
            dig_epsilon = 0 if count[0] < count[1] else 1
            gammarate += str(dig_gamma)
            epsilon_rate += str(dig_epsilon)
            product = int(gammarate, 2) * int(epsilon_rate,2)

    output = f'gammarate: { gammarate} | epsilonrate:  {epsilon_rate}' + \
             f'\nmultiplication: {gammarate }* {epsilon_rate} = {bin(product)} (dec:{product})'
    print(output)
