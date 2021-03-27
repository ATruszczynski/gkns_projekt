from ato_game import *
from ato_tester import *
from utility import *
from player_human import *

state = ""
desc = "description"
end_state = "end state"

# state = "G"

while True:
    # wybór trybu obsługi
    if state == "":
        clear()
        print("Wybierz tryb aplikacji:")
        odict = { "1": ["Tryb rozgrywki", "G"],
                  "2": ["Tryb testowy", "T"],
                  "0": ["Zamknij aplikację", "E"]}
        state = pick_option(odict)

    if state == "G":
        clear()
        print("Wybierz ustawienia gry")
        print(long_sep)
        ato = AtoGame()
        ato.set_parameters()
        clear()
        ato.print_parameters()
        print(short_sep)

        odict = { "1": ["Zatwierdź ustawienia i graj", "GR"],
                  "2": ["Zmień ustawienia gry", "G"]}
        print("Czy gra jest gotowa?")
        state = pick_option(odict)

    if state == "GR":
        ato.play()
        clear()
        ato.print_result()
        print(short_sep)

        odict = { "1": ["Zagraj jeszcze raz", "GR"],
                  "2": ["Zmień ustawienia gry", "G"],
                  "3": ["Zmień tryb aplikacji", ""],
                  "0": ["Wyjdź z aplikacji", "E"]}
        state = pick_option(odict)

    if state == "T":
        print("¯\_(ツ)_/¯ not here yet ¯\_(ツ)_/¯")
        _ = input("Click enter to continue")
        state = ""
        # tester = AtoTester()
        # tester.set_parameters()
        #
        # state += "R"

    # if state == "TR":
        # tester.run()
        # tester.print_results()
        #
        # odict = { "1": ["Powtórz testy", "TR"],
        #           "2": ["Zmień parametry testów", "T"],
        #           "3": ["Zmień tryb aplikacji", ""],
        #           "0": ["Wyjdź z aplikacji", "E"]}
        # state = pick_option(odict)

    if state == "E":
        break

desc = "description"
end_state = "end state"


