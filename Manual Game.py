import random
import time

# Function to print the Sudoku board with 3x3 borders
def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Horizontal border
        row_str = ""
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "  # Vertical border
            row_str += (str(num) if num != 0 else ".") + " "
        print(row_str)

# Function to check if a number is valid in a given position
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

# Backtracking solver
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Generate a random Sudoku puzzle
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for _ in range(random.randint(12, 20)):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        board[row][col] = num
    return board

# Check the board and remove incorrect entries
def check_board(board, original_board):
    incorrect_positions = []
    for row in range(9):
        for col in range(9):
            if original_board[row][col] == 0 and board[row][col] != 0:
                if not is_valid(board, row, col, board[row][col]):
                    incorrect_positions.append((row + 1, col + 1))
                    board[row][col] = 0
    if incorrect_positions:
        print("\nIncorrect entries found and removed at the following positions:")
        for position in incorrect_positions:
            print(f"Row {position[0]}, Column {position[1]}")
    else:
        print("\nAll entries are correct!")

# Finish the puzzle by first checking and then solving
def finish_puzzle(board, original_board):
    print("\nChecking the current board...")
    time.sleep(2)
    check_board(board, original_board)

    print("\nSolving the puzzle...")
    time.sleep(2)

    solve_sudoku(board)

    print("\nThe puzzle has been completed!")
    time.sleep(2)

    print("\nHere is the completed puzzle:\n")
    time.sleep(2)
    print_board(board)

    print("\nThank you for playing! Goodbye!")
    time.sleep(2)
    exit()

# Allow the user to solve the puzzle
def user_solve_sudoku(board):
    original_board = [row[:] for row in board]
    first_time = True
    while True:
        if not first_time:
            print("\nCurrent Board:")
            time.sleep(2)
            print_board(board)
        first_time = False
        try:
            time.sleep(2)
            print("\nChoose one of the following options:")
            time.sleep(1)
            print("1. Enter your move in the format 'row col num'.")
            time.sleep(1)
            print("2. Type 'check' to validate your board.")
            time.sleep(1)
            print("3. Type 'finish' to automatically complete the puzzle.")
            time.sleep(1)
            print("4. Type 'quit' to exit.")
            time.sleep(1)
            print()
            user_input = input("Your choice: ").strip().lower()
            if user_input == "quit":
                print("\nExiting. Goodbye!")
                time.sleep(2)
                break
            elif user_input == "check":
                print("\nChecking the current board...")
                time.sleep(2)
                check_board(board, original_board)
                continue
            elif user_input == "finish":
                finish_puzzle(board, original_board)
                break
            row, col, num = map(int, user_input.split())
            row, col = row - 1, col - 1
            if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
                print("\nInvalid input. Please enter row, column, and number in range.")
                time.sleep(2)
                continue
            if original_board[row][col] != 0:
                print("\nCell is already filled. Choose another cell.")
                time.sleep(2)
                continue
            if is_valid(board, row, col, num):
                board[row][col] = num
                print("\nMove accepted.")
                time.sleep(2)
            else:
                print("\nInvalid move. Try again.")
                time.sleep(2)
        except ValueError:
            print("\nInvalid format. Please enter either:")
            time.sleep(1)
            print(" - 'row col num' for a move,")
            print(" - 'check' to validate the board,")
            print(" - 'finish' to solve the puzzle, or")
            print(" - 'quit' to exit.")
            time.sleep(2)

# Main execution
if __name__ == "__main__":
    print("Welcome to Interactive Sudoku!")
    time.sleep(2)
    print("\nGenerating your puzzle...")
    time.sleep(3)
    puzzle = generate_sudoku()
    print("\nHere is your puzzle:")
    print_board(puzzle)
    user_solve_sudoku(puzzle)
