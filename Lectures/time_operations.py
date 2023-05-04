import time
import random

N = 10000
s = 0.0
a = 0.0
t0 = time.time()
for i in range(N): #2 operations(increment counter, put in in i
    s += random.random() # ((ax+b)%m)/m
    # ops: *, +, %, extract digits, /, +=, ->s
    # 7 operations in total
    a += 1.0
t1 = time.time()

print(1000* (t1 - t0) / N, "ms per iteration"
print(1000*(t1-t0)/N/11, "ms per operation")


