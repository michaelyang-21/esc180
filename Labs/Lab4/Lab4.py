#Problem 2

def count_evens(L):

    count = 0
    for num in L:
        if num %2 == 0:
            count += 1
    return count

# Problem 3

def list_to_str(L):

    string = '['
    for i in range(len(L) - 1):
        string += str(L[i]) +", "
    string += str(L[-1]) + "]"
    return string

# Problem 4

def lists_are_the_same(list1, list2):

    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

# Problem 5

def list1_start_with_list2(list1, list2):

    if len(list1) < len(list2):
        return False

    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

# Problem 6

def match_pattern(list1, list2):

    for i in range(len(list1) - len(list2)):
        for j in range(len(list2)):
            if list1[i+j] != list2[j]:
                break
            if j == len(list2) - 1:
                return True
    return False

# Problem 7

def duplicates(list0):
    for i in range(len(list0) - 1):
        if list0[i] == list0[i+1]:
            return True
    return False

L1 = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, 5]
L3 = [1, 3, 5, 7, 9]
L4 = [1, 2, 3, 4, 5, 6]
L5 = [1, 2, 3]

L6 = [4, 10, 2, 3, 50, 100]
L7 = [2, 3, 50]
L8 = [1, 2, 3, 3]

print(count_evens(L1))
print(list_to_str(L1))
print(lists_are_the_same(L1, L2))
print(lists_are_the_same(L1, L3))
print(list1_start_with_list2(L1, L5))
print(list1_start_with_list2(L1, L4))



print(match_pattern(L6, L7))
print(match_pattern(L3, L4))
print(duplicates(L8))