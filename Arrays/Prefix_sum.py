
# ------------------------------------------ Prefix sum ----------------------------------------------------------

# A Prefix Sum array stores cumulative totals: prefix[i] = arr[0] + arr[1] + ..... + arr[i]

# To find the sum of elements between index L and index R in O(1) time: Sum(L, R) = prefix[R] - prefix[L-1] (If L = 0, Sum(0, R) = prefix[R].)
# Why it works: prefix[R] contains arr[0....R]. Subtracting prefix[L-1] removes arr[0....L-1], leaving exactly arr[L....R].


def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix  # prefix[i] = sum of arr[0.....i-1]

print(build_prefix([7,8,9,0,5,7]))


# # ------------

# Padded version used in the code below: prefix[0] = 0 and prefix[i+1] = prefix[i] + arr[i], so Sum(L, R) = prefix[R+1] - prefix[L]. 
# No special case for L = 0. Example: arr = [2, 4, 1, 3] gives prefix = [0, 2, 6, 7, 10]. Sum(1, 2) = prefix[3] - prefix[1] = 7 - 2 = 5, which is 4 + 1.

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

# # Comparision between approach:

# ------------------------------------------ 

# If your original array is arr = [5, 2, 3]:

# Approach	        Prefix Array Structure	                       Finding Sum of index 0 to 2 (arr[0] to arr[2])

# Approach 1	        [5, 7, 10]                              	Requires an if condition because L-1 is -1.
# Approach 2	        [0, 5, 7, 10]                         prefix[3] - prefix[0] -> 10 - 0 = 10 (No if statement needed)

# ------------------------------------------ 

# # subarray sum of k 
    
# A brute-force approach would check every possible subarray using nested loops, taking O(n**2)or o(n**3) time. 

# This clever approach avoids that by using a mathematical trick.
# The Core Mathematical Intuition


# Let’s define a prefix sum (P) as the running total of elements from the start of the array up to the current index.

# If you want to know the sum of elements between index j and index i, you can find it by subtracting the prefix sum before
#  index j from the prefix sum at index i:

#                                       Subarray Sum=P[i]−P[j−1]

# We are looking for subarrays where this sum equals k:
#                                            P[i]−P[j−1]=k

# If we rearrange this equation to solve for the previous prefix sum (P[j−1]), we get:
#                                            P[j−1]=P[i]−k
\
# As we iterate through the array and track our running sum (curr_sum), we can ask: “Have we seen a previous prefix sum equal to (curr_sum - k) before?” 
# If we have, it means the elements between that previous point and our current point add up to exactly k!



# Subarray sum = k trick: prefix[r+1] - prefix[l] = k is the same as prefix[l] = prefix[r+1] - k. While scanning, 
# count how many earlier prefix sums equal current - k using a hashmap. This works even with negative numbers.

arr = [1,2,3,4,6,9,8]
def subarray_sum_equals_k(arr, k):
    count = 0
    curr_sum = 0
    seen = {0: 1}  # prefix sum -> frequency; 0:1 handles subarray starting at index 0
    for num in arr:
        curr_sum = curr_sum + num
        count += seen.get(curr_sum - k, 0)
        seen[curr_sum] = seen.get(curr_sum, 0) + 1
    return count

print(subarray_sum_equals_k(arr,3))

# ------------------------------------------ 

# Same idea with products: prefix product x suffix product (Product of Array Except Self). Cost: O(n) to build, O(1) per query.

arr = [1,2,3,4,5,6]
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total -= num                 # total is now right_sum
        if left_sum == total:
            return i
        left_sum += num
    return -1
print(equilibrium_index(arr))



# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# Practice problems

# Running Sum of 1d Array (#1480).       

def runningSum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr

print(runningSum([1, 2, 4, 6, 8, 10]))          # time o(n) space o(1)

# ---------------

arr = [1,2,4,6,8,10]

def running_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

print(running_sum(arr))                         # time o(n) space o(1)
