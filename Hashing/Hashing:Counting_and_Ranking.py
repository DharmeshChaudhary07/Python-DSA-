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