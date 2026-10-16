# ------------------------------------------ Two Pointers on Strings  ---------------------------------------------

# Core concept
# Same idea as arrays: two indices, left and right, move inward from both ends, or in the same direction. 
# Because strings are immutable, you usually compare characters instead of swapping them. To swap, convert to a list first.

# Palindrome check: compare s[left] and s[right], then move both inward. Stop when they meet.

#----------------------------

def reverse_string(chars):           # LeetCode gives a list of characters
    l, r = 0, len(chars) - 1
    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1

# ----------------------------

def is_palindrome(s):                # ignore non-alphanumerics, ignore case
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

# ​----------------------------------------------------------------------------------------------------------------

# Time: O(n). Space: O(1) (O(n) if you copy to a list).

# Approach: Ask “can I decide which pointer to move from the comparison?” For palindromes the answer is “both move inward if the characters 
# match, otherwise stop”.

# Common mistakes: forgetting the l < r check inside the skipping loops (index error); not lowercasing; trying to assign s[i] directly.
# Recognize the pattern: palindrome, reverse, “compare from both ends”, merging two strings.