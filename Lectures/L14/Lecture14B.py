s = "antidisestablishmentarianism"

for c in s:
    print(c)

s[:4] #splicing does not change string

L = [4, 5, 1]
L.sort()
#sort changes L
print(L)

# .replace does not change s. Must be assigned to new variable
s_pro = s.replace("anti", "pro")
print(s)
print(s_pro)

s.capitalize()

def my_capitalize(s):
    #s = s.capitalize
    return s.capitalize()

if __name__ == '__main__':
    s = "antidisestablishmentarianism"
    s = my_capitalize(s)
    print(s)