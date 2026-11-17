
# ----------------------------------- Two pointer and Sliding window Basics -----------------------------------
# -------------------------------------------------------------------------------------------------------------

# What are these two patterns?
# Both patterns replace a nested loop (O(n²)) with a single pass (O(n)) by reusing work already done.

# Two pointers: two indexes move through the data by a rule. They either move toward each other, or both move forward at different speeds.
# Sliding window: a contiguous range `[left, right]` that grows on the right and shrinks on the left. You update the answer for the window instead of recomputing it.
# DE link: a rolling average is a fixed window. Sessionization (cut a new session when the gap is too big) is a variable window.