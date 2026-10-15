# ------------------------------------------ Strings ----------------------------------------------------------


# A sequence of characters, like an array of characters: 0-based, `s[i]` is O(1), `len(s)` is O(1).
#  Most array patterns (two pointers, sliding window, prefix ideas) work on strings, with the differences below.


# Important points to remember

#  1. Python strings are immutable.
#  `s[0] = 'a'` raises an error. Every “change” builds a new string.
#  To modify characters, convert first: `chars = list(s)`, edit, then `''.join(chars)`.


#  2. Never build a string with `+=` in a loop.
#  It can cost O(n²).
#  Append to a list and `''.join(...)` at the end (O(n)).


#   3. Slicing copies.
#  `s[a:b]` costs O(b-a), so slicing inside a loop hides an O(n²).

#   4. Substring vs subsequence.
#   Substring (Contiguous): Characters must appear right next to each other in the exact order.
#   Example: In "abcdef", "cde" is a valid substring. "ace" is not because it skips characters (b and d).

#   Subsequence (Gaps allowed): Characters must appear in the same relative order, but you are allowed to skip/drop characters in between.
#.  Example: In "abcdef", "ace" is a valid subsequence.


#   5. Character <-> number: `ord('a') = 97`, `chr(97) = 'a'`. `ord(c) - ord('a')` gives an index 0-25 for lowercase letters.

#   6. Useful built-ins: `split`, `join`, `strip`, `lower`, `isalnum`, `isdigit`, `startswith`, `find`, `sorted`, `Counter`.

#   7. Edge cases to always check**: empty string, single character, all same characters, upper/lower case, spaces and punctuation.

# Operation	                                Time

# s[i], len(s)	                            O(1)
# s + t	                                  O(n + m)
# s[a:b]                               	  O(b - a)
# s == t	                                O(n)
# t in s (substring search)     	    O(n x m) worst case
# sorted(s)	                            O(n log n)
# ''.join(list)	                        O(total length)
# s[::-1]	                                O(n)

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
