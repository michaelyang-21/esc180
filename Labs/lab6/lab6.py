## Problem 3

f = open("data2.txt")
text = f.read()
lines = text.split("\n")

for line in lines:
    if "lol" in line.lower():
        print(line)
## Problem 4

def fict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should     return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter            and can be different every time).
    """

    string = ""
    keys = d.keys()
    for key in keys:
        add = "" + str(key) + ", " + str(d[key])
        string += add + "\n"
    return string
print(fict_to_str({1:2, 5:6}))

## Problem 5
def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""

    string = ""
    sorted_d = sorted(d.items())
    for i in range(len(sorted_d)):
        string += str(sorted_d[i][0]) + ", " + str(sorted_d[i][1]) + "\n"
    return string
print(dict_to_str_sorted({1:2, 0:3, 10:5}))