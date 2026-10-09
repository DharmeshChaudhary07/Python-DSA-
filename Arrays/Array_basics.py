
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

