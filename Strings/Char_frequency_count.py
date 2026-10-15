# ------------------------------------------ Character Frequency Count -------------------------------------------

#  Core concept

#  Count how many times each character appears, in one pass. Two ways:
 
#  1. Dictionary / Counter: works for any characters.

#  2. Fixed array of 26: only for lowercase `a-z`. `count[ord(ch) - ord('a')] += 1`. 
#       This is O(1) space because the alphabet is bounded.
 

#  Two strings are anagrams exactly when their frequency counts are equal.
#  Whenever a problem asks “how many / which / does it contain” about characters, build a frequency map first.

# ---------------------------------------------------------------------------------------------------------------

from collections import Counter

def freq_dict(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count

print(freq_dict("compressors"))


# --------------------------------------------

from collections import Counter

def freq_array(s):                 # lowercase a-z only
    count = [0] * 26
    for ch in s:
        count[ord(ch) - ord('a')] += 1
    return count

print(freq_array("compressors"))

# --------------------------------------------

from collections import Counter

def first_unique(s):               # first character that appears once
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

print(first_unique("compressorsc"))

# --------------------------------------------

from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

print(is_anagram("compressors","comp"))
print(is_anagram("come","comp"))

# # --------------------------------------------


# Time: O(n). Space: O(1) for a bounded alphabet (O(k) for k distinct characters).

# Approach: Build the map in one pass, then answer the question with a second pass or a lookup. 
# To compare two strings, count both and compare, or add for one string and subtract for the other.

# Common mistakes: forgetting the length check before comparing; using `sorted()` (O(n log n)) when counting gives O(n); 
# using the 26-array on uppercase or other characters.

# Recognize the pattern: anagram, unique character, most frequent character, ransom note, “same characters”.

