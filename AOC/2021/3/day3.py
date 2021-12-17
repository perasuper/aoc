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

        gammarate = ''
        for i in range(0, diagnostic_report.shape[1]-1):
            count = np.bincount(diagnostic_report[:, i])
            dig = 0 if count[0] > count[1] else 1
            gammarate += str(dig)
        epsilon_rate = 1
