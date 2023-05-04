# Computing pi

import random

#pseudo_random
random.seed(0)
random.random()
print(random.random())
print(random.random())

# random number between 5 and 7
5 + 2 * random.random()

# f(f(f(seed)))

#x, y
#x ** 2 + y ** 2 < 1

N =100000
count = 0
for i in range(N):
    x, y = random.random(), random.random()
    if x ** 2 + y ** 2 < 1:
        count += 1

print("pi is approx", 4 * count/N)