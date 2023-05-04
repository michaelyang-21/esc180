L = [2.3, 3.9, 4.0, 4.9, 1.3, 2.3]
L[2:3] = []
print(L)

L = [2.3, 3.9, 4.0, 4.9, 1.3, 2.3]
del L[2]
print(L)

def correct_transcipt_bad(grades):
    for i in range(len(grades)):
        if grades[i] < 4.0:
            del grades[i]
#correct_transcipt_bad(L)

def correct_transcipt_bad1(grades):
    i = 0
    while i < len(grades):
        if grades[i] < 4.0:
            del grades[i]
        i += 1

def correct_transcipt_good(grades):
    i = 0
    while i < len(grades):
        if grades[i] < 4.0:
            del grades[i]
        else:
            i += 1


def correct_transcipt_better(grades):
    res = []
    for grade in grades:
        if grade >= 4.0:
            res.append(grade)
    return res


# correct_transcript_bad(grades)
#correct_transcipt_bad1(L)

