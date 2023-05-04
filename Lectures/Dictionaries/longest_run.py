# find the longest of the character c in the string s
# s = "abbcbbttt" c = "b" longest run: 2
# s = "abbcbbttt" c = "t" longest run: 3

def longest_run(s, c):
    for i in range(len(s), -1, -1):
        if c*i in s:
            return i

# s = "abbbbbbsssssbb", c = "b"

def longest__run2(s, c):
    # state variables
    run = 0 # The length of the current run so far
    max_run = 0 # The longest run we've seen so far

    for ch in s:
        if ch!= c:
            max_run = max(max_run, run)
            run = 0
        else:
            run += 1

    return max(max_run, run)