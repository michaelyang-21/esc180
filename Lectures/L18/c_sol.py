L = [[5, 6], 7]
L1 = [L[0]]
L1[0][1] = 7
L1[0] = [7]
print(L) # [[5, 7], 7]
print(L1) # [[7]]

# Global variables
# Name          Address
# L             @1080
# 

# Memory
# Address       Value
# 1000          5
# 1020          6
# 1040          7
# 1060          [@1000, @1040]  # L[0]
# 1080          [@1060, @1040]  # L
# 1100          [@1120]         # L1
# 1120          [@1040]         # L1[0]
# 1140          