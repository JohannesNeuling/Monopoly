class MainHouse:
    def __init__(self, place, price, round_money, name):  # maschinen des hauses
        self.name = name
        self.price = price
        self.place = place
        self.buy = False
        self.machines = []  # max 5 bzw. 4
        self.round_money = round_money

class MainMachines:
    def __init__(self, price, house, house_machines, money_multiplicator):
        self.price = price
        self.house = house
        # self.house_machines = house_machines
        self.money_multiplicator = money_multiplicator

class MainPlayer:
    def __init__(self, gehalt, name):
        self.gehalt = gehalt
        self.houses_name = []
        self.houses_as_object = []
        self.machines = []
        self.name = name
