import math
import time

import numpy

import utils
from utils import get_input, num_to_eng, num_map, inverse_num_map, strReplace, print2d

'''
'''

def run():
    input = get_input('3')
    parts = []

    def getParts(x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if input[y + i][x + j].isnumeric():
                    c = 1
                    breakout = [False, False]
                    newNum = str(input[y + i][x + j])
                    row = input[y + i]
                    while breakout[0] is False or breakout[1] is False:
                        if breakout[0] is False and x + j + c < len(row) and row[x + j + c].isnumeric():
                            newNum += str(row[x + j + c])
                            input[y + i] = strReplace(input[y + i], x + j + c, '.')
                        else:
                            breakout[0] = True

                        if breakout[1] is False and x + j - c >= 0 and row[x + j - c].isnumeric():
                            newNum = str(row[x + j - c]) + newNum
                            input[y + i] = strReplace(input[y + i], x + j - c, '.')
                        else:
                            breakout[1] = True

                        c += 1
                    parts.append(int(newNum))
                    input[y + i] = strReplace(input[y + i], x+j, ".")


    for y, row in enumerate(input):
        for x, val in enumerate(row):
            if val.isnumeric() is False and val is not '.':
                getParts(x, y)
    print2d(input)
    print(parts)
    print(sum(parts))



    return 0
