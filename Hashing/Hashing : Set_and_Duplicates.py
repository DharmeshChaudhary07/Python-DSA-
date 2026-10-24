# ---------------------------------------------- Hashing Sets and Duplicates -----------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------

# Core concept ->  A set answers one question in O(1): “have I seen this before?” Walk through the data once, check the set, then add to it.
# This replaces a nested loop (O(n²)) with a single pass (O(n)).

# Set operators: `a & b` (in both), `a | b` (in either), `a - b` (in a but not b).


# ------------------------------------------------------

# Approach: Ask “what do I need to remember from the past?” If the answer is only “which values appeared”, use a set.
#  If you also need a count or a position, use a dict (Day 2 and Day 5).

# Common mistakes: adding to the set before checking (everything looks like a duplicate); using a list for `seen`; 
# forgetting that `set(a)` drops duplicates.

# Recognize the pattern: duplicate, appears twice, common elements, unique values, “have I seen this”, a process that may 
# repeat a state (Happy Number: what must happen if it never reaches 1?).

# ------------------------------------------------------

# # Practice first (do these 4 before the plan problems)

# 1. Single Number (#136)
# 2. Missing Number (#268)
# 3. Set Mismatch (#645)
# 4. Distribute Candies (#575)

    # --------------------------------------------------------------------------------------------------------------------------

# first value that appears a second time

nums = [1,2,3,4,3,2,5]
def first_repeated(nums):          
    seen = set()
    for x in nums:
        if x in seen:              # check BEFORE adding
            return x
        seen.add(x)
    return None

print(first_repeated(nums))


# -------------------------------


a = [1,3,4,6,7]
b = [2,4,7,2,8]

def set_operations(a, b):
    a_set, b_set = set(a), set(b)
    both = a_set & b_set
    either = a_set | b_set
    only_in_a = a_set - b_set
    return both, either, only_in_a

print(set_operations(a,b))