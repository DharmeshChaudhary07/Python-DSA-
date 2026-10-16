# ----------------------------------------------------- Anagram -------------------------------------------------------

# Core concept

# Two strings are anagrams if they have the same character counts. 
# To group anagrams, give every word a key that is the same for all its anagrams, then use a dictionary from key to list of words. 
# The key can be tuple(sorted(word)) or a tuple of 26 counts. To find an anagram inside a longer string, slide a fixed-size window and compare counts.



# --------------------------

from collections import Counter, defaultdict
def group_anagrams(strs):                   # key = sorted letters
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())

# --------------------------

def group_anagrams_count_key(strs):         # key = 26 counts (faster for long words)
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        groups[tuple(count)].append(s)      # lists can't be keys, tuples can
    return list(groups.values())

# --------------------------

def find_anagrams(s, p):                    # start indices of anagrams of p in s
    if len(p) > len(s):
        return []
    need = Counter(p)
    window = Counter(s[:len(p)])
    result = [0] if window == need else []
    for i in range(len(p), len(s)):
        window[s[i]] += 1                   # add the new character
        out = s[i - len(p)]
        window[out] -= 1                    # remove the oldest character
        if window[out] == 0:
            del window[out]
        if window == need:
            result.append(i - len(p) + 1)
    return result

# --------------------------

# Time: sorted key is O(n x k log k), count key is O(n x k), for n words of length k. Window version is O(len(s)). Space: O(n x k) for groups.

# Approach: “Same letters” means a canonical key. Group with a dictionary. For “find inside a longer string”, use a fixed window.

# Common mistakes: using a list as a dictionary key (use a tuple); not deleting zero counts before comparing counters; skipping the length check.

# Recognize the pattern: “rearrangement of letters”, “group words that use the same letters”, “permutation of a string inside another”.