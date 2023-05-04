L = [[1, 2], [3, 4]]
L1 = L # changing L1[0] change L[0], changing L1[1][0]
# changes L[1][0]

L2 = [L[0], L[1]]

import copy
copy.deepcopy(L)
L3 = [[L[0][0], L[0][1]], [L[1][0], L[1][1]]]

L2[0] = 3 # L2 is now [3, [3, 4]], L and L1 are unchanged 
L2[1][1] = 3 # L2 is now [3, [3, 3]], L and L1 are [[1, 2], [3, 3]]

# Global variables
# Name          Address
# L             @1120
# 

# Memory
# Address       Value
# 1000          1
# 1020          2
# 1040          3
# 1060          4
# 1080          [@1000, @1020] # L[0], also L1[0]
# 1100          [@1040, @1040] # L[1], also L1[1]
# 1120          [@1080, @1100] # L (also L1)
# 1140          [@1040, @1100] # L2