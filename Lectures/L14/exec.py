s = '''a = 5
print(a)'''
exec(s)

def make_code_that_prints_n(n):
    return "print(" + str(n) + ")"

s = make_code_that_prints_n(60)

exec(s)