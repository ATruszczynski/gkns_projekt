import math
from os import name, system

short_sep = "-----------"
long_sep = 3 * short_sep


def analyse_word(word: [str]) -> (bool, dict):  # zwraca czy słowo ma powtórzenie
    result = False
    repetition = None
    analysis_dict = {}

    for hole_index in range(1, len(word)):
        left_len = hole_index
        right_len = len(word) - hole_index
        len_to_analyse = min(left_len, right_len)

        for l in range(1, len_to_analyse + 1):
            dict_left = {}
            dict_right = {}
            for i in range(hole_index - l, hole_index):
                letter = word[i]
                if letter not in dict_left:
                    dict_left[letter] = 1
                else:
                    dict_left[letter] += 1

            for i in range(hole_index, hole_index + l):
                letter = word[i]
                if letter not in dict_right:
                    dict_right[letter] = 1
                else:
                    dict_right[letter] += 1

            dict_same = dict_left == dict_right
            result = result or dict_same
            if result and repetition is None:
                repetition = (hole_index, l)

            if hole_index not in analysis_dict:
                analysis_dict[hole_index] = {}

            analysis_dict[hole_index][l] = (dict_left, dict_right)

    return result, repetition, analysis_dict

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