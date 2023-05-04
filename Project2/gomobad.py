"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 28, 2022
"""

def is_empty(board):
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != " ":
                return False
    return True
    

def is_sq_in_board(board, y, x):
    if 0 <= y and y < len(board):
        if 0 <= x and x < len(board[y]):
            return True
    return False

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - (length-1)*d_y
    x_start = x_end - (length-1)*d_x

    # If the squares on both sides are blank
    if is_sq_in_board(board, y_start - d_y, x_start - d_x) and is_sq_in_board(board, y_end + d_y, x_end + d_x):
        if board[y_start - d_y][x_start - d_x] == " " and board[y_end + d_y][x_end + d_x] == " ":
            return "OPEN"

    # If the squares on both sides are off the board
    if is_sq_in_board(board, y_start - d_y, x_start - d_x) == False and is_sq_in_board(board, y_end + d_y, x_end + d_x) == False:
        return "CLOSED"

    
    # If the end beginning not on board and other is not the same color
    if is_sq_in_board(board, y_start - d_y, x_start - d_x) == False and is_sq_in_board(board, y_end + d_y, x_end + d_x):
        if board[y_end + d_y][x_end + d_x] != board[y_end][x_end] and board[y_end + d_y][x_end + d_x] != " ":
            return "CLOSED"
    
    # The other way
    if is_sq_in_board(board, y_start - d_y, x_start - d_x) and is_sq_in_board(board, y_end + d_y, x_end + d_x) == False:
        if board[y_start - d_y][x_start - d_x] != board[y_start][x_start] and board[y_start - d_y][x_start - d_x] != " ":
            return "CLOSED"
    
    # If the squares on both sides are not the same colors
    if is_sq_in_board(board, y_start - d_y, x_start - d_x) and is_sq_in_board(board, y_end + d_y, x_end + d_x):
        if board[y_start - d_y][x_start - d_x] != board[y_start][x_start] and board[y_end + d_y][x_end + d_x] != board[y_end][x_end] and board[y_start - d_y][x_start - d_x] != " " and board[y_end + d_y][x_end + d_x] != " ":
            return "CLOSED"

    return "SEMIOPEN"
     
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count = 0
    semi_open_seq_count = 0

    i = 0

    while i < len(board):
        y_cur = y_start + d_y * i
        x_cur = x_start + d_x * i

        if is_sq_in_board(board, y_cur, x_cur) == False:
            if is_bounded(board, y_cur - d_y, x_cur - d_x, i, d_y, d_x) == "SEMIOPEN":
                open_seq_count += 1
                break

        elif board[y_cur][x_cur] != col:
            if is_bounded(board, y_cur - d_y, x_cur - d_x, i, d_y, d_x) == "OPEN":
                open_seq_count += 1
            elif is_bounded(board, y_cur - d_y, x_cur - d_x, i, d_y, d_x) == "SEMIOPEN":
                open_seq_count += 1
            
            i = 0
            y_cur = y_cur + d_y
            x_cur = x_cur + d_x
        
        else:
            i += 1

    return open_seq_count, semi_open_seq_count
    
def detect_rows(board, col, length):
    ####CHANGE ME
    open_seq_count, semi_open_seq_count = 0, 0
    return open_seq_count, semi_open_seq_count
    
def search_max(board):
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    pass


def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0

def is_bounded_test_corner():
    board = make_empty_board(8)
    board[0][0] = "w"
    board[0][7] = "w"
    board[7][0] = "w"
    board[7][7] = "w"
    print_board(board)

    a,mini_test_count=0,0
    #checking (0,0)
    y,x=0,0
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="CLOSED" and is_bounded(board,y,x,1,1,1)=="SEMIOPEN":
        mini_test_count+=4

    #checking (7,0)
    x,y=7,0
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,1)=="CLOSED":
        mini_test_count+=4

    #checking (0,7)
    x,y=0,7
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,1)=="CLOSED":
        mini_test_count+=4

    #checking (7,7)
    x,y=7,7
    if is_bounded(board,y,x,1,0,1)=="SEMIOPEN" and is_bounded(board,y,x,1,1,0)=="SEMIOPEN" and is_bounded(board,y,x,1,1,-1)=="CLOSED" and is_bounded(board,y,x,1,1,1)=="SEMIOPEN":
        mini_test_count+=4

    if mini_test_count == 16:
        print("TEST CASE for is_bounded PASSED!!!!")
    else:
        print("TEST CASE for is_bounded FAILED, passing", mini_test_count,"/16",":(")
  
            
if __name__ == '__main__':
    #play_gomoku(8)
    print_board(8)
    test_is_empty()
    #test_is_bounded()
    #is_bounded_test_corner()
    #test_detect_row()
    