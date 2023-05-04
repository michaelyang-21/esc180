# Return True iff the string s contains "a" * n + b, with no
# trailing b's or preceding a's

# n_as_plus_b(s, n)
# n_as_plus_b("zaaaby", 3) -> True
# n_as_plus_b("zaaabb", 3) -> False
# n_as_plus_b("aaaab", 3) -> False

# s = aaabxxxabaab        n = 2
# s = xaaabxxxabaabx

def n_as_plus_b(s, n):
    s = "x" + s + "x"

    query = "a" * n + "b"

    while query in s:
        if s[s.find(query) - 1] != "a" and s[s.find(query) + len(query)] != "b":
            return True
        s = s[s.find(query)-1 + len(query):]
    return False

# cur_run_as = 0

def n_as_plus_b1(s, n):
    cur_run_as = 0 # Length of the current of a's in the string that we're processing

    for i in range(len(s)):
        if s[i] == "a":
            cur_run_a += 1

        elif s[i] == "b":
            if cur_run_a == n:
                if i == len(s) - 1:
                    return True
                if s[i+1] != "b":
                    return True
        cur_run_as = 0
    return False
