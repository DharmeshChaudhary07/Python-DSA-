# ---------------------------------------------- Hashing : Counting and Ranking ----------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

# Core concept

# Day 2(Hashing : FrequencyMaps) gave you counts. 
# Day 3 is about doing something with the counts: order them, pick the top k, rebuild output by count.

# `count.most_common(k)` returns the k biggest as `(value, count)` pairs.

# `sorted(count.items(), key=lambda p: p[1], reverse=True)` sorts all pairs by count. 
# That is O(k log k). Later, think about whether you can avoid a full sort.

# Grouping by a key: compute a key for every item and use `groups[key].append(item)`. 
# The key can be a count, a length or a tuple. `defaultdict(list)` removes the “is the key there yet” check.

# Word Pattern is the mapping idea from Day 2, now between words and letters.

# ------------------------------------------------------

# Approach: Three steps: count, order, build the answer. For grouping problems, the whole problem is choosing the key: 
# “what do all items in one group have in common?”

# Common mistakes: sorting the dict instead of `count.items()`; using a list as a key; 
# ignoring ties; building a string with `+=` in a loop (use a list and `''.join`).

# Recognize the pattern: top k, rank by frequency, “sort by how often”, group, bucket.

# ------------------------------------------------------

# ### Practice first (do these 4 before the plan problems)

# 1. Group Anagrams (#49)
# 2. Find and Replace Pattern (#890)
# 3. Group the People Given the Group Size They Belong To (#1282)
# 4. Find Duplicate File in System (#609)


# ----------------------------------------------------------------------------------------------------------------------------


from collections import Counter, defaultdict

items = [1,2,4,5,1,3,4,3,3,3,5,6]
def sorted_by_count(items):
    count = Counter(items)                                     # count = Counter(items) counts each value:{1: 2, 2: 1, 4: 2, 5: 2, 3: 4, 6: 1}
    return sorted(count.items(), key=lambda p: p[1], reverse=True)

print(sorted_by_count(items))

# count.items() gives the pairs (1,2), (2,1), (4,2), (5,2), (3,4), (6,1).
# sorted(..., key=lambda p: p[1], reverse=True) sorts those pairs:
# p is one pair, like (3, 4).
# p[1] is its count, so key tells sorted to compare by count instead of by value.
# reverse=True puts the biggest count first.


# ----------------------------------

items = ["cat", "dog", "bird", "fish", "ant", "bee"]
make_key = len

def group_by(items, make_key):
    groups = defaultdict(list)
    for item in items:
        groups[make_key(item)].append(item)
    return list(groups.values())

print(group_by(items, make_key))

# group_by(words, len)  -> groups of words with the same length
# make_key can return a str, an int or a tuple (never a list)

# creating a plain {} raises KeyError here.
# Why: groups[key].append(item) does two things in order:
# groups[key] reads the value for that key.
# .append(item) adds to whatever the read returned.

# item	    key	    groups after
# cat	    3	    {3: [cat]}
# dog	    3	    {3: [cat, dog]}
# bird	    4	    {3: [cat, dog], 4: [bird]}
# fish	    4   	{3: [cat, dog], 4: [bird, fish]}
# ant   	3	    {3: [cat, dog, ant], 4: [bird, fish]}
# bee	    3	    {3: [cat, dog, ant, bee], 4: [bird, fish]}