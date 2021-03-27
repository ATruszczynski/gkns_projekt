import player_abs
from player_rng import *
from player_human import *
from collections import *

pl_dict = { "1": ["Człowiek", type(HumanPlayer)],
            "2": ["Komputer losowy", type(PlayerRng)]}

# TODO zunifikować utility

def pick_option(opt_dictionary: dict):
    while True:
        for k in opt_dictionary:
            print(f"{k} - {opt_dictionary[k][0]}")

        option = input("Wybierz opcję:\n")

        if option in opt_dictionary:
            return opt_dictionary[option][1]
        else:
            print("Niepoprawna opcja")

def analyse_word(word:[str]) -> (bool, dict): # zwraca czy słowo ma powtórzenie
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

def generate_alphabet(length: int, alphabet_base: [str]) -> [str]:
    generator = deque()
    memory = deque([""])
    alphabet = []

    for i in range(length):
        if len(generator) == 0:
            base = memory.popleft()
            for l in alphabet_base:
                generator.append(base + l)

        next = generator.popleft()
        alphabet.append(next)
        memory.append(next)

    return alphabet






