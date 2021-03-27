from ato_game import *
from ato_tester import *
from utility import *
from player_human import *

state = ""
desc = "description"
end_state = "end state"

state = "G"

while True:
    # wybór trybu obsługi
    if state == "":
        odict = { "1": ["Tryb rozgrywki", "G"],
                  "2": ["Tryb testowy", "T"],
                  "0": ["Zamknij aplikację", "E"]}
        state = pick_option(odict)

    if state == "G":
        ato = AtoGame()
        ato.set_parameters()
        ato.print_parameters()

        print("Kliknij enter, aby rozpocząć grę")
        _ = input()

        state += "R"

    if state == "GR":
        ato.play()
        ato.print_result()

        odict = { "1": ["Zagraj jeszcze raz", "GR"],
                  "2": ["Zmień ustawienia gry", "G"],
                  "3": ["Zmień tryb aplikacji", ""],
                  "0": ["Wyjdź z aplikacji", "E"]}
        state = pick_option(odict)

    if state == "T":
        tester = AtoTester()
        tester.set_parameters()

        state += "R"

    if state == "TR":
        tester.run()
        tester.print_results()

        odict = { "1": ["Powtórz testy", "TR"],
                  "2": ["Zmień parametry testów", "T"],
                  "3": ["Zmień tryb aplikacji", ""],
                  "0": ["Wyjdź z aplikacji", "E"]}
        state = pick_option(odict)

    if state == "E":
        break

desc = "description"
end_state = "end state"


