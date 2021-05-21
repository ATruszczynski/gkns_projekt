from ato_tester import *
from utility import *
from players.player_human import *

desc = "description"
end_state = "end state"

# state = GAME_PREPARE

MAIN_MENU = "AAA"
GAME_PREPARE = "BBB"
GAME_READY = "fff"
TESTS_EMPTY = "CCC"
TESTS_ADD = "DDD"
# TESTS_ADD = "DASDA"
TESTS_LIST = "ggg"
TESTS_RUN = "EEE"
TESTS_DONE = "FFF"
TESTS_SAVE = "FADSFE"
EXIT = "GGG"

state = MAIN_MENU

random.seed(10011010)

while True:
    # wybór trybu obsługi
    if state == MAIN_MENU:
        clear()
        print("Wybierz tryb aplikacji:")
        odict = { "1": ["Tryb rozgrywki", GAME_PREPARE],
                  "2": ["Tryb testowy", TESTS_EMPTY],
                  "0": ["Zamknij aplikację", EXIT]}
        state = pick_option(odict)

    if state == GAME_PREPARE:
        clear()
        print("Wybierz ustawienia gry")
        print(long_sep)
        ato = AtoGame()
        ato.set_gamemode_parameters()
        clear()
        ato.print_parameters()
        print(short_sep)

        odict = { "1": ["Zatwierdź ustawienia i graj", GAME_READY],
                  "2": ["Zmień ustawienia gry", GAME_PREPARE],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        print("Czy gra jest gotowa?")
        state = pick_option(odict)

    if state == GAME_READY:
        ato.play()
        clear()
        ato.print_result()
        print(short_sep)

        odict = { "1": ["Zagraj jeszcze raz", GAME_READY],
                  "2": ["Zmień ustawienia gry", GAME_PREPARE],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        state = pick_option(odict)

    if state == TESTS_EMPTY:
        clear()
        tester = AtoTester()

        odict = { "1": ["Dodaj nastepny test", TESTS_ADD],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        state = pick_option(odict)

    if state == TESTS_ADD:
        clear()
        tester.add_test()
        clear()

        odict = { "1": ["Dodaj nastepny test", TESTS_ADD],
                  "2": ["Zresetuj listę testów", TESTS_EMPTY],
                  "3": ["Wykonaj testy", TESTS_RUN],
                  "4": ["Pokaż listę testów", TESTS_LIST],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        state = pick_option(odict)

    if state == TESTS_LIST:
        clear()
        tester.print_parameters()

        odict = { "1": ["Dodaj nastepny test", TESTS_ADD],
                  "2": ["Zresetuj listę testów", TESTS_EMPTY],
                  "3": ["Wykonaj testy", TESTS_RUN],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        state = pick_option(odict)

    if state == TESTS_RUN:
        clear()
        tester.run()
        clear()
        tester.print_results()
        tester.save_results(history=True)

        odict = { "1": ["Przeprowadź testy jeszcze raz", TESTS_RUN],
                  "2": ["Przeprowadź nowe testy", TESTS_EMPTY],
                  # "3": ["Zapisz wyniki", TESTS_SAVE],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        state = pick_option(odict)

    if state == TESTS_SAVE:
        clear()
        print("Jak chcesz zapisać testy?")
        choice_dict = { "1": ["Zapisz parametry i wyniki gier testowych", False],
                        "2": ["Zapisz parametry, wyniki i historie gier testowych", True]}

        choice = pick_option(choice_dict)


        odict = { "1": ["Przeprowadź testy jeszcze raz", TESTS_RUN],
                  "2": ["Przeprowadź nowe testy", TESTS_EMPTY],
                  "9": ["Zmień tryb aplikacji", MAIN_MENU],
                  "0": ["Wyjdź z aplikacji", EXIT]}
        state = pick_option(odict)

    if state == EXIT:
        break

desc = "description"
end_state = "end state"


