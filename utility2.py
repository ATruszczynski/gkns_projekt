import math
from os import name, system

short_sep = "-----------"
long_sep = 3 * short_sep

# TODO To nie wygląda dobrze dla alfabetów ze znakami o większej długości
def ato_word_to_string(word: [str], marker: int = -1, sep:str = "") -> str:
    result = ""

    for i in range(len(word)):
        if marker == i:
            result += "_"
        else:
            result += sep
        result += word[i]
    if marker == len(word):
        result += "_"
    else:
        result += sep

    return result

def pick_int(min: int, max: int = math.inf) -> int:
    while True:
        string = input()

        try:
            if "." in string or "," in string:
                raise ValueError

            integer = int(string)

            if integer < min or integer >= max:
                raise ValueError

            break
        except ValueError:
            print("Niepoprawna wartość")

    return integer


def clear():

    # for windows
    if name == 'nt':
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")