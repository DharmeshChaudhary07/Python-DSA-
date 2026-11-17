
# ----------------------------------- Two pointer and Sliding window Basics -----------------------------------
# -------------------------------------------------------------------------------------------------------------

# What are these two patterns?
# Both patterns replace a nested loop (O(n²)) with a single pass (O(n)) by reusing work already done.

# Two pointers: two indexes move through the data by a rule. They either move toward each other, or both move forward at different speeds.
# Sliding window: a contiguous range `[left, right]` that grows on the right and shrinks on the left. 
# You update the answer for the window instead of recomputing it.
# DE link: a rolling average is a fixed window. Sessionization (cut a new session when the gap is too big) is a variable window.
 
# ----------------------------------- 
### Important points to remember

# - Converging pointers need sorted data (or a reason why moving one end is safe). Sorting first costs O(n log n).
# - Each pointer only moves one way. That is why the total work is O(n) even with a loop inside a loop.
# - Variable window = expand, then shrink while invalid. Decide the “valid” rule before you code.
# - Window sum or count is updated, never recomputed: add the new element, subtract the one that left.
# - Sliding window with a sum condition needs non-negative numbers. With negatives, use prefix sums (Week 2, Day 5).
# - Subarray / substring = contiguous. Subsequence = not contiguous, so a window does not apply.
# - Edge cases to always check: empty input, one element, all equal, window larger than the array, duplicates.

# Pattern	                              Pointers move	             Typical time	          Extra space

# Converging	                       left up, right down	             O(n)	                O(1)
# Fast / slow (read-write)	    both forward, different speed	         O(n)	                O(1)
# Fixed window	                    both forward together	             O(n)	                O(1)
# Variable window + set/map	    right always, left when invalid	         O(n)	                O(k)

# ----------------------------------- 
