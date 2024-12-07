from Manual_Game import is_valid, solve_sudoku, generate_sudoku, check_board


def test_sudoku_functions():
    # Test Cases for is_valid
    def test_is_valid():
        print("Testing is_valid()...")
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        assert is_valid(board, 0, 2, 4) == True  # Valid
        assert is_valid(board, 0, 2, 3) == False  # Invalid
        assert is_valid(board, 4, 4, 8) == False  # Subgrid conflict
        assert is_valid(board, 7, 6, 9) == True  # Valid
        assert is_valid(board, 8, 8, 2) == True  # Valid

        print("is_valid() passed all test cases!")

    # Test Cases for solve_sudoku
    def test_solve_sudoku():
        print("Testing solve_sudoku()...")
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        solve_sudoku(board)
        assert board == [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]
        print("solve_sudoku() passed all test cases!")

    # Test Cases for generate_sudoku
    def test_generate_sudoku():
        print("Testing generate_sudoku()...")
        board = generate_sudoku()
        filled_count = sum(row.count(0) for row in board)
        assert 61 <= filled_count <= 69  # Random puzzle should have 12-20 numbers
        print("generate_sudoku() passed all test cases!")

    # Test Cases for check_board
    def test_check_board():
        print("Testing check_board()...")
        original_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        modified_board = [row[:] for row in original_board]
        modified_board[0][2] = 3  # Valid move
        modified_board[1][4] = 1  # Invalid move
        check_board(modified_board, original_board)
        assert modified_board[1][4] == 0  # Invalid move corrected
        print("check_board() passed all test cases!")

    # Run all test cases
    test_is_valid()
    test_solve_sudoku()
    test_generate_sudoku()
    test_check_board()

# Run the tests
test_sudoku_functions()
