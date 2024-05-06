
from random import*

class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = None
    def choose_symbol(self):
        while True:
            try:
                symbol = int(input(f"{self.name}, choose a symbol [1: X, 2: O]: "))
            except ValueError:
                print("Invalid value. Try again.")
                continue
            if symbol == 1:
                self.symbol = "X"
                break
            elif symbol == 2:
                self.symbol = "O"
                break
            else:
                print("Invalid number. Try again.")

    def choose_coordinate(self):
        while True:
            try:
                coordinate = int(input("Enter coordinate: "))
            except ValueError:
                print("Invalid value. Try again.")
                continue
            if coordinate in range(1, 10):
                return coordinate
            else:
                print("Invalid coordinate. Try again.")

    @staticmethod
    def validate_name(name):
        return name.isalpha()  # Returns True if the name contains only letters

class Computer():
    def __init__(self , opponent):
        self.opponent = opponent
    def choose_opponent( opponent):
        while True:
            try:
                opponent = int(input("[Player : 1 or computer : 2] :  "))
                
            except:
                print("only numbers allowed. Try again")
                continue
            if opponent == 1: # player
                return True
            else:
                return False # computer
    def Random_coordinate(self):
                    coordinate = int(uniform(1,9))
                    return coordinate
            


class Board:
    def __init__(self):
        self.cells = [str(_) for _ in range(1, 10)]
    
    def display(self):
        
        for i in range(0, 9, 3):
            print(" | ".join(self.cells[i:i + 3]))
            
            if i < 6:
                print("-" * 9)
            else:
                print("\n")

    def update(self, coordinate, symbol , name):
        if self.cells[coordinate - 1] in ['X', 'O']:
            if name == "Computer":
                return False
            else:
                print("This position is already taken. Please choose another coordinate.")
                return False
        else:
            self.cells[coordinate - 1] = symbol
            return True


class Result:
    @staticmethod
    def check_win(board, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            if board.cells[condition[0]] == board.cells[condition[1]] == board.cells[condition[2]] == player.symbol:
                return True
        return False

    @staticmethod
    def check_draw(board):
        return all(cell in ['X', 'O'] for cell in board)


# Main game loop
def play_again():
    while True:
        try:
            play = int(input("[1 :play or 2:quit] : "))
        except:
            print("numbers only allowed.Try again")
            continue
        if play == 2:
            return False
        elif play == 1:
            return True
        else:
            print("invalid number. Try again")
            return play_again()
def main():
    while play_again():
        if Computer.choose_opponent(""):
            player1_name = input("Enter Player 1's name: ")
            while not Player.validate_name(player1_name):
                print("Name must contain letters only.")
                player1_name = input("Enter Player 1's name: ")
            player1 = Player(player1_name)
            player1.choose_symbol()

            player2_name = input("Enter Player 2's name: ")
            while not Player.validate_name(player2_name):
                print("Name must contain letters only.")
                player2_name = input("Enter Player 2's name: ")
            player2 = Player(player2_name)
            if player1.symbol == "X":
                player2.symbol = "O"
            else:
                player2.symbol = "X"

            board = Board()
            board.display()

            while True:
                coordinate = player1.choose_coordinate()
                while not board.update(coordinate, player1.symbol , player2_name):
                    coordinate = player1.choose_coordinate()
                board.display()
                if Result.check_win(board, player1):
                    print(f"{player1.name} wins!")
                    break
                elif Result.check_draw(board.cells):
                    print("It is a draw")
                    break

                coordinate = player2.choose_coordinate()
                while not board.update(coordinate, player2.symbol):
                    coordinate = player2.choose_coordinate
                board.display()
                if Result.check_win(board, player2):
                    print(f"{player2.name} wins!")
                    break
                elif Result.check_draw(board.cells):
                    print("It is a draw")
                    break
        else:
            player1_name = input("Enter Player 1's name: ")
            while not Player.validate_name(player1_name):
                print("Name must contain letters only.")
                player1_name = input("Enter Player 1's name: ")
            player1 = Player(player1_name)
            player1.choose_symbol()
            player2 = Player("Computer")
            if player1.symbol == "X":
                player2.symbol = "O"
            else:
                player2.symbol = "X"
            board = Board()
            board.display()

            while True:

                coordinate = player1.choose_coordinate()
                while not board.update(coordinate, player1.symbol , player1_name):
                    coordinate = player1.choose_coordinate()
                board.display()
                if Result.check_win(board, player1):
                    print(f"{player1.name} wins!")
                    break
                elif Result.check_draw(board.cells):
                    print("It is a draw")
                    break

                #computer's coordinates
                coordinate =Computer.Random_coordinate("")
                while not board.update(coordinate, player2.symbol , player2.name):
                    coordinate = Computer.Random_coordinate("")
                board.display()
                if Result.check_win(board, player2):
                    print(f"{player2.name} wins!")
                    break
                elif Result.check_draw(board.cells):
                    print("It is a draw")
                    break



if __name__ == "__main__":
    
    main()

