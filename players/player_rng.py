from players.player_abs import *
import random

class PlayerRng(PlayerAbs):
    def to_string(self):
        return "Gracz losowy"

    def make_move_1(self, word: [str], alphabet: [str], word_analisys: dict, separator: str, word_length: int):
        return random.randrange(0, len(word) + 1)

    def make_move_2(self, word: [str], alphabet: [str], position:int, word_analisys: dict, separator: str, word_length: int):
        return alphabet[random.randrange(0, len(alphabet))]
