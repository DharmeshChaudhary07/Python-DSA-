
# ----------------------------------------- Hashing: Sets for Sequences and Windows ------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

#  Core concept
 
#  `prefix[i]` = sum of the first i elements. The sum of a subarray from `a` to `b` is `prefix[b] - prefix[a]`.
 
#  To find a subarray with sum `target` ending at the current position, you need an earlier prefix equal to `current_prefix - target`.
#  Look it up in a dict as you go.

#  What the dict stores depends on the question:

#  Longest subarray: store the first index where each prefix appeared.
#  Count subarrays: ask yourself what to store instead, and what the map must contain before the loop starts (the “empty prefix”).
 

#  Trick for 0/1 arrays (Contiguous Array): treat 0 as -1, and “equal 0s and 1s” becomes “sum = 0”.
 

#  Value - index dict (Insert Delete GetRandom): a dict that tells you where a value lives lets you find it in O(1). 
# Think about how to delete from a list in O(1) when you know its position.

# ----------------------------------------- 

# Approach: Write `prefix[j] - prefix[i] = target`, rearrange to `prefix[i] = prefix[j] - target`, and decide what the dict
#  must hold. Use this when the array has negatives, because sliding window fails there.

# Common mistakes: forgetting the starting entry `{0: ...}`; overwriting the first index with a later one when you want 
# the longest; looking up `total` instead of `total - target`.

# Recognize the pattern: subarray sum equals or divisible by k, equal number of two things, “contiguous” plus a sum condition with negatives.

# ----------------------------------------- 

# ### Practice first (do these 4 before the plan problems)

# 1. Continuous Subarray Sum (#523)
# 2. Binary Subarray With Sum (#930)
# 3. Subarray Sums Divisible by K (#974)
# 4. Count Number of Nice Subarrays (#1248)

# ----------------------------------------- 