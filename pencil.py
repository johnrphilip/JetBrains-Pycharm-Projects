import random

def bot_move(pencils_on_table):
    if pencils_on_table in [5,9,13,17]:
        return random.randint(1, 3)
    elif pencils_on_table == 1:
        return 1
    elif pencils_on_table % 4 == 0:
        return 3
    elif pencils_on_table % 4 == 3:
        return 2
    elif pencils_on_table % 4 == 2:
        return 1
    else:
        return random.randint(1, 3)

def play_turn(player):
    print('|' * pencil_number)
    if player == "John":
        while True:
            try:
                move = int(input(f"{player}'s turn!"))
                if move in [1,2,3] and move <= pencil_number:
                    return move
            except ValueError:
                pass
            print("Possible values: '1', '2', '3'")
            if move > pencil_number:
                print("Too many pencils")
    else:
        move = bot_move(pencil_number)
        print(f"{player}'s turn:\n{move}")
        return move


def start():
    global pencil_number

    # Set up the number of pencils with input validation
    while True:
        try:
            pencil_number = int(input("How many pencils would you like to use:"))
            if pencil_number <= 0:
                raise ValueError("The number of pencils should be positive.")
            break
        except ValueError as e:
            if str(e) == "The number of pencils should be positive.":
                print(e)
            else:
                print("The number of pencils should be numeric.")

    # Determine the playing order
    while True:
        first_player = input("Who will be the first (John, Jack):")
        if first_player == "John":
            second_player = "Jack"
            break
        elif first_player == "Jack":
            second_player = "John"
            break
        else:
            print("Choose between 'John' and 'Jack'")
            continue

    # Game loop
    current_player = first_player
    while pencil_number > 0:
        move = play_turn(current_player)
        pencil_number -= move

        if pencil_number <= 0:
            print(f"{second_player if current_player == first_player else first_player} won!")
            return

        current_player, second_player = second_player, current_player

if __name__ == "__main__":
    start()
