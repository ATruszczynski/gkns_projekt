import math
from os import name, system

short_sep = "-----------"
long_sep = 3 * short_sep

def ato_word_to_string(word: [str], marker: int = -1, sep:str = "") -> str:
    result = ""

    for i in range(len(word)):
        if marker == i:
            result += sep + "_" + sep
        else:
            result += sep
        result += word[i]
    if marker == len(word):
        result += sep + "_" + sep
    else:
        result += sep

    return result

def flatten_list_of_strings(list: [str], separator: str) -> str:
    result = ""

    for i in range(0, len(list)):
        result += str(list[i])
        if i != len(list) - 1:
            result += separator

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