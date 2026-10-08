
# ------------------------------------------ Arrays ----------------------------------------------------------

# Arrays are stored in contiguous memory locations, like arrays/tuple and strings.
# As memory is allocated in a contiguous block, it is easy to calculate the address of each element by --> base address + (index * size of each element)

# We can access elements in an array using the index of the element. The index starts from 0 for the first element.

# Some complexity of array operations:
# Access by index: O(1)
# Search (unsorted): O(n)
# Search (sorted): O(log n) via binary search
# Insert/delete at end: O(1) (amortized, for dynamic arrays)
# Insert/delete at start/middle: O(n) (shifting required)

# Python lists / Java ArrayList / C++ vector are dynamic arrays — resize automatically.

# Many array subtopics become easy/hard depending on whether the array is sorted — always check.
# Sorting costs O(n log n) — don't sort if the problem needs original order/index preserved.



# Problems: 

#     Find the max and second max (no sorting).
#     Check if the array is sorted.
#     Move all zeros to the end, keeping the order.
#     Rotate the array by k.

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

arr = [4, 2, 7, 1, 9]

# 1. Traversal: by value, by index, and both
for x in arr: 
    print(x)

for i in range(len(arr)): 
    print(i, arr[i])

for i, x in enumerate(arr): 
    print(i, x)

# ---------------------------


# 2. Reverse traversal
for i in range(len(arr) - 1, -1, -1): 
    print(arr[i])

# ---------------------------


# 3. Max/min without using max()

def find_max(a):
    best = a[0]
    for x in a:
        if x > best:
            best = x
    return best

maxi = find_max([4, 2, 7, 1, 9])
print("Max:", maxi)

# ---------------------------


# 4. Reverse in place (a preview of two pointers)

def reverse(a):
    l, r = 0, len(a) - 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1


# ---------------------------

# 5. Slicing, which is a copy and costs O(k)

print(arr[1:4], arr[::-1])


# ---------------------------

# 6. Insert/delete, which costs O(n) in the middle

arr.insert(2, 99)   # O(n)
print(arr)

arr.pop()           # O(1)
print(arr)          # [4, 2, 7, 1]

arr.pop(0)          # O(n)
print(arr)          # [2, 7, 1, 9]


# ---------------------------

# 7. 2D array creation. Watch this trap(When changing values in one row, all rows change because they are the same list object):

good = [[0] * 3 for i in range(3)]
bad  = [[0] * 3] * 3     # all rows are the SAME list!

print(good)
print(bad)

# ---------------------------

# 8. Count frequency and check duplicates
arr = [1, 2, 3, 4, 5, 1, 2]
from collections import Counter
print(Counter(arr))
print(len(arr) != len(set(arr)))



# -----------------------------------------------------------------------------------------------------------

# Problems: 

#     Find the max and second max (no sorting).

# test case

# 1. if empty then -> return none
#    if 1 element then -> return that element and none
#    if 2 elements then -> return max and min
#    if both are same then -> return that element and none
#    if negative numbers then -> return max and second max

# 2. Make a rough sketch of what i need to do and how i will do it.
#    make two variable highest and 2highest, use one fixed and one moving, campare them if moving is bigger then put it into highest and fixed one 

# brute forcet: Check every pair → nested loop → O(n²).

# #
# loop through the array and check if the current element is greater than highest ->
# if yes then put highest into 2highest and put current element into highest.
# else check if current element is greater than 2highest, if yes then put current element into 2highest.


def max_secondmax(arr):
    first = arr[0]
    for x in arr:              # n times
        if x > first:
            first = x               

    second = None
    for x in arr:              # n times
        if x != first:
            if second is None or x > second:
                second = x
    print(first, second)

value = max_secondmax([2,4,6,2,7,9])    # time complexity = o(n) space 0(1)

# -----------------------------------------------------------------------------------------------------------

#     Check if the array is sorted.

# # test case: 1. if array is empty -> true 
#              2. if only 1 element -> return true 
#              3. if duplicates are there -> return true
#              4. if negative numbers are there -> return true
#              5. if array is sorted in ascending order -> return true
#              6. if array is sorted in descending order -> return true         
#              7. if array is not sorted -> return false.     .....many more


# arr = [2,4,5,7,8]
def is_sorted(arr):
    for i in range(len(arr) - 1):     # n times
        if arr[i] > arr[i + 1]:
            return False
    return True

print(is_sorted([2,4,3,7,8]))   

# alternate 
#  def is_sorted(arr):
#      return all(x <= y for x, y in zip(arr, arr[1:]))

# -----------------------------------------------------------------------------------------------------------

#     Move all zeros to the end, keeping the order.

# Brute force 
arr = [0,2,4,0,5,7,8]
def move_0(arr):
    newlist = []
    for x in arr:
        if x != 0:
            newlist.append(x)
    for x in arr:
        if x == 0:
            newlist.append(x)
    return newlist      

print(move_0(arr))  # time complexity = o(n) space 0(n) 
# why space complexity is O(n) because we are creating a new list to store the non-zero elements and then appending the zeros at the end. 
# This requires additional space proportional to the size of the input array.         



# # better complexity using two pointer. -> time complexity -> o(n) and space complexity -> o(1)

arr = [0,2,4,0,5,7,8]
def movezeros(arr):
    write = 0
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1
    return arr      

print(movezeros(arr))


# -----------------------------------------------------------------------------------------------------------

#     Rotate the array by k.

# if k is bigger than length of arr then k % len(arr) 

arr = [0,2,4,7,8]  
def rotate(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k %= n
    return arr[-k:] + arr[:-k]
# complexity = o(n) space 0(n) because we are creating a new list to store the rotated elements.

print(rotate(arr, 2))


# complexity = o(n) space 0(1) using reverse method

def rotate_in_place(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k %= n

    # Reverse the entire array
    arr.reverse()
    # Reverse the first k elements
    arr[:k] = reversed(arr[:k])
    # Reverse the remaining n-k elements
    arr[k:] = reversed(arr[k:])
    
    return arr

print(rotate_in_place(arr, 2))

# -----------------------------------------------------------------------------------------------------------
