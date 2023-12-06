import math
import time
import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map

'''
'''

def run():
    input = get_input('4', False)
    return sum(list(map(lambda line: scoreCard(line), input)))
    return 0

def scoreCard(line):
    [winners, numbers] = line.split("|")
    winners = [int(n) for n in winners.strip().split(" ")[2:] if n.isnumeric()]
    numbers = [int(n) for n in numbers.split(" ") if n.isnumeric()]
    wins = sum(n in winners for n in numbers)
    if wins == 0:
        return 0
    return 2 ** (wins - 1)