from player_abs import *
from utility2 import *

class HumanPlayer(PlayerAbs):

    def to_string(self):
        return "Gracz człowiek"

    def make_move_1(self, word: [str], alphabet: [str], word_analisys: dict, separator: str):
        position = 0
        print("Aktualne słowo: " + ato_word_to_string(word, sep=separator))
        print(f"Wybierz pozycję ({0}-{len(word)}):")
        pos = pick_int(0, len(word) + 1)

        return pos

    def make_move_2(self, word: [str], alphabet: [str], position:int, word_analisys: dict, separator: str):
        print("Aktualne słowo: " + ato_word_to_string(word, marker=position, sep=separator))

        while True:
            # TODO Tu jakiś flatten może by się nadał (trzeba zmienić tak czy siak)
            print(f"Wybierz literę ({ato_word_to_string(alphabet, sep='|')}):")
            letter = input()

            if letter in alphabet:
                break
            else:
                print("Nie ma takiego znaku w alfabecie")

        return letter
