import math
import time
import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map

#Game 1: 5 red, 1 green, 2 blue; 2 green, 8 blue, 6 red; 8 red, 3 blue, 2 green; 6 red, 1 green, 19 blue; 1 red, 17 blue


def run():
    input = get_input('2')
    return sum(list(map(lambda line: validGame(line), input)))

def validGame(line):
    maxBag = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    line = line[4:] # prune "game" from line
    [id, rest] = line.split(':')

    games = rest.split(';')
    for game in games:
        for bag in game.split(','):
            curBag = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            bag = bag.strip().split(' ')
            curBag[bag[1]] += int(bag[0])
            if curBag[bag[1]] > maxBag[bag[1]]:
                return 0

    return int(id.strip())
