import random
import time
import timeit

def longest_run1(s, c):
    # n = len(s)
    run = 0
    max_run = 0

    #k1 * n
    if c == "z":
        s += "y"   # s = s + "y"
    else:
        s += "z"

    # k2*n
    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1

    return max_run

# (k1 + k2) * n + k3 time is O(n)


def longest_run2(s, ch):
    for longest in range(len(s), -1, -1):
        if ch*longest in s:
            return longest

    return 0 #Optional, 0 will be returned anyway since '' is in any string


def longest_run3(s, ch):
    for longest in range(len(s), -1, -1):
        cur_run = 0
        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0

            if cur_run == longest:
                return longest
    return 0 # Optinoal, 0 will be returned anyway since '' is in any string


def gen_ab(length):
    s = ""
    for i in range(length):
        if random.random() > 0.5:
            s += "a"
        else:
            s += "b"
    return s

lengths = [10, 100, 500, 1000, 1500, 2000, 5000, 10000, 100000, 200000, 400000, 1000000]

runtime1 = []
runtime2 = []
runtime3 = []

for length in lengths:
    s = gen_ab(length)
    runtime1.append(timeit.timeit("longest_run1(s, 'b')", number = 20, globals = globals()))
    runtime2.append(timeit.timeit("longest_run1(s, 'b')", number = 20, globals = globals()))
    runtime3.append(timeit.timeit("longest_run1(s, 'b')", number = 20, globals = globals()))


plt.figure(1)
plt.plot(lengths[:8], )
