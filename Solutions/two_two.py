import math
import time

import numpy as numpy

import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map

#Game 1: 5 red, 1 green, 2 blue; 2 green, 8 blue, 6 red; 8 red, 3 blue, 2 green; 6 red, 1 green, 19 blue; 1 red, 17 blue


def run():
    input = get_input('2')
    return sum(list(map(lambda line: validGame(line), input)))

def validGame(line):
    curBag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    line = line[4:] # prune "game" from line
    [_, rest] = line.split(':')

    game = rest.split(';')
    for round in game:
        for draw in round.split(','):
            draw = draw.strip().split(' ')
            if int(draw[0]) > curBag[draw[1]]:
                curBag[draw[1]] = int(draw[0])

    return numpy.prod(list(curBag.values()))

