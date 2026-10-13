# --------------------------------------------- In-place Modification ------------------------------------------------

# Core concept
# Use two pointers on the same array: read scans every element and write marks where the next kept element goes. 
# Because write <= read always, you never overwrite something you have not read yet.

# Filtering (remove element, remove duplicates, move zeroes): if arr[read] is valid, then arr[write] = arr[read]; write += 1.

# Swapping (reverse, sort colors): swap instead of overwrite so no value is lost.

# Rotate by k: reverse the whole array, reverse the first k, reverse the rest (always do k %= n first).

# Index as hashmap: when values are in range 1..n, value v belongs at index v-1. 
# Swap each value into its home position and you get O(1) extra space (First Missing Positive).

# Marker trick: reuse part of the input (first row/column) as flags instead of an extra array (Set Matrix Zeroes).

# Look for the phrases “O(1) extra space” and “modify in place” in the problem.

# What: Modifying the array without using extra space - O(1) extra space constraint (not counting the input/output itself).

# -----------------------------------------------------------------------------------------

# # Move all zeroes to the end, keep relative order of non-zeroes
# def move_zeroes(arr):
#     insert_pos = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
#             insert_pos += 1
#     return arr

# # Reverse array in place
# def reverse(arr):
#     left, right = 0, len(arr) - 1
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
#     return arr

# # Rotate array right by k steps - reverse trick (O(n) time, O(1) space)
# def rotate(arr, k):
#     n = len(arr)
#     k %= n
#     reverse_range(arr, 0, n - 1)
#     reverse_range(arr, 0, k - 1)
#     reverse_range(arr, k, n - 1)

# def reverse_range(arr, i, j):
#     while i < j:
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1
#         j -= 1

# # Dutch National Flag - sort array of 0s, 1s, 2s in one pass
# def sort_colors(arr):
#     low, mid, high = 0, 0, len(arr) - 1
#     while mid <= high:
#         if arr[mid] == 0:
#             arr[low], arr[mid] = arr[mid], arr[low]
#             low += 1
#             mid += 1
#         elif arr[mid] == 1:
#             mid += 1
#         else:  # arr[mid] == 2
#             arr[mid], arr[high] = arr[high], arr[mid]
#             high -= 1  # don't increment mid here - swapped value unchecked

# ​
# Time: O(n) for all above. Space: O(1) — this is the entire point of “in-place”.

# Approach: Usually combined with two pointers — one pointer tracks “where the next valid element should go” (write pointer),
#  the other scans (read pointer). Swap, don’t overwrite — overwriting loses data you might still need.

# Common mistakes: In Dutch National Flag, incrementing mid after swapping with high - wrong, 
# because the swapped-in value from high hasn’t been checked yet; k %= n forgotten in rotate (if k > n, wastes work or errors); 
# using extra array when the problem explicitly says O(1) space (defeats the purpose).

# Recognize the pattern: “modify array in place”, “O(1) extra space”, “remove element”, “rotate array”, “Dutch national flag / sort 0s 1s 2s”, 
# “First Missing Positive” (uses index-as-hashmap trick: place each value at its “correct” index in-place).