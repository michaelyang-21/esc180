import timeit

s = '''def f(N):
    s = 0
    for i in range(N):
        s += i
f(1000000)'''

def f(N):
    s = 0
    for i in range(N):
        s += i

print(timeit.timeit(s, number = 10, globals = globals()))

globals()