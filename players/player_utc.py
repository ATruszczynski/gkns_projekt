import copy
from node import Node
from players.player_abs import PlayerAbs
from utility3 import play_one_game


class PlayerUCT(PlayerAbs):
    def to_string(self):
        return "Gracz uct"

    def make_move_1(self, word: [str], alphabet: [str], word_analisys: dict, separator: str, word_length: int):
        root = Node(copy.deepcopy(word), -1, "", 2, alphabet)
        for i in range(1000):
            play_one_game(root, alphabet, word_length)
        return root.get_best_move()

    def make_move_2(self, word: [str], alphabet: [str], position: int, word_analisys: dict, separator: str, word_length: int):
        root = Node(copy.deepcopy(word), position, "", 1, alphabet)
        for i in range(1000):
            play_one_game(root, alphabet, word_length)
        return root.get_best_move()



