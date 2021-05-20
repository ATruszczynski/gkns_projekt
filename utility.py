from players.player_rng import *
from players.player_human import *
from players.player_moves_heuristic import *
from collections import *

pl_dict = { "1": ["Człowiek", type(HumanPlayer)],
            "2": ["Komputer losowy", type(PlayerRng)],
            "3": ["Komputer heurystyka ilości ruchów", type(PlayerMoveHeu)],
            }

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






