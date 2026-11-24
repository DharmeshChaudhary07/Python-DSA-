
# -------------------------------------------------- Pair / Triple Search --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

#  Core concept
 
#  Same converging idea, but now the decision rule is the hard part.
 
#  1. Squares of a Sorted Array: negatives become large after squaring. Where is the largest square always found? Fill the answer from that end.
#  2. Container With Most Water: area = width × the shorter height. Moving the taller line can never help, because the width shrinks and 
#     the height is still capped by the shorter line. Think about which line is worth replacing.
#  3. Sum: fix one number, then run the pair search on the rest. The array must be sorted first.
#  4. Skipping duplicates: after you use a value, move past every copy of it so the same triple is not reported twice.

# --------------------------------------------------

# Approach: Write down, in one sentence, why discarding a pointer position is safe. If you cannot say it, the move is a guess.

# Common mistakes: forgetting to sort; skipping duplicates before using a value instead of after; not moving both 
# pointers after a hit; filling Squares from the front.

# Recognize the pattern: “all unique triplets”, “maximize area between two ends”, sorted + negatives + transform.


#  Practice first (do these 4 before the plan problems)

# 1. 3Sum Closest (#16)
# 2. Boats to Save People (#881)
# 3. Valid Triangle Number (#611)
# 4. 4Sum (#18)

# --------------------------------------------------

def pairs_for_each_first(nums):            # 3Sum-style skeleton (not a full solution)
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate first value
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            # compare nums[i] + nums[left] + nums[right] with the target,
            # move a pointer, and after a hit skip duplicate left/right values
            ...

