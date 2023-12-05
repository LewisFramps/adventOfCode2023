import math
import time


import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map

'''
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a
map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by
December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second
puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you
("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the
sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a
trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been
amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit
and the last digit (in that order) to form a single two-digit number.
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

