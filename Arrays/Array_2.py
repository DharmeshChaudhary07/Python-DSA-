
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

# # ------------------------------------------ Arrays ----------------------------------------------------------

# # Subtopics covered below:
#                 # - Array traversal
#                 # - Prefix sums
#                 # - Two pointers
#                 # - Sliding window
#                 # - Kadane's Algorithm
#                 # - In-place modification
#                 # - Matrix traversal
#                 # - Intervals

# # -----------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------------

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

# # - Prefix sum
# # Prefix Sum is used to solve problems involving the sum of elements between two indices in an array or operations on subarrays.

# # Time: O(n) to build, O(1) per query after that. Space: O(n) for the prefix array.

# # Approach: Build the prefix array once (O(n)), then every range query is O(1). When the problem wants "number of subarrays 
# # with sum = k" (and numbers can be negative, so sliding window won't work), combine prefix sum with a hashmap of seen sums — this is a very 
# # common interview pattern.

# # Common mistakes: Off-by-one on prefix array indexing (prefix has length n+1); forgetting seen = {0: 1} initialization in 
# # the subarray-sum-k problem (misses subarrays that start at index 0); sliding window only works for positive numbers — if negatives are 
# # allowed, you need prefix sum + hashmap instead.

# # Recognize the pattern: "range sum queries" (especially multiple queries on same array), 
# # "subarray sum equals X" (especially with negative numbers present), "equilibrium/pivot index".

arr = [1, 2, 3, 4, 5]
def build_prefix(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix  # prefix[i] = sum of arr[0..i-1]

# print(build_prefix(arr))


# # Subarray sum equals k (prefix sum + hashmap) - handles negative numbers too
def subarray_sum_equals_k(arr, k):
    count = 0
    curr_sum = 0
    seen = {0: 1}  # prefix sum -> frequency; 0:1 handles subarray starting at index 0
    for num in arr:
        curr_sum += num
        count += seen.get(curr_sum - k, 0)
        seen[curr_sum] = seen.get(curr_sum, 0) + 1
    return count

# print(subarray_sum_equals_k([3,5,7,2,4,8], 3))

# # Equilibrium index - index where left sum == right sum
def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        total -= num                 # total is now right_sum
        if left_sum == total:
            return i
        left_sum += num
    return -1