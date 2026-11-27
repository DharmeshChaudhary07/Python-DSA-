
# -------------------------------------------- Window with frequency map -------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# Core concept

# Keep a `Counter` for the window. The window is valid when the counts satisfy the rule.

# 1. Permutation in String: fixed window of size `len(p)`. The window matches when its counts equal `p`’s counts.
# 2. Longest Repeating Character Replacement: window length − count of the most frequent letter = replacements needed. Valid 
#    while that number is ≤ k. Think about whether the max count must be exact after shrinking.
# 3. Minimum Window Substring: track how many required characters are still missing. Expand until nothing is missing, then 
#    shrink to find the smallest window, recording at each valid step.

# -------------------------------------------- 

# Approach: Decide how you test validity cheaply. Comparing two Counters each step is fine for 26 letters. 
# A `missing` count is O(1) per step and is the cleaner choice for Minimum Window.

# Common mistakes: leaving zero counts in the window Counter; shrinking `left` without updating the counts;
# recording the answer only when the window is invalid; forgetting duplicates in `t`.

# Recognize the pattern: “permutation / anagram in a string”, “minimum window containing all”, “replace at most k”.


# Practice first (do these 4 before the plan problems)

# 1. Find All Anagrams in a String (#438)
# 2. Maximum Erasure Value (#1695)
# 3. Get Equal Substrings Within Budget (#1208)
# 4. Frequency of the Most Frequent Element (#1838)
    
# -------------------------------------------- 

from collections import Counter

def window_matches(s, p):                  # fixed window + Counter comparison
    need, window = Counter(p), Counter()
    for i, ch in enumerate(s):
        window[ch] += 1
        if i >= len(p):
            old = s[i - len(p)]
            window[old] -= 1
            if window[old] == 0:
                del window[old]            # needed so == comparison works
        if window == need:
            return True
    return False

def missing_counter(s, t):                 # “how many still missing” bookkeeping
    need = Counter(t)
    missing = len(t)
    # on adding ch: if need[ch] > 0, missing -= 1; then need[ch] -= 1
    # on removing ch: need[ch] += 1; if need[ch] > 0, missing += 1
    return need, missing


# -------------------------------------------- 