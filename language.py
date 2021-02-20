class Language:
    def __init__(self, player_language):
        self.language = player_language

        while True:
            if not self.language == 'en' or not self.language == 'de':
                self.language = input('No available language! / Keine moegliche Sprache! Try again / Versuche erneut')
                continue
            break

        if self.language == 'en' or self.language == 'de':
            pass

        else:
            exit('pls report: if not doesn\'t work (Language.py > class Language > def __init__() / > while True > if)')

    def text(self):
        if self.language == 'en':
            pass
        elif self.language == 'de':
            pass
        else:
            exit('pls report: error (language.py > class Language > def text() > else:)')