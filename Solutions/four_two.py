import math
import time
import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map


def run():
    input = get_input('4')
    copies = [1 for _ in range(len(input))]
    for i, line in enumerate(input):
        for j in range(1, scoreCard(line) + 1):
            copies[i + j] += copies[i]
            if i + j >= len(copies):
                break
    return sum(copies)

def scoreCard(line):
    [winners, numbers] = line.split("|")
    winners = [int(n) for n in winners.strip().split(" ")[2:] if n.isnumeric()]
    numbers = [int(n) for n in numbers.split(" ") if n.isnumeric()]
    return sum(n in winners for n in numbers)
