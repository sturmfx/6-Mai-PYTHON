import random
def print_ruletka(numbers):
    for number in numbers:
        if number == "00":
            print(f"test")
        else:
            print(f"test2")

def spin_wheel():
    numbers = [str(i) for i in range(37)] +  ["00"]
    random.shuffle(numbers)
    return numbers

def bet(points):
    while True:
        bet = input("Enter your bet (0 - 36, or 00), RED or BLACK: ")
        if bet == "RED" or bet == "BLACK":
            return bet, points
        elif bet in [str(i) for i in range(37)]:
            while True:
                bet_

def play_game():
    print("Welcome to game!")

    while True:
        print("Spinning....")
        wheel = spin_wheel()
        bet1 = bet()
        winning_number = wheel[0]

        if bet1 == winning_number:
            print(f"You won! Winning number was {winning_number}")
        else:
            print(f"You lost! Winning number was {winning_number}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
    print("Thanks for playing!")

play_game()
