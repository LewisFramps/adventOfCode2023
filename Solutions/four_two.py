import math
import time
import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map


def run():
    input = get_input('4')
    copies = [1 for i in range(len(input))]
    for i, line in enumerate(input):
        score = scoreCard(line)
        counter = i + 1
        while score > 0 and counter < len(copies):
            copies[counter] += copies[i]
            score -= 1
            counter += 1
    return sum(copies)

def scoreCard(line):
    [winners, numbers] = line.split("|")
    winners = [int(n) for n in winners.strip().split(" ")[2:] if n.isnumeric()]
    numbers = [int(n) for n in numbers.split(" ") if n.isnumeric()]
    wins = sum(n in winners for n in numbers)
    if wins == 0:
        return 0
    return wins
