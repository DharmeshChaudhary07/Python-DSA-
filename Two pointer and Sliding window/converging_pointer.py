

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

# ----------------------------------------- 
