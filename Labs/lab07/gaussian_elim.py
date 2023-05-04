import numpy as np


def print_matrix(M_lol):

    print("The matrix is currently: ")

    print(np.array(M_lol))

    print("="*10)



def get_lead_ind(row):

    for i in range(len(row)):

        if row[i] != 0:

            return i

    return len(row)



def get_row_to_swap(M, start_i):

    best_lead_ind = len(M[0])

    best_i = len(M[0])

    for i in range(start_i, len(M)):

        lead_ind = get_lead_ind(M[i])

        if lead_ind < best_lead_ind:

            best_i = i

            best_lead_ind = lead_ind

    return best_i, best_lead_ind



def add_rows_coefs(r1, c1, r2, c2):

    r = [0]*len(r1)

    for i in range(len(r)):

        r[i] = c1*r1[i] - c2*r2[i]

    return r



def eliminate(M, row_to_sub, best_lead_ind):

    for row1 in range(row_to_sub+1, len(M)):

        if M[row1][best_lead_ind] != 0:

            M[row1] = add_rows_coefs(M[row1], 1, M[row_to_sub], M[row1][best_lead_ind] / M[row_to_sub][best_lead_ind])

            M[row1][best_lead_ind] = 0







def forward_step(M):

    for row in range(len(M)):

        print("Now looking at row %d" % row)

        print_matrix(M)

        best_i, best_lead_ind = get_row_to_swap(M, row)

        if best_i == len(M[0]):

            break

        print("Swapping rows %d and %d so that entry %d in the current row is non-zero" % (row, best_i, best_lead_ind))



        r = []

        for j in range(len(M[row])):

            r.append(M[row][j])



        M[row] = M[best_i]

        M[best_i] = r



        # M[row] , M[best_i] = M[best_i], M[row]





        print_matrix(M)

        eliminate(M, row, best_lead_ind)

        print_matrix(M)





def backward_step(M):

    for row in range(len(M) -1, -1, -1):

        lead_ind = get_lead_ind(M[row])



        print("Adding row %d to rows above it to add_rows_coefs coefficients in column %d" % (row, lead_ind))



        for row1 in range(row):

            if M[row1][lead_ind] != 0:

                M[row1] = add_rows_coefs(M[row1], 1, M[row], M[row1][lead_ind]/M[row][lead_ind])



        print_matrix(M)



def div_lead_coef(r):

    i = get_lead_ind(r)

    if i < len(r):

        ri = r[i]

        for j in range(i, len(r)):

            r[j] /= ri



def solve(M, b):

    aug = []

    for i in range(len(M)):

        aug.append(M[i] + [b[i]])

    print_matrix(aug)



    # do forward step



    forward_step(aug)



    print_matrix(aug)

    # backward step

    backward_step(aug)



    for i in range(len(aug)):

        div_lead_coef(aug[i])

    print_matrix(aug)



    x = []

    for i in range(len(aug)):

        x.append(aug[i][-1])

    return x









M_listoflists = [[0, 0, 1, 0, 2],[1, 0, 2, 3, 4],[3, 0, 4, 2, 1], [1, 0, 1, 1, 2]]

M = np.array(M_listoflists)

#print(get_row_to_swap(M_listoflists, 1))



forward_step(M)

backward_step(M)



M = np.array([[1, -2, 3], [3, 10, 1], [1, 5, 3]])

x = np.array([7, 10, -1])

b = np.matmul(M, x)

print(solve(M.tolist(), b.tolist()))



