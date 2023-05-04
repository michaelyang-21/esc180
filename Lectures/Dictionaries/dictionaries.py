# dictionaries

# key-value pairs
# keys are unique
# values can repeat

passwords = {"guerzhoy": "asdf", "cluett": "matrix", "stangeby": "rigorous"}

print(passwords["cluett"])

passwords["cluett"] = "vector"

# keys must be immutable
passwords[(1, 2)] = 5
print(passwords)