import random

# Function to print the Sudoku board with 4x4 borders (16x16 grid)
def print_board(board):
    for i, row in enumerate(board):
        if i % 4 == 0 and i != 0:
            print("-" * 41)  # Horizontal border for 16x16 grid
        row_str = ""
        for j, num in enumerate(row):
            if j % 4 == 0 and j != 0:
                row_str += "| "  # Vertical border for 4x4 sub-grids
            row_str += (str(num) if num != 0 else ".") + " "
        print(row_str)

# Function to check if a number is valid in a given position
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(16)]:
        return False
    start_row, start_col = 4 * (row // 4), 4 * (col // 4)
    for i in range(start_row, start_row + 4):
        for j in range(start_col, start_col + 4):
            if board[i][j] == num:
                return False
    return True

# Backtracking solver
def solve_sudoku(board):
    for row in range(16):
        for col in range(16):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 17):  # Try numbers 1-16
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Reset if not solvable
                return False
    return True

# Generate a fully solved 16x16 Sudoku grid
def generate_solved_sudoku():
    board = [[0 for _ in range(16)] for _ in range(16)]

    def fill_grid():
        for row in range(16):
            for col in range(16):
                if board[row][col] == 0:
                    numbers = list(range(1, 17))
                    random.shuffle(numbers)
                    for num in numbers:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if fill_grid():
                                return True
                            board[row][col] = 0
                    return False
        return True

    fill_grid()
    return board

# Remove numbers to create a puzzle
def create_puzzle(board, clues=60):
    puzzle = [row[:] for row in board]  # Copy the board
    cells = [(row, col) for row in range(16) for col in range(16)]
    random.shuffle(cells)

    for row, col in cells:
        if sum(row.count(0) for row in puzzle) >= (16 * 16 - clues):
            break
        backup = puzzle[row][col]
        puzzle[row][col] = 0
        temp = [row[:] for row in puzzle]
        if not solve_sudoku(temp):
            puzzle[row][col] = backup

    return puzzle

# Main execution
if __name__ == "__main__":
    print("\nGenerating a fully solved 16x16 Sudoku grid...")
    solved_board = generate_solved_sudoku()

    print("\nCreating a puzzle from the solved grid...")
    puzzle = create_puzzle(solved_board, clues=60)

    print("\nUnsolved Sudoku Puzzle:")
    print_board(puzzle)

    print("\nSolving the puzzle...")
    solved_puzzle = [row[:] for row in puzzle]
    solve_sudoku(solved_puzzle)

    print("\nSolved Sudoku Puzzle:")
    print_board(solved_puzzle)
