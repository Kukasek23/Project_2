import sys
from colorama import Fore


"""
projekt_2.py: Druhý projekt python SPŠD Motol
author: Lukáš Jan Bylok 3.A 2024
email: lukas.bylok@gmail.com
"""

separator_2 = "-" * 110
separator = "=" * 110

sign_Dictionary = [' '] * 9

player_A = input("Enter the name of the player A: ")
player_B = input("Enter the name of the player B: ")

print(separator)
print(f"Welcome to the Tic Tac Toe: {player_A}; {player_B}")
print(separator)

print("GAME RULES:")
print("1. Each player can place one mark (or stone) per turn on the 3x3 grid.")
print("2. The WINNER is the player who succeeds in placing three of their marks in a:")
print(Fore.RED + "   * horizontal")
print(Fore.RED + "   * vertical")
print(Fore.RED + "   * or diagonal row")
print(Fore.WHITE + separator)

print(Fore.YELLOW + "Let's start the game...")
print(Fore.WHITE + separator_2)

print(Fore.CYAN + "Generating the board... You will choose a number between 1 - 9 to select your position")
print("""
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
""")

print(Fore.WHITE + f"{player_A}'s sign will be - X")
print(f"{player_B}'s sign will be - O")
input("Press any key to start the game: ")
print(separator)



def print_Board():
    Board = f"""
  +---+---+---+
  | {sign_Dictionary[0]} | {sign_Dictionary[1]} | {sign_Dictionary[2]} |
  +---+---+---+
  | {sign_Dictionary[3]} | {sign_Dictionary[4]} | {sign_Dictionary[5]} |
  +---+---+---+
  | {sign_Dictionary[6]} | {sign_Dictionary[7]} | {sign_Dictionary[8]} |
  +---+---+---+
  """
    print(Board)

index_List = []

def take_Input(player_name):
    while True:
        X = int(input(f"{player_name}, enter your position (1 - 9): "))
        X -= 1
        if 0 <= X < 9:
            if X in index_List:
                print("This spot is blocked...")
                continue
            index_List.append(X)
            return X
        else:
          print("Wrong number... Try Again.")


def check_winner(sign):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    for combo in winning_combinations:
        if sign_Dictionary[combo[0]] == sign_Dictionary[combo[1]] == sign_Dictionary[combo[2]] == sign:
            return True
    return False


for letter in range(9):
    if letter % 2 == 0:
        index = take_Input(player_A)
        sign_Dictionary[index] = "X"
        print_Board()
        if check_winner("X"):
            print(f"Congratulations {player_A} WON!!!")
            sys.exit("Thank you for playing...")

    else:
        index = take_Input(player_B)
        sign_Dictionary[index] = "O"
        print_Board()
        if check_winner("O"):
            print(FORE.YELLOW + f"Congratulations {player_B} WON!!!")
            sys.exit(FORE.WHITE + "Thank you for playing...")

print(FORE.RED + "This is a TIE; Nobody Won... Play Again")
