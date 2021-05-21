from players.player_abs import PlayerAbs
from utility2 import analyse_word


class PlayerMoveHeu(PlayerAbs):
    def to_string(self):
        return "Gracz heur"

    def __build_rating_for_move1(self, word: [str], alphabet: [str]):
        move_rating = []
        for move1 in range(len(word) + 1):
            numer_of_possible_moves = 0
            for move2 in alphabet:
                new_word = word[:]
                new_word.insert(move1, move2)
                is_rep, _, _ = analyse_word(new_word)
                numer_of_possible_moves += is_rep
            move_rating.append(numer_of_possible_moves)
        return move_rating

    def make_move_1(self, word: [str], alphabet: [str], word_analisys: dict, separator: str, word_length: int):
        move_rating = self.__build_rating_for_move1(word, alphabet)
        best_move = move_rating.index(max(move_rating))
        return best_move

    def make_move_2(self, word: [str], alphabet: [str], position: int, word_analisys: dict, separator: str, word_length: int):
        best_move1_scores = []
        for move2 in alphabet:
            new_word = word[:]
            new_word.insert(position, move2)
            if analyse_word(new_word)[0]:
                best_move1_scores.append(float('inf'))
            else:
                best_move1_score = max(self.__build_rating_for_move1(new_word, alphabet))
                best_move1_scores.append(best_move1_score)
        best_move = best_move1_scores.index(min(best_move1_scores))
        return alphabet[best_move]
