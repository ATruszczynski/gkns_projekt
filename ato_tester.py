from ato_game import *
import os
import datetime

test_dir = "tests"

class AtoTester:
    def __init__(self):
        self.tests = []
        self.test_records = []

    def add_test(self):
        print("Dodawanie testu")
        print(short_sep)
        game = AtoGame()
        game.set_testmode_parameters()
        print("Określ liczbę testów")
        count = pick_int(1)

        self.tests.append((game, count))

    def set_parameters(self):
        print("Tester sets parameters")

    def print_parameters(self):
        clear()
        print("Lista testów:")
        print(long_sep)

        for t in self.tests:
            t[0].print_parameters(end=". ")
            print(f"Powtórzenia: {t[1]}")
            print(short_sep)

    def run(self):
        self.test_records = []

        for t in self.tests:
            reps = t[1]
            for r in range(reps):
                game = t[0]
                game.play()
                record = [game.p1.to_string(), game.p2.to_string(), game.alph_count, game.word_length, len(game.log), game.winner, ato_word_to_string(game.word, sep="|"), flatten_list_of_strings(game.log, separator="|")]
                self.test_records.append(record)

    def print_results(self):
        for tr in self.test_records:
            print(tr)

    def save_results(self, history: bool = False):
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)

        now = datetime.datetime.now()
        file = open(f"{test_dir}{os.path.sep}tests_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.csv", "w")


        file.write("player_1,player_2,alph_count,word_len,game_len,winner")
        if history:
            file.write(",final_word,log")
        file.write("\n")
        for tr in self.test_records:
            file.write(f"{tr[0]},{tr[1]},{tr[2]},{tr[3]},{tr[4]},{tr[5]}")
            file.write(f",{tr[6]},{tr[7]}")
            file.write("\n")