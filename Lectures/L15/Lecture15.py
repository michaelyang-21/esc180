alphabet = "abcdef"

for c1 in alphabet:
    for c2 in alphabet:
        for c3 in alphabet:
            print(c1 + c2 + c3)

# Write a function that print strings over the alphabet alphabet, of length n

code = '''a = 5
print(a)'''

exec(code)

# f-string
"abc" + str(5)

x = 5
f"the value of x is {x}"
f"the value of x is {12*5+2}"

def gen_nested_loop(n):
    res = "def gen_passwords(alphabet):\n"

    for i in range(n):
        res += f"{(i+1)*' '} for c{i} in alphabet:\n"
    
    add_line = f"{(n+1)*' '}password = "
    for i in range(n):
        add_line += f"c{i} + "
    add_line += "''"

    res += add_line

    res += f"{(n+1)*' '}print(password)"

    return res

if __name__ == '__main__':
    code_15 = gen_nested_loop(15)
    exec(code_15)
    
