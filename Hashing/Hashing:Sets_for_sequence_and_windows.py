
# ----------------------------------------- Hashing: Sets for Sequences and Windows ------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

# Core concept
# Three uses of sets and counters, one per problem:

# Sequences without sorting: with O(1) lookups you can ask “does the number just before this one exist?” 
# Think about which number is the right place to start counting a run.

# One set per group (Valid Sudoku): keep a set for each row, each column and each box, and check before adding. 
# Ask how to turn a cell `(r, c)` into a box id.

# Fixed window + counts: slide a window of length `len(p)` over `s`, keep a `Counter` of the window, and compare it to the `Counter` of `p`.
#  Add the new character, remove the old one.

# -----------------------------------------

# Common mistakes: leaving zero counts in the window Counter; sorting for the sequence problem and breaking O(n); checking only rows in Sudoku and forgetting columns and boxes.

# Recognize the pattern: longest run in unsorted data, “valid grid”, anagram or permutation inside a longer string.

# -----------------------------------------

# ### Practice first (do these 4 before the plan problems)

# 1. Contains Duplicate II (#219)
# 2. Check If N and Its Double Exist (#1346)
# 3. Longest Harmonious Subsequence (#594)
# 4. Find Common Characters (#1002)

# --------------------------------------------------------------------------------------------------------------------------

from collections import Counter

grid = [
    [1, 2, 3],
    [4, 5, 4],  
    [7, 8, 9] ]

# grid = [                  
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9] ]           # no_duplicate


def rows_with_duplicates(grid):             # one set per row
    for row in grid:
        seen = set()
        for v in row:
            if v in seen:
                return True
            seen.add(v)
    return False

print(rows_with_duplicates(grid))
# print(rows_with_duplicates(grid))



# -----------------------------------------

s = "cbaebabacd"
p = "abc"

def windows_matching(s, p):                 # start indexes of windows that are a bag-match of p
    need = Counter(p)
    window = Counter()
    result = []
    for i, ch in enumerate(s):
        window[ch] += 1
        if i >= len(p):                     # window too long: drop the oldest
            old = s[i - len(p)]
            window[old] -= 1
            if window[old] == 0:
                del window[old]             # needed so == comparison works
        if window == need:
            result.append(i - len(p) + 1)
    return result

print(windows_matching(s,p))

# ----------------------------------------- 