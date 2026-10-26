
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

# ----------------------------------------------------------------------------------`ß-----------------------------------------