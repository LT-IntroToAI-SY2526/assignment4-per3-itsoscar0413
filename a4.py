# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __init__(self):
        self.board = 9 * ["*"]

    def __str__(self):
        board_str = ""
        for i in range(0, 9, 3): #chatgpt helped with this. it starts at 0 and goes to 9 (like the 9 items in the list), and breaks it into 3
            board_str += f"{self.board[i]} {self.board[i+1]} {self.board[i+2]}\n"
        return board_str

    def make_move(self, player, pos):
        # This checks if the spot is invalid or full, and if it is, it returns false
        if pos < 0 or pos > 8:
            return False
        if self.board[pos] != "*":
            return False
    
        # If the move was made successfully, it returns true and makes the move
        self.board[pos] = player
        return True

    def has_won(self, player):
        #the stuff below is what counts as a win
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], #rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], #column
            [0, 4, 8], [2, 4, 6] #diagnol
        ]
        for order in wins:
            if all(self.board[i] == player for i in order):
                return True
        return False
    
    def game_over(self):
        # it returns true if someone won (with 'x' or 'o'), or if the board is full and doesn't have any '*' left, returns true
        if self.has_won("X") or self.has_won("O"):
            return True
        if "*" not in self.board:
            return True
        # if none of that falls into this, it returns false and game keeps going
        return False

    def clear(self):
        # clears the board, reused code from __init__
        self.board = 9 * ["*"]

def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    "Additional assert below"
    brd.clear()
    brd.make_move("X", 0)
    brd.make_move("X", 3)
    brd.make_move("X", 6)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True


    print("All tests passed!")

    # uncomment to play!
    # play_tic_tac_toe()
