class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {"quarter":0.25,
                   "dimes":0.10,
                   "nickles":0.05,
                   "pennies":0.01}

    def __int__(self):
        self.profit = 0
        self.money_received = 0

    def  report(self):
        """ print current profit"""
        print(f"money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """return total coins inserted"""
        print("please insert coins ")
        for coin in self.COIN_VALUES:
         self.money_received += int(input(f"how many {coin}?:  ")) * self.COIN_VALUES[coin]
         return self.money_received

    def make_payment(self,cost):
        """return true when payment accepted or false"""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost,2)
            print(f"here is {self.CURRENCY}{change} in change. ")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("sorry you dont have enough money")
            return False