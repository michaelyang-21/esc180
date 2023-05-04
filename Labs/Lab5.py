'''
 X | O | X

---+---+---

 O | O | X

---+---+---

   | X |

'''



import random





def print_board_and_legend(board):

    for i in range(3):

        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]

        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)

        print(line1 + " "*5 + line2)

        if i < 2:

            print("---+---+---" + " "*5 + "---+---+---")







def make_empty_board():

    board = []

    for i in range(3):

        board.append([" "]*3)

    return board





def coordinate(square_num):

    row_num = ((square_num - 1) // 3)

    column_num = (square_num % 3) - 1



    coord = [row_num, column_num]

    return coord;





def put_in_board(board, mark, square_num):

    coord = coordinate(square_num)

    board[coord[0]][coord[1]] = mark





def get_free_squares(board):

    coordinates = []

    for i in range(3):

        for j in range(3):

            if board[i][j] == " ":

                 coord = [i, j]

                 coordinates.append(coord)



    return coordinates



def make_random_move(board, mark):

    coordinates = get_free_squares(board)

    n = random.randint(0, len(coordinates))



    random_pos = coordinates[n]

    board[random_pos[0]][random_pos[1]] = mark



def is_row_all_three(board, row_i, marks):

    for i in range(3):

        if (board[row_i][i] != marks):

            return False



    return True



def is_col_all_three(board, col_i, marks):

    for i in range(3):

        if (board[i][col_i] != marks):

            return False



    return True



def is_left_diag_all_three(board, mark):

    for i in range(3):

        if board[i][i] != mark:

            return False

    return True





def is_right_diag_all_three(board, mark):

    for i in range(3):

        if board[i][2-i] != mark:

            return False

    return True



def is_win(board, mark):

    for i in range(3):

        if is_row_all_three(board, i, mark):

            return True



    for i in range(3):

        if is_col_all_three(board, i, mark):

            return True



    if is_right_diag_all_three(board, mark):

        return True



    if is_left_diag_all_three(board, mark):

        return True



    return False





def smart_comp_move(board, mark):

    free_squares = get_free_squares(board)

    for sq in free_squares:

        row, column = sq[0], sq[1]

        board[row][column] = mark

        if is_win(board, mark):

            return



        board[row][column] = " "



    make_random_move(board, mark)



if __name__ == '__main__':

    board = make_empty_board()

    print_board_and_legend(board)



    print("\n\n")



    #board = [["O", "X", "X"],

    #         [" ", "X", " "],

    #         [" ", "O", " "]]



    #print_board_and_legend(board)



    count = 0

    while (count < 9):

        if (count % 2 == 0):

            mark = "X"

            print("Player move")

            print("Enter your move: ", end = "")

            square_num = int(input())

            put_in_board(board, mark, square_num)



            if (is_win(board, "X") == True):

                print("Player wins!")

                break;





        else:

            print("Computer move")

            mark = "O"



            smart_comp_move(board, mark)



            if (is_win(board, "O") == True):

                print("Computer wins!")

                break;





        print_board_and_legend(board)

        print("\n\n")



        count += 1;



    print_board_and_legend(board)

