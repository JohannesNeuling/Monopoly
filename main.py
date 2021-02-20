import variabels
from classes import MainPlayer
import language


class Game:
    def __init__(self):
        ### inputs ###
        self.give_player = variabels.Player()
        self.player1, self.player2 = self.give_player.return_players()
        print(self.player1, '+', self.player2)

    def game(self):
        pass


class Main:
    def __init__(self):
        self.players_language = None
        while True:
            language_input = input("Wich language do you speek?\n"
                                   "Welche Sprache sprichst du?\n"
                                   "type: \"english\" or \"german\"\n"
                                   "tippe \"englisch\" oder \"deutsch\":\n")
            if language_input == "english" or language_input == "enlisch":
                self.players_language = 'en'
            elif language_input == "german" or language_input == "deutsch":
                self.players_language = "de"
            else:
                continue
            break
        if self.players_language is None:  # == or is ?
            exit('pls report: "language still None (main.py > Class Main > def  __init__ > self.players_language)"')
        print_language = language.Language(self.players_language)

        self.written = Written()
        self.game = Game()
        while True:
            self.start_way = input(
                "Was moechtest du als erstes machen? Gleich das Game starten [1], dir die Anleitung durchlesen [2]"
                "oder Informationen ueber das Spiel erhalten [3]?")
            if self.start_way == '1':
                self.game.game()
            elif self.start_way == '2':
                self.written.anleitung()
            elif self.start_way == '3':
                self.written.info()
            else:
                continue
            break





class Written:
    def __init__(self):
        pass

    def info(self):
        print(
            "Hallo, ich bin Johannes Neuling und dies ist Monopoly. Die Idee dieses Spiels ist in meiner Schule "
            "enstanden. Bis jetzt ist dieses Spiel nur auf Deutsch verfuegbar")

    def anleitung(self):
        print('')


if __name__ == "__main__":
    Game()
    # Main()
