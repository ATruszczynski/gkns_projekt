from utility import *
from utility2 import *
from collections import deque

pl_dict = { "1": ["Człowiek", HumanPlayer],
            "2": ["Komputer losowy", PlayerRng]}

del_dict = {"1": ["Nie", False],
            "2": ["Tak", True]}

base_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class AtoGame:
    def set_parameters(self):
        print("Wybierz liczność alfabetu")
        self.alph_count = pick_int(min=1)

        print("Wybierz długość słowa")
        self.word_length = pick_int(min=1)

        print("Wybierz gracza 1:")
        self.p1 = pick_option(pl_dict)()

        print("Wybierz gracza 2:")
        self.p2 = pick_option(pl_dict)()

        if not isinstance(self.p1, HumanPlayer) or not isinstance(self.p2, HumanPlayer):
            print("Wyamagać kliknięcia przed wykonaniem ruchu komputera?")
            self.delay = pick_option(del_dict)

        # self.alph_count = 5
        # self.word_length = 8
        # self.p1 = HumanPlayer()
        # self.p2 = HumanPlayer()
        # self.delay = False

        if self.alph_count > len(base_alphabet):
            self.separator = "|"
        else:
            self.separator = ""
        self.alphabet = generate_alphabet(self.alph_count, base_alphabet)

    def print_parameters(self):
        print(f"Parametry gry: \nLiczność alfabetu: {self.alph_count} | Maks. dł. słowa: {self.word_length} | \nGracz 1: {self.p1.to_string()} | Gracz 2: {self.p2.to_string()}")

    def play(self):
        self.word = []
        self.move = 0
        self.log = "|"
        word_analisys = {}
        self.winner = -1

        while True:
            clear()
            if len(self.word) != 0:
                print("Ruch gracza 1:")
                if not isinstance(self.p1, HumanPlayer) and self.delay:
                    _ = input("(enter żeby gracz wykonał ruch)")

                move1 = self.p1.make_move_1(self.word, self.alphabet, word_analisys, self.separator)
                self.log += f"{move1}|"

                print(ato_word_to_string(word=self.word, marker=move1, sep=self.separator))
            else:
                move1 = 0

            clear()
            print("Ruch gracza 2:")
            if not isinstance(self.p2, HumanPlayer) and self.delay:
                _ = input("(enter żeby gracz wykonał ruch)")

            move2 = self.p2.make_move_2(self.word, self.alphabet, position=move1, word_analisys=word_analisys, separator=self.separator)
            self.log += f"{move2}|"
            self.word.insert(move1, move2)

            is_rep, self.repetition, word_analisys = analyse_word(self.word)

            if is_rep:
                self.winner = 1
                break
            elif len(self.word) == self.word_length:
                self.winner = 2
                break

    def print_result(self):
        if self.winner == 1:
            print(f"Gracz 1 wygrywa. W słowie '{ato_word_to_string(self.word, sep=self.separator)}' na miejscu {self.repetition[0]} jest powtórzenie w promieniu {self.repetition[1]}.")
        else:
            print(f"Gracz 2 wygrywa. Słowo '{ato_word_to_string(self.word, sep=self.separator)}' ma długość {self.word_length} i nie zawiera powtórzeń.")

        print(short_sep)
        print(f"Kolejne ruchy: {self.log}")
