from players.player_moves_heuristic import PlayerMoveHeu
from players.player_utc import PlayerUCT
from utility import *
from utility2 import *

computer_player_list = [["Komputer losowy", PlayerRng], ["Komputer UCT", PlayerUCT],
                        ["Komputer heurystyka ilości ruchów", PlayerMoveHeu]
                        ]

pl_dict_gamemode = {"1": ["Człowiek", HumanPlayer]}
pl_dict_testmode = {}

i = 1
for pl in computer_player_list:
    pl_dict_gamemode[str(i+1)] = pl
    pl_dict_testmode[str(i)] = pl
    i = i + 1

del_dict = {"1": ["Nie", False],
            "2": ["Tak", True]}

base_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# base_alphabet = ['a', 'b', 'c']


class AtoGame:
    def __init__(self):
        # game parameters
        self.alph_count = -1
        self.word_length = -1
        self.p1 = None
        self.p2 = None
        self.alphabet = []

        # game variables
        self.log = []
        self.word = []
        self.winner = -1
        self.repetition = None

        # mode setter
        self.gamemode = True

        # gamemode parameters
        self.delay = -1
        self.separator = ""


    def set_testmode_parameters(self):
        self.gamemode = False
        self.set_game_parameters()
        self.set_players(pl_dict_testmode)
        pass

    def set_game_parameters(self):
        print("Wybierz liczność alfabetu")
        self.alph_count = pick_int(min=1)

        print("Wybierz długość słowa")
        self.word_length = pick_int(min=1)

        self.alphabet = generate_alphabet(self.alph_count, base_alphabet)

    def set_gamemode_parameters(self):
        self.gamemode = True
        self.set_game_parameters()
        self.set_players(pl_dict_gamemode)

        if not isinstance(self.p1, HumanPlayer) or not isinstance(self.p2, HumanPlayer):
            print("Wyamagać kliknięcia przed wykonaniem ruchu komputera?")
            self.delay = pick_option(del_dict)

        if self.alph_count > len(base_alphabet):
            self.separator = "|"
        else:
            self.separator = ""

    def set_players(self, pl_dict: dict):
        print("Wybierz gracza 1:")
        self.p1 = pick_option(pl_dict)()

        print("Wybierz gracza 2:")
        self.p2 = pick_option(pl_dict)()

    def print_parameters(self, end = "\n"):
        print(f"Parametry gry: \nLiczność alfabetu: {self.alph_count} | Maks. dł. słowa: {self.word_length} | \nGracz 1: {self.p1.to_string()} | Gracz 2: {self.p2.to_string()}", end=end)

    def play(self):
        self.word = []
        # self.move = 0
        self.log = []
        word_analisys = {}
        self.winner = -1

        while True:

            if self.gamemode:
                clear()
            if len(self.word) != 0:
                if self.gamemode:
                    print("Ruch gracza 1:")
                    if not isinstance(self.p1, HumanPlayer) and self.delay:
                        _ = input("(enter żeby gracz wykonał ruch)")

                move1 = self.p1.make_move_1(self.word, self.alphabet, word_analisys, self.separator, word_length=self.word_length)

                # if self.gamemode:
                #     print(ato_word_to_string(word=self.word, marker=move1, sep=self.separator))
            else:
                move1 = 0

            self.log.append(move1)

            if self.gamemode:
                clear()
                print("Ruch gracza 2:")
                if not isinstance(self.p2, HumanPlayer) and self.delay:
                    _ = input("(enter żeby gracz wykonał ruch)")

            move2 = self.p2.make_move_2(self.word, self.alphabet, position=move1, word_analisys=word_analisys, separator=self.separator, word_length=self.word_length)

            self.log.append(move2)
            self.word.insert(move1, move2)

            is_rep, self.repetition, word_analisys = analyse_word(self.word)

            if len(self.log) > 2 * self.word_length:
                ori = 1

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
        print(f"Kolejne ruchy: {flatten_list_of_strings(self.log, ',')}")
