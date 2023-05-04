# An anagram: two expressions that consist of 
# the same letters, but in possibly different
# order, and with possibly different number
# of spaces, possibly different
# capitalization

"praxis forever"    "a prefix rovers"

"praxis forever".count("e")
"a prefix rovers".count("e")

def is_anagrams(s1, s2):
    '''Return True iff s1 and s2 are anagrams'''

    s1 = s1.lower()
    s2 = s2.lower()

    for c in s1 + s2:
        if c.isalpha():
            if s1.count(c) != s2.count(c):
                return False

    return True

def is_anagrams2(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    return sorted(s1) == sorted(s2)

def is_angrams3(s1, s2):
    return sorted(s1.lower().replace(" ", "")) == sorted(s2.lower().replace(" ", ""))

