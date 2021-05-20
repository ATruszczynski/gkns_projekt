import copy
import math


class Node:
    def __init__(self, word: [str], place: int, letter: str, player_type: int, alphabet: [str]):
        self.Plays = 0
        self.Score = 0
        self.Children = []
        self.Word = word
        self.Type = player_type
        if player_type == 1:
            self.UnusedMoves = copy.deepcopy(alphabet)
            self.Place = place
        if player_type == 2:
            self.UnusedMoves = list(range(len(word)))
            self.Letter = letter

    def get_not_used_move(self):
        if len(self.UnusedMoves) == 0:
            return -1
        return self.UnusedMoves.pop(0)

    def get_best_child(self):
        best_child = None
        for child in self.Children:
            if best_child is None:
                best_child = child
                continue
            if best_child.Plays == 0:
                best_child = child
                continue
            if child.Plays != 0:
                if self.get_uct_value(child) > self.get_uct_value(best_child):
                    best_child = child
        return best_child

    def get_uct_value(self, child):
        return child.Score / child.Plays + math.sqrt(2) * math.sqrt(math.log(self.Plays) / child.Plays)

    def update_score(self, score):
        self.Plays += 1
        self.Score += score

    def get_best_move(self):
        if self.Type == 2:
            return self.get_best_child().Place
        else:
            return self.get_best_child().Letter
