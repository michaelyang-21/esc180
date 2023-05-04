# Start at 0
# Each player can say +1 or +2
# The first player to get to 21 wins

#
#2
#4
#6
#8
#9
#10
#12
#14
#15
#16
#18
#

def is_winning_sum(s):
    '''Return True if getting to the sum s means that the playee wins with perfect play'''
    if s == 21:
        return True

    for move in [1, 2]:
        if is_winning_sum(s + move):
            return False

    return True

    # s = 10
    # if is_winning_sum(11) is False and is_winning_sum(12) is False, then is_winning_sum(10) is True

# state: [0, 0]

def is_win(state):
    return 21 in state

def get_possible_moves(state):
    for i in [1, 2]:
        for j in [1, 2]:
            if state[0] + i <= 21:
                res.append((i, 0))
            if state[1] + j <= 21:
                res.append((0, j))
            res.append((i, j))
    return res

def make_move(state, move):
    new_state = state[:]
    new_state[0] += move[0]
    new_state[1] += move[1]
    return new_state


def is_win_state(state):
    if is_win(state):
        return True

    moves = get_possible_moves(state)
    for move in moves:
        possible_state = make_move(state, move)
        if is_win_state(possible_state):
            return False
    return True


