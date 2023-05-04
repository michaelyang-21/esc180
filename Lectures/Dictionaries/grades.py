def correct_transcipt_dict_bad(grades):
    for course, grade in grades:
        if grade < 97:
            del grades[course]

def correct_transcipt_dict_bad(grades):
    for course in list(grades.keys()):
        if course[grades] < 97:
            del grades[course]

def correct_transcript_dict_bad(grades):
    for course, grade in grades.items():
        if grade < 97:
            del grades[course]

def correct_transcript_dict_ok(grades):
    for course in list(grades.keys()):
        if grades[course] < 97:
            del grades[course]

def drop_everything_bad(grades):
    grades = {}

def drop_everything1(grades):
    for course in list(grades.keys()):
        del grades[course]

def drop_everything2(grades):
    while len(grades) != 0:
        del grades[list(grades.keys())[0]]

grades = {"103":98, "180":98, "CIV": 89}
#correct_transcipt_dict(grades)

correct_transcript_dict_ok(grades)
drop_everything1(grades)






