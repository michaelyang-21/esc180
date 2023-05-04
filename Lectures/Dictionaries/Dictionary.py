grades = {"103": 98, "180":98, "CIV":89}

grades["180"]

print(grades.keys())
print(list(grades.keys()))
print(list(grades.values()))
print(list(grades.items()))

print(list(grades.items())[1][0])
print(list(grades.items())[1][1])

# go through every key k in the dictionary
for k in grades:
    print(k, grades[k])

for course, grade in grades.items():
    print(course, grade)

def get_course_by_grade(grades, grade):
    '''Return the list of course im which we recieved the grade grade'''
    res = []
    for course, gr in grades.items():
        if gr == grade:
            res.append(course)
    return res

# Inverting a dictinoary
# Have the grade be the keys,
# and the vales e lists of the values that correspond to the keys

grades = {"103":98, "180":98, "CIV": 89}
inv_grades = {98:["103", "180"], 89: ["CIV"]}

def invert_dict(d):
    inv_d = {}
    for k, v in d.items():
        if v in inv_d:
            d[v].append(k)
        else:
            d[v] = [k]
    return inv_d