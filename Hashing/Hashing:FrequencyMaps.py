# ---------------------------------------------- Hashing Frequency Maps -----------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Core concept ->  A dict from value -> how many times it appears. Build it in one pass, then answer the question with a lookup or a second pass.

# - `Counter(x)` builds the map for you. A missing key gives 0, with no `KeyError`.
# - Two strings or lists are the same “bag” exactly when their counts are equal.

# Consistent mapping (needed for Isomorphic Strings): every character must always map to the same partner. 
# If two different characters may not share a partner, you must also check the reverse direction. Think of two dicts, one per direction.

# ------------------------------------------------------

# Approach: Count first, decide second. For “more than n/2”, the count map is step one; step two is what you compare each count against. 
# For mapping problems, ask “can two different things map to the same thing?”

# Common mistakes: `count[x] += 1` on a plain dict without initializing; forgetting the length check when comparing two strings; 
# checking a mapping in one direction only.

# Recognize the pattern: most or least frequent, majority, “enough of each”, anagram, “same pattern”.

# ------------------------------------------------------

# ### Practice first (do these 4 before the plan problems)

# 1. Find the Difference (#389)
# 2. Unique Number of Occurrences (#1207)
# 3. Find Words That Can Be Formed by Characters (#1160)
# 4. Check if All Characters Have Equal Number of Occurrences (#1941)

# --------------------------------------------------------------------------------------------------------------------------


from collections import Counter

# items = [3,4,6,3,5,6,2,1]
items = "addsda"

def freq_manual(items):
    count = {}
    for x in items:
        count[x] = count.get(x, 0) + 1
    return count

print(freq_manual(items))



# ---------------------------------

# items = [2,4,6,2,4,7,2,4,8,9]
items = "addsda"

def most_frequent(items):
    count = Counter(items)
    return max(count, key=count.get)       # key with the highest count

print(most_frequent(items))



# ---------------------------------

# target = [2]
# source = [3,6,7,2]

target = "addsda"
source = "aaddds"

def can_build(target, source):             # does source have enough of each item?
    have = Counter(source)                 # what we have
    need = Counter(target)                 # what we need 

    for k, c in need.items():              # goes through each item you need. k is the item and c is how many of it you need.
        if have[k] < c:                    # return False means you have fewer than you need, so building is impossible. Stop and return False.
            return False
    return True                            # return True means every item passed the check, so building is possible.

print(can_build(target, source))
