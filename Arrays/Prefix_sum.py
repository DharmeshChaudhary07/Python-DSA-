
# ------------------------------------------ Prefix sum ----------------------------------------------------------

# A Prefix Sum array stores cumulative totals: prefix[i] = arr[0] + arr[1] + ... + arr[i]

# To find the sum of elements between index L and index R in O(1) time: Sum(L, R) = prefix[R] - prefix[L-1] (If L = 0, Sum(0, R) = prefix[R].)

# Why it works: prefix[R] contains arr[0..R]. Subtracting prefix[L-1] removes arr[0..L-1], leaving exactly arr[L..R].

# Padded version used in the code below: prefix[0] = 0 and prefix[i+1] = prefix[i] + arr[i], so Sum(L, R) = prefix[R+1] - prefix[L]. 
# No special case for L = 0. Example: arr = [2, 4, 1, 3] gives prefix = [0, 2, 6, 7, 10]. Sum(1, 2) = prefix[3] - prefix[1] = 7 - 2 = 5, which is 4 + 1.


def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix  # prefix[i] = sum of arr[0..i-1]

print(build_prefix([7,8,9,0,5,7]))

# # ------------

arr = [3, 1, 4, 1, 5, 9]

prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)             # prefix array is now: [0, 3, 4, 8, 9, 14, 23]
# 3. Range Sum Function
def range_sum(prefix, l, r):  # Sum of arr[l..r] inclusive
    return prefix[r + 1] - prefix[l]

print(range_sum(prefix, 1, 4)) 

print(range_sum(prefix, 0, 2))

# ------------------------------------------ 


# using both build prefix and range_sum togther 

arr = [3, 1, 4, 1, 5, 9]
def build_prefix(arr):                                      # just a running total
    prefix = [0] * (len(arr) + 1)                           # creates a array [0,0,0,0,0,0,0] -> 7
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix  # prefix[i] = sum of arr[0..i-1]         # build_prefix: O(N) Time, O(N) Space

prefix = build_prefix(arr)
print(build_prefix(arr))

def range_sum(prefix, l, r):  # Sum of arr[l..r] inclusive      # prefix = [0, 3, 4, 8, 9, 14, 23]
    return prefix[r + 1] - prefix[l]                            # prefix[4+1] - prefix[1] -> 14 - 3 => 11

print(range_sum(prefix, 1, 4)) 
print(range_sum(prefix, 0, 2))   

# build_prefix: O(N) Time, O(1) Space


# ------------------------------------------ 

# Subarray sum = k trick: prefix[r+1] - prefix[l] = k is the same as prefix[l] = prefix[r+1] - k. While scanning, 
# count how many earlier prefix sums equal current - k using a hashmap. This works even with negative numbers.


# ------------------------------------------ 

# Same idea with products: prefix product x suffix product (Product of Array Except Self). Cost: O(n) to build, O(1) per query.

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Practice problems

# Running Sum of 1d Array (#1480).          


# Range Sum Query - Immutable (#303).
    

# Find Pivot Index (#724).


# Contiguous Array (#525): treat 0 as -1, then it becomes "longest subarray with sum 0".