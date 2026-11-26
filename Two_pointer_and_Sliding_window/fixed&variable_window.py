
# -------------------------------------------------- Fixed and Variable Window --------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

# Core concept

# Fixed window (size k): build the first window, then slide: add the new element, remove the one that left, update the answer.

# > Variable window: `right` expands every step. While the window is invalid, move `left` forward and undo what `left` contributed.

# 1. Shortest window that is valid (Minimum Size Subarray Sum): shrink while it is still valid, recording the length each time.
# 2. Longest window that is valid (Longest Substring): shrink only when it becomes invalid, then record the length.
# 3. The set or dict inside the window must always describe exactly `[left, right]`.


# ----------------------------------------- 

# Approach: Write the validity rule in words first. Then ask: am I searching for the longest or the shortest? That decides where 
# the answer is recorded.

# Common mistakes: recomputing the window sum each step; recording the answer at the wrong place (before vs after shrinking); removing 
# from the set without moving `left`; using this on arrays with negatives.

# Recognize the pattern: “subarray / substring of size k”, “longest … without”, “smallest length with sum ≥ target”, “rolling average”.


# Practice first (do these 4 before the plan problems)

# 1. Maximum Number of Vowels in a Substring of Given Length (#1456)
# 2. Contains Duplicate II (#219)
# 3. Fruit Into Baskets (#904)
# 4. Max Consecutive Ones III (#1004)

# -----------------------------------------     

def best_fixed(nums, k):                   # fixed window template
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best


def longest_valid(items):                  # variable window with a set
    seen = set()
    left = best = 0
    for right, x in enumerate(items):
        while x in seen:                   # invalid -> shrink
            seen.remove(items[left])
            left += 1
        seen.add(x)
        best = max(best, right - left + 1)
    return best

