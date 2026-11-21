

# -------------------------------------------------- Converging Pointer --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# Core concept

# Put `left` at the start and `right` at the end. Look at the pair, decide which side to move, never go back.

# 1. For a sorted array and a target sum: sum too small -> move `left` up; sum too big -> move `right` down.
# 2. For palindromes: compare the two ends, move both inward.
# 3. For merging two sorted arrays: ask which end is safe to fill first, so you never overwrite a value you still need.

# ----------------------------------------- 

# Approach: Ask “if I move this pointer, can I lose the answer?” If the data is sorted and the move only removes pairs that
# cannot work, the pointers are safe.

# Common mistakes: `<=` instead of `<`; moving the wrong pointer; forgetting to skip non-alphanumeric characters (Valid Palindrome);
#  filling a merge from the front and overwriting values.

# Recognize the pattern: sorted array + pair or target, palindrome, reverse in place, merge two sorted lists.


# # Practice first (do these 4 before the plan problems)

# 1. Reverse String (#344)
# 2. Reverse Vowels of a String (#345)
# 3. Valid Palindrome II (#680)
# 4. Is Subsequence (#392)

# ----------------------------------------- 

sorted_nums = 1,2,4,4,5,6,6,7
target = 14
def has_pair(sorted_nums, target):        # converging template
    left, right = 0, len(sorted_nums) - 1
    while left < right:                   # < not <=, a pair needs 2 different positions
        s = sorted_nums[left] + sorted_nums[right]
        if s == target:
            return True
        if s < target:
            left += 1
        else:
            right -= 1
    return False

print(has_pair(sorted_nums, target))



text = "asdabdsa"
def mirrored(text):                       # compare ends, move inward
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

print(mirrored(text))