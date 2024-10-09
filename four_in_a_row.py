"""Four-in-a-Row,
A two-player game where each player tries to get four pieces in a row."""

import sys

# Constants used for the game board display:
EMPTY_SPACE = "."  # Easier to count than spaces.
PLAYER_X = "X"
PLAYER_O = "O"

# Game board dimensions:
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# Template for displaying the game board:
BOARD_TEMPLATE = """
 1234567
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+"""

def main():
    """Plays one game of Four-in-a-Row."""
    print(
        """Four-in-a-Row,
A two-player game where each player drops pieces into a column. The goal is to line up four pieces in a row (horizontally, vertically, or diagonally).
"""
    )

    # Set up a new game:
    gameBoard = getNewBoard()  # Creates an empty board.
    playerTurn = PLAYER_X  # Player X starts first.

    while True:  # Loop to handle each player's turn.
        displayBoard(gameBoard)  # Show the current game board.
        playerMove = getPlayerMove(playerTurn, gameBoard)  # Get a valid move.
        gameBoard[playerMove] = playerTurn  # Place the player's tile.

        # Check for a winner or tie:
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # Show final board.
            print(f"Player {playerTurn} has won!")
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)  # Show final board.
            print("It's a tie!")
            sys.exit()

        # Switch to the other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        else:
            playerTurn = PLAYER_X

def getNewBoard():
    """Returns a dictionary representing the game board.
    Keys are tuples (columnIndex, rowIndex) and values are "X", "O", or "."."""
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

def displayBoard(board):
    """Displays the game board on the screen."""
    # Prepare the list to be passed to the format() method for BOARD_TEMPLATE.
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # Display the game board:
    print(BOARD_TEMPLATE.format(*tileChars))

def getPlayerMove(playerTile, board):
    """Asks the player to select a column to drop their piece.
    Returns a tuple (column, row) where the piece lands."""
    while True:  # Loop until a valid move is made.
        print(f"Player {playerTile}, enter 1 to {BOARD_WIDTH} or 'QUIT' to quit:")
        response = input("> ").upper().strip()  # Get and process player input.

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:  # Ensure a valid column number.
            print(f"Enter a number from 1 to {BOARD_WIDTH}.")
            continue

        columnIndex = int(response) - 1  # Convert to zero-based index.

        # Check if the column is full:
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("That column is full, choose another one.")
            continue

        # Find the lowest empty row in this column:
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)

def isFull(board):
    """Returns True if the board is full, otherwise False."""
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # Found an empty space, board is not full.
    return True  # No empty spaces, board is full.

def isWinner(playerTile, board):
    """Returns True if `playerTile` has four in a row, else False."""
    # Check all possible winning combinations on the board:
    # Check horizontal lines:
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            if (board[(columnIndex, rowIndex)] == playerTile and
                board[(columnIndex + 1, rowIndex)] == playerTile and
                board[(columnIndex + 2, rowIndex)] == playerTile and
                board[(columnIndex + 3, rowIndex)] == playerTile):
                return True

    # Check vertical lines:
    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            if (board[(columnIndex, rowIndex)] == playerTile and
                board[(columnIndex, rowIndex + 1)] == playerTile and
                board[(columnIndex, rowIndex + 2)] == playerTile and
                board[(columnIndex, rowIndex + 3)] == playerTile):
                return True

    # Check diagonal (bottom-left to top-right):
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            if (board[(columnIndex, rowIndex)] == playerTile and
                board[(columnIndex + 1, rowIndex + 1)] == playerTile and
                board[(columnIndex + 2, rowIndex + 2)] == playerTile and
                board[(columnIndex + 3, rowIndex + 3)] == playerTile):
                return True

    # Check diagonal (top-left to bottom-right):
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(3, BOARD_HEIGHT):
            if (board[(columnIndex, rowIndex)] == playerTile and
                board[(columnIndex + 1, rowIndex - 1)] == playerTile and
                board[(columnIndex + 2, rowIndex - 2)] == playerTile and
                board[(columnIndex + 3, rowIndex - 3)] == playerTile):
                return True

    return False

if __name__ == "__main__":
    main()
