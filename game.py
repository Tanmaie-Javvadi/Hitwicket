def move_character(board, character, current_position, move):
    row, col = current_position
    
    # Determine the move based on the character type and move command
    if character in ["P1", "P2"]:  # Pawn
        if move == "L": col -= 1
        elif move == "R": col += 1
        elif move == "F":
            if character == "P1":
                row -= 1
            else:
                row += 1
        elif move == "B":
            if character == "P1":
                row += 1
            else:
                row -= 1

    elif character == "H1":  # Hero1
        if move == "L": col -= 2
        elif move == "R": col += 2
        elif move == "F":
            if character == "P1":
                row -= 2
            else:
                row += 2
        elif move == "B":
            if character == "P1":
                row += 2
            else:
                row -= 2

    elif character == "H2":  # Hero2
        if move == "FL":  # Forward-Left
            if character == "P1":
                row -= 2
            else:
                row += 2
            col -= 2
        elif move == "FR":  # Forward-Right
            if character == "P1":
                row -= 2
            else:
                row += 2
            col += 2
        elif move == "BL":  # Backward-Left
            if character == "P1":
                row += 2
            else:
                row -= 2
            col -= 2
        elif move == "BR":  # Backward-Right
            if character == "P1":
                row += 2
            else:
                row -= 2
            col += 2

    # Ensure the move is within the board bounds
    if 0 <= row < 5 and 0 <= col < 5:
        # Check if the target cell is occupied by an opponent's character
        target_cell = board[row][col]
        if target_cell is not None:
            # Implement logic for capturing/killing the opponent's character (if needed)
            print(f"{character} captures {target_cell}")

        # Move the character to the new position
        board[current_position[0]][current_position[1]] = None  # Remove from old position
        board[row][col] = character  # Place in new position

    return board
