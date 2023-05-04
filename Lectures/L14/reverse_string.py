# reverse a string
# reverse_str("praxis") -> "sixarp"

def reverse_str1(s):
    return s[::-1]

def reverse_str2(s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res += s[i]
    
    return res

def reverse_str3(s):
    res = ""
    for c in s:
        res = c + res
    
    return res

if __name__ == '__main__':
    print(reverse_str1("praxis"))
    print(reverse_str2("praxis"))
    print(reverse_str3("praxis"))
