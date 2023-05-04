board = [["W", "W","W"],
        ["W", "W", "W"],
        ["W", "W", "W"]]

def is_sq_in_board(board, y, x):
    if 0 <= y and y < len(board):
        if 0 <= x and x < len(board[y]):
            return True

    return False

def is_sequence_complete(board, col, y_start, x_start, length, dy, dx):
    #checking before
    if is_sq_in_board(board, y_start - dy, x_start - dx):
        if board[y_start - dy][x_start - dx] == col:
            return False

    #checks during
    for i in range(length):
        if is_sq_in_board(board, y_start, x_start):
            if board[y_start][x_start] != col:
                return False
            y_start += dy
            x_start += dx
        else:
            return False

    #checks after
    if is_sq_in_board(board, y_start, x_start):
        if board[y_start][x_start] == col:
            return False

    return True

print (is_sequence_complete(board, "W", 2, 2, 3, 1, -1))