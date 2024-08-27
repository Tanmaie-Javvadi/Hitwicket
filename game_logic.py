def initialize_board():
    board = [[None for _ in range(5)] for _ in range(5)]
    board[4] = ["P1", "H1", "P1", "H2", "P1"]
    board[0] = ["P2", "H2", "P2", "H1", "P2"]
    return board


