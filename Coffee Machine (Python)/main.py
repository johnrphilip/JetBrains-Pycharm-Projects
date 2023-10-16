class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def coffee_machine_state(self):
        print(f"""The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.coffee_beans} g of coffee beans
        {self.cups} disposable cups
        ${self.money} of money
        """)

    def check_espresso(self):
        if self.coffee_beans - 16 < 0:
            print("Sorry, not enough coffee beans!")
            self.coffee_action()
        elif self.water - 250 < 0:
            print("Sorry, not enough water!")
            self.coffee_action()
        elif self.cups - 1 < 0:
            print("Sorry, not enough cups!")
            self.coffee_action()

    def check_latte(self):
        if self.coffee_beans - 20 < 0:
            print("Sorry, not enough coffee beans!")
            self.coffee_action()
        elif self.water - 350 < 0:
            print("Sorry, not enough water!")
            self.coffee_action()
        elif self.cups - 1 < 0:
            print("Sorry, not enough cups!")
            self.coffee_action()
        elif self.milk - 75 < 0:
            print("Sorry, not enough milk!")
            self.coffee_action()

    def check_capp(self):
        if self.coffee_beans - 12 < 0:
            print("Sorry, not enough coffee beans!")
            self.coffee_action()
        elif self.water - 200 < 0:
            print("Sorry, not enough water!")
            self.coffee_action()
        elif self.cups - 1 < 0:
            print("Sorry, not enough cups!")
            self.coffee_action()
        elif self.milk - 100 < 0:
            print("Sorry, not enough milk!")
            self.coffee_action()
    def buy_coffee(self):
        drink_choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if drink_choice == "1":
            self.check_espresso()
            self.coffee_beans -= 16
            self.water -= 250
            self.money += 4
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
        elif drink_choice == '2':
            self.check_latte()
            self.coffee_beans -= 20
            self.water -= 350
            self.money += 7
            self.milk -= 75
            self.cups -= 1
            print("I have enough resources, making you a coffee!")
        elif drink_choice == '3':
            self.check_capp()
            self.coffee_beans -= 12
            self.water -= 200
            self.money += 6
            self.cups -= 1
            self.milk -= 100
            print("I have enough resources, making you a coffee!")
        self.coffee_action()


    def fill_machine(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:"))
        self.cups += int(input("Write how many disposable cups you want to add:"))
        self.coffee_action()

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        self.coffee_machine_state()

    def remaining(self):
        self.coffee_machine_state()
        self.coffee_action()


    def coffee_action(self):
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            self.buy_coffee()
            self.coffee_action()
        elif action == "fill":
            self.fill_machine()
            self.coffee_action()
        elif action == "take":
            self.take_money()
            self.coffee_action()
        elif action == "remaining":
            self.remaining()
            self.coffee_action()
        elif action == "exit":
            breakpoint()


machine_today = CoffeeMachine(400, 540, 120, 9, 550)
machine_today.coffee_action()