# ---------------------------------------------- Hashing Basics -----------------------------------------------
# -------------------------------------------------------------------------------------------------------------

# A hash table stores key -> value pairs. A hash function turns the key into a number, and that number decides which bucket holds the pair.
# Lookup, insert and delete do not scan anything, so they are O(1) on average.

# Python dict = hash table of key -> value.
# Python set = hash table of keys only.
# DE link: dict is GROUP BY, set is DISTINCT, and a lookup in a dict is a hash join.



# # Important points to remember

# 1. Collision: two keys land in the same bucket. Python handles it internally. 
# Many collisions push the worst case to O(n), but treat average O(1) as normal.

# 2. Keys must be hashable: int, str, tuple of hashables are fine. `list`, `set`, `dict` are not. Use `tuple(my_list)` as a key.

# 3. `x in list` is O(n), `x in set` is O(1). Converting a list to a set to check membership is the most common hashing speed-up.

# 4. `d[k]` raises `KeyError` if missing. Use `d.get(k, default)`, `k in d`, `Counter` or `defaultdict`.

# 5. Do not add or remove keys while looping over the same dict. Loop over a copy: `list(d)`.

# 6. Sets have no order and no duplicates. Dicts keep insertion order (Python 3.7+).

# 7. Space trade: hashing buys speed with O(n) extra memory.

# 8. Edge cases to always check: empty input, one element, all elements equal, negative numbers, a key that is not there yet.



# Operation	                                Average time

# d[k], d[k] = v, k in d, del d[k]	            O(1)
# s.add(x), x in s, s.remove(x)	                O(1)
# set(list) / Counter(list)	                    O(n)
# x in list	                                    O(n)
# a & b, a \| b, a - b (sets)	            O(len a + len b)
# loop over a dict or set	                    O(n)

# -------------------------------------------------------------------------------------------------------------

import sys
print(sys.executable)