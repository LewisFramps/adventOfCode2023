import math
import time


import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map

'''
--- Day 1: Trebuchet?! ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two,
 three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:
'''

def run():
    input = get_input('1')
    return sum(list(map(lambda line: getSum(line), input)))


def getSum(line):
    lval = -1
    rval = -1
    lhs = []
    rhs = []

    def check(list, char):
        # easy! we got a number
        if char.isnumeric():
            return char
        # check if we have a number in the list. This is dumb and bad
        num = next((numEng for numEng in num_map.values() if numEng in ''.join(list)), None)
        if num:
            return inverse_num_map[num]
        return -1

    for i, _ in enumerate(line):
        if lval is -1:
            lhs.append(line[i])
            lval = check(lhs, line[i])

        if rval is -1:
            rhs.insert(0, line[-(i + 1)])
            rval = check(rhs, line[-(i + 1)])

        # value found!
        if lval is not -1 and rval is not -1:
            return int(lval + rval)

    return 0

