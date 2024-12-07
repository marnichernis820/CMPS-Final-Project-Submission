import random

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

# Function to check if a number is valid in a given cell
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 sub-grid
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
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Reset if not solvable
                return False
    return True

# Generate a random Sudoku puzzle
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill a few random cells to start
    for _ in range(random.randint(12, 20)):  # Random number of initial clues
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        board[row][col] = num

    return board

# Main execution
if __name__ == "__main__":
    # Generate a puzzle
    print("")
    puzzle = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_board(puzzle)

    # Solve the puzzle
    if solve_sudoku(puzzle):
        print("\nSudoku Puzzle Solved:")
        print_board(puzzle)
    else:
        print("\nNo solution exists!")
        
    print("")
