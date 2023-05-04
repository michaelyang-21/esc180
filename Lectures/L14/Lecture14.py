s = "abcdef"
# Print out all the strings of length three
# over the alphabet s

"abc"
"dea"
"aaa"

for c1 in s:
    for c2 in s:
        print(c1 + c2)

"aa"
"ab"
"ac"
"ba"
"bb"
"bc"

def print_all_combinations3(S):
    for c1 in s:
        for c2 in s:
            for c3 in s:
                print(c1 + c2 + c3)


if __name__ == '__main__':
    s = "abcdef"
    s1 = "antidisestablishmentarianism"
    print_all_combinations3(s)

    for c in s1:
        print(c)
