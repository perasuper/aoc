from os import path
from pathlib import Path


file_i = path.join(Path(__file__).parent.absolute(), 'input.txt')
with open(file_i) as f:
    start_fish = [int(x) for x in f.readline().strip().split(",")]

db = 1
fish_states = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for f in start_fish:
    fish_states[f] += 1

days = 256
for i in range(days-1):
    fish_states = fish_states[1:] + fish_states[:1]
    fish_states[7] += fish_states[0]

print(f'{sum(fish_states)} fish')

