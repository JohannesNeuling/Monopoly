from classes import MainHouse, MainMachines, MainPlayer


class Houses:
    def __init__(self):
        self.card = ["Deutschland", "Norwegen", "Polen", "Niederlande", "Frankreich"]  # 0 - 4
        self.deutschland = MainHouse(place=self.card[0], price=1000, round_money=500, name="Deutschland")
        self.norwegen = MainHouse(place=self.card[1], price=750, round_money=375, name="Norwegen")
        self.polen = MainHouse(place=self.card[2], price=600, round_money=300, name="Polen")
        self.niederlande = MainHouse(place=self.card[3], price=500, round_money=250, name="Niederlande")
        self.frankreich = MainHouse(place=self.card[4], price=250, round_money=125, name="Frankreich")

        """self.price_deutschland = 1000 self.round_value_deutschland = 500 self.name_deutschland = 'Deutschland' 
        self.deutschland = MainHouse(place=self.card[0], price=self.price_deutschland, 
        round_money=self.round_value_deutschland, name=self.name_deutschland) 
        

        self.price_norwegen = 750 self.round_value_norwegen = 375 self.name_norwegen = 'Norwegen' self.norwegen = 
        MainHouse(place=self.card[1], price=self.price_norwegen, round_money=self.round_value_norwegen, 
        name=self.name_norwegen) 

        self.price_polen = 600 self.round_value_polen = 300 self.name_polen = 'Polen' self.polen = MainHouse(
        place=self.card[2], price=self.price_polen, round_money=self.round_value_polen, name=self.name_polen) 

        self.price_niederlande = 500 self.round_value_niederlande = 250 self.name_niederlande = 'Niederlande' 
        self.niederlande = MainHouse(place=self.card[3], price=self.price_niederlande, 
        round_money=self.round_value_niederlande, name=self.name_niederlande) 

        self.price_frankreich = 250 self.round_value_frankreich = 125 self.name_frankreich = 'Frankreich' 
        self.frankreich = MainHouse(place=self.card[4], price=self.price_frankreich, 
        round_money=self.round_value_frankreich, name=self.name_frankreich) """


class Player:
    def __init__(self):
        self.gehalt = input('Mit wie viel Gehalt wollt ihr starten? Richtwert 1000: ')
        self.name1 = input('Wie soll der erste Spieler heißen?')
        self.player1 = MainPlayer(gehalt=self.gehalt, name=self.name1)
        self.name2 = input('Wie soll der zweite Spieler heißen?')
        self.player2 = MainPlayer(gehalt=self.gehalt, name=self.name2)
    def return_players(self):
        return self.player1, self.player2
