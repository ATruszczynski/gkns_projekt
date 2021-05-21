from ato_game import *
import os
import datetime

test_dir = "tests"

class AtoTester:
    def __init__(self):
        self.tests = []
        self.test_records = []
        self.summary_record = []

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
            t[0].print_parameters(end=" | ")
            print(f"Powtórzenia: {t[1]}")
            print(short_sep)

    def run(self):
        self.test_records = []

        for t in self.tests:
            game = t[0]
            reps = t[1]

            p1_winrate = 0
            av_game_len = 0

            for r in range(reps):
                game.play()
                if game.winner == 1:
                    p1_winrate += 1
                av_game_len += len(game.log)
                record = [game.p1.to_string(), game.p2.to_string(), game.alph_count, game.word_length, len(game.log), game.winner, ato_word_to_string(game.word, sep="|"), flatten_list_of_strings(game.log, separator="|")]
                self.test_records.append(record)

            p1_winrate = round(p1_winrate / reps)
            p2_winrate = 1 - p1_winrate
            av_game_len = round(av_game_len / reps, 2)

            self.summary_record.append([game.p1.to_string(), game.p2.to_string(), game.alph_count, game.word_length, p1_winrate, p2_winrate, av_game_len])

    def print_results(self):
        for tr in self.test_records:
            print(tr)

    def save_results(self, history: bool = False):
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)

        now = datetime.datetime.now()

        dir = f"{test_dir}{os.path.sep}"
        suff = f"tests_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.csv"

        res_file_name = f"{dir}{suff}"
        summary_file_names = f"{dir}/summary_{suff}"
        file = open(res_file_name, "w")
        sum_file = open(summary_file_names, "w")


        history = True #TODO remove
        # TODO tego się chyba nie da wywołać z history = TRUE
        file.write("player_1,player_2,alph_count,word_len,game_len,winner")
        sum_file.write("player_1,player_2,alph_count,word_len,p1_winrate,p2_winrate,av_game_len\n")
        if history:
            file.write(",final_word,log")
        file.write("\n")
        for tr in self.test_records:
            file.write(f"{tr[0]},{tr[1]},{tr[2]},{tr[3]},{tr[4]},{tr[5]}")
            if history:
                file.write(f",{tr[6]},{tr[7]}")
            file.write("\n")

        for sr in self.summary_record:
            sum_file.write(f"{sr[0]},{sr[1]},{sr[2]},{sr[3]},{sr[4]},{sr[5]},{sr[6]}\n")
