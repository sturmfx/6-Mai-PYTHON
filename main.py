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
                bet_amount = input("ENTER YOUR BET: ")
                try:
                    bet_amount = int(bet_amount)
                    if bet_amount <= points and bet_amount > 0:
                        return bet, bet_amount
                    else:
                        print("Invalid input or insufficient points.")
                except ValueError:
                    print("FIGNJA")
        else:
            print("Invalid input")
def play_game():
    print("Welcome to game!")
    point_bank = 100
    while True:
        print(f"You have {point_bank} points.")
        print("Spinning....")
        wheel = spin_wheel()
        bet_num, bet_amount = bet(point_bank)
        winning_number = wheel[0]

        if bet_num == "RED" and winning_number in ["2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36"]:
            print(f"You won {bet_amount * 2}! Winning number was {winning_number} (color was RED)")
            point_bank = point_bank + bet_amount
        elif bet_num == "BLACK" and winning_number in ["1","3","5","7","9","11","13","15","17","19","21","23","25","27","29","31","33","35","37"]:
            print(f"You won {bet_amount * 2}! Winning number was {winning_number} (color was BLACK)")
            point_bank = point_bank + bet_amount
        elif bet_num == winning_number:
            
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break
    print("Thanks for playing!")

play_game()
