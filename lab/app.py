import sys
import datetime

usage = """
USAGE:
first arg: digit from 0 to 9
second arg (optional): string bin, oct, hex
"""


def logger(func_to_decorate):
    with open("log.txt", "a") as file:
        file.write("{0:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.now()) + " : " + func_to_decorate.__name__ + "\n")
    return func_to_decorate


class RangeException(Exception):
    def __str__(self):
        return "argv[1] is not in 0-9"


class ConvertTypeException(Exception):
    def __str__(self):
        return "argv[2] is not in (bin, oct, hex)"


class ArgsCountException(Exception):
    def __str__(self):
        return "arguments expected"


@logger
def digit_to_str(digit):
    if digit == 0:
        string = "\nЭто нулb"
    elif digit == 1:
        string = "\nЭто одын"
    elif digit == 2:
        string = "\nЭто два"
    elif digit == 3:
        string = "\nЭто три"
    elif digit == 4:
        string = "\nЭто четыре"
    elif digit == 5:
        string = "\nЭто пятb"
    elif digit == 6:
        string = "\nЭто шестb"
    elif digit == 7:
        string = "\nЭто семb"
    elif digit == 8:
        string = "\nЭто восемb"
    elif digit == 9:
        string = "\nЭто девятb"
    else:
        string = None
    return string


@logger
def check_console_args():
    if len(sys.argv) < 2:
        raise ArgsCountException
    if not str(sys.argv[1]).isdigit():
        raise TypeError
    if not int(sys.argv[1]) in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        raise RangeException
    if len(sys.argv) == 3:
        if sys.argv[2] not in ("bin", "oct", "hex"):
            raise ConvertTypeException


@logger
def to_bin_str(digit):
    return str(bin(digit))[2:]


@logger
def to_hex_str(digit):
    return str(hex(digit))[2:]


@logger
def to_oct_str(digit):
    return str(oct(digit))[2:]


if __name__ == "__main__":

    try:
        check_console_args()
    except Exception as e:
        print(e)
        print(usage)
        exit(1)

    sys.argv[1] = int(sys.argv[1])

    if len(sys.argv) == 2:
        string = digit_to_str((int(sys.argv[1])))
        print(string)
    elif len(sys.argv) == 3:
        if sys.argv[2] == "bin":
            print(to_bin_str(sys.argv[1]))
        elif sys.argv[2] == "oct":
            print(to_oct_str(sys.argv[1]))
        elif sys.argv[2] == "hex":
            print(to_hex_str(sys.argv[1]))
