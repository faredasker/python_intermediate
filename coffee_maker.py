class CoffeeMaker:
    """ models the machine that make the coffee """
    def __int__(self):
        self.resources= {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """ print a report of all resources """
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}ml")
        print(f"coffees: {self.resources['coffee']}gm")

    def is_resource_sufficient(self,drink):
        """ return True when order can be made, False if no enough"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"sorry is not enough{item}.")
                can_make = False
        return can_make

    def make_coffee(self,order):
        """ deduct the required ingredients from resource"""
        for item in order.ingredients:
            self.resources[item]-= order.ingredients[item]
            print(f"here is your {order.name} enjoy")

