
# '''
# # --------------------------------------------------------
# Steps to follow:

# 1. Read the problem twice. Note: input type, constraints (size of n, sorted or not, duplicates allowed?, negative numbers?), and what exactly to return.

# 2. Think brute force first (even if you won't code it) — usually nested loop, O(n²).
# This tells you the "naive" baseline and often reveals why it's slow (recomputing/rechecking same things).

# 3. Ask what's slow about the brute force — am I re-searching for something repeatedly? → hashmap. Am I re-summing a range? → prefix sum. 
# Am I checking all pairs on a sorted array? → two pointers. Am I checking all subarrays? → sliding window.

# 4. Match the "slow part" to a pattern from your notes (this is the actual skill — recognizing which technique kills the bottleneck).

# 5. Write pseudocode before code — plain English steps, no syntax.

# 6. Code it.

# 7. Trace through a small example by hand (3-5 elements) before trusting it.

# 8. Check edge cases: empty input, one element, already-sorted, duplicates, negatives.

# # --------------------------------------------------------

# Example: Two Sum (array, unsorted, return indices of pair summing to target)

# Step 1 — brute force thought: Check every pair → nested loop → O(n²).

# Step 2 — what's slow?: For each number, I'm searching the rest of the array for target - num. Searching repeatedly = slow.

# Step 3 — match pattern: "Have I seen this value before?" → hashmap gives O(1) lookup instead of O(n) search.

# Step 4 — pseudocode:

#                         create empty hashmap  (value -> index)
#                         for each index i, number num in array:
#                             complement = target - num
#                             if complement exists in hashmap:
#                                 return [hashmap[complement], i]
#                             else:
#                                 store num -> i in hashmap
#                         return "no answer found"

# Step 5 — code it (you already have this in your notes).

# Step 6 — trace by hand: arr = [2,7,11,15], target = 9

#     i=0, num=2, complement=7, not in map → store {2:0}
#     i=1, num=7, complement=2, 2 is in map → return [0,1] ✅

# Step 7 — edge cases: empty array (no pair exists), no valid pair exists (return what? check problem spec), same number used twice (does [3,3] with target 6 count — need two different indices, map handles this naturally since you check before storing).

# This same 8-step flow is what you run on every problem — the pattern-matching in step 3/4 gets faster the more problems you do.

# '''

# # ------------------------------------------ Arrays Traversal ----------------------------------------------------------

# # Array traversal is the process of visiting each element of an array exactly once to perform some operation on it. 

# # Time: O(n) always (visiting each element once). Space: O(1) if not storing results, O(n) if building an output array.

# # Approach: No real "technique" — it's the base skill every other pattern sits on. 
# # Get comfortable with index math (i+1, i-1, boundaries 0 and len(arr)-1) since off-by-one errors here cause most array bugs.

# # Common mistakes: range(len(arr)) vs range(len(arr)-1) confusion; accessing arr[i+1] without checking i+1 < len(arr) → IndexError; 
# # forgetting Python supports negative indexing (arr[-1] = last element).

# # Recognize when it's "just traversal": Problem asks to compute something by looking at each element once with no relationship 
# # between elements (sum, max, count, find an element).


arr = [1, 2, 3, 4, 5]
# forward
for i in range(len(arr)):               # len -> 5  
    print(arr[i])

# backward
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])

# with index + value
for i, val in enumerate(arr):
    print(i, val)

# step up traversal
for i in range(0, len(arr), 2):
    print(arr[i])

# # -----------------------------------------------------------------------------------------------------------


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

# Reverse an array without [::-1] or .reverse().


def reverse(arr):
    arr.reverse()
    return arr
print(reverse([2,4,6,3,7]))

# When we write return arr.reverse(), we are returning the result of the .reverse() method rather than the modified list itself.

def reverse(arr):
    return arr[::-1]
print(reverse([2,4,6,3,7]))


# Approach	            Time Complexity             Space Complexity	                     Notes
# arr.reverse()         	O(N)	                      O(1)	             Reverses in-place; memory overhead is constant.
# arr[::-1]	                O(N)	                      O(N)	             Creates and returns a shallow copy in reverse order.
# list(reversed(arr))      	O(N)	                      O(N)	       reversed() creates an iterator (O(1)), and list() builds the new list (O(N)).

def reverse(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left] , arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
print(reverse([3,4,6,7,8,]))   # time O(n/2) , space(n)

# -----------------------------------------------------------------------------------------------------------

# Return a new array where out[i] = max of arr[0..i] (running max).

def max(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

print(max([1,2,3,4,5]))         # time O(n) , space(1)

# -----------------------------------------------------------------------------------------------------------

# Find the first and last index of a target in one pass (return [-1, -1] if absent).

def first_and_last(arr, k):
    first = -1
    last = -1
    for i, value in enumerate(arr):
        if value == k:
            if first == -1:
                first = i
            last = i
    return [first, last]                    # time O(n) , space(1)   # o(1) only beacuse return list is not growing with input array.
print(first_and_last([7,4,3,5,3,7,2], 3))        



# -----------------------------------------------------------------------------------------------------------

# Missing Number: array holds n distinct numbers from 0..n, find the missing one (try the sum formula first).

def missing(arr):
    n = len(arr)
    sum = n * (n + 1)// 2
    total = 0
    for i in arr:
             total += i
        
    return sum - total

print(missing([1,0,3,4,2]))

# -----------------------------------------------------------------------------------------------------------


def missing(arr):
    n = len(arr)
    exp_sum = n * (n + 1) // 2
    return exp_sum - sum(arr)
print(missing([1,0,3,4,2]))



