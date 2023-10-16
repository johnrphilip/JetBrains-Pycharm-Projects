class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def get_state(self):
        return (
            f"The coffee machine has:\n"
            f"{self.water} ml of water\n"
            f"{self.milk} ml of milk\n"
            f"{self.coffee_beans} g of coffee beans\n"
            f"{self.cups} disposable cups\n"
            f"${self.money} of money\n"
        )

    def check_resources(self, water, milk, beans, cost):
        if self.water - water < 0:
            return "Sorry, not enough water!"
        elif self.milk - milk < 0:
            return "Sorry, not enough milk!"
        elif self.coffee_beans - beans < 0:
            return "Sorry, not enough coffee beans!"
        elif self.cups - 1 < 0:
            return "Sorry, not enough cups!"
        else:
            self.water -= water
            self.milk -= milk
            self.coffee_beans -= beans
            self.cups -= 1
            self.money += cost
            return "I have enough resources, making you a coffee!"

    def buy_coffee(self, choice):
        coffees = {
            "1": {"water": 250, "milk": 0, "beans": 16, "cost": 4},
            "2": {"water": 350, "milk": 75, "beans": 20, "cost": 7},
            "3": {"water": 200, "milk": 100, "beans": 12, "cost": 6},
        }
        if choice in coffees:
            coffee = coffees[choice]
            return self.check_resources(
                coffee["water"], coffee["milk"], coffee["beans"], coffee["cost"]
            )

    def fill_machine(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.coffee_beans += beans
        self.cups += cups

    def take_money(self):
        taken_money = self.money
        self.money = 0
        return taken_money


def interact_with_machine(machine):
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
            if choice != "back":
                print(machine.buy_coffee(choice))
        elif action == "fill":
            water = int(input("Write how many ml of water you want to add: "))
            milk = int(input("Write how many ml of milk you want to add: "))
            beans = int(input("Write how many grams of coffee beans you want to add: "))
            cups = int(input("Write how many disposable cups you want to add: "))
            machine.fill_machine(water, milk, beans, cups)
        elif action == "take":
            print(f"I gave you ${machine.take_money()}")
        elif action == "remaining":
            print(machine.get_state())
        elif action == "exit":
            break


if __name__ == "__main__":
    machine_today = CoffeeMachine(400, 540, 120, 9, 550)
    interact_with_machine(machine_today)