import time


def get_input(day, example=False):
    with open("Inputs/input_" + (day if not example else day + "_example")) as f:
        lines = list(map(lambda line: line.strip(), f))
    f.close()
    return lines


num_map = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"
        }

inverse_num_map = {v: str(k) for k, v in num_map.items()}

def num_to_eng(n):
    try:
        return num_map[n]
    except KeyError:
        return None


def timerun(func):
    now = time.time()
    val = func.run()
    print(func.__name__, ":", val, ':', time.time() - now)
