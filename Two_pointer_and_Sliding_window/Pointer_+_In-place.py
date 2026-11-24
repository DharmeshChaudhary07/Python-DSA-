
# -------------------------------------------------- Pointer + In-place --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

#  Core concept

# Fast / slow (read-write) pointers: `read` scans every element, `write` marks where the next kept value goes. Everything 
# before `write` is the finished result.

#  1. Remove duplicates, keep at most 2: compare the value to the element two places back in the kept part.
#  2. Sort Colors (3 values): use three regions (0s, unknown, 2s) with pointers on their borders. Think 
#     about what happens when you swap with the right side: is the swapped-in value checked yet?
#  3. Trapping Rain Water: water above a bar = min(tallest on its left, tallest on its right) − its height. 
#     Two pointers can track the left max and right max and always process the smaller side.

# ----------------------------------------- 

# Approach: Say what the part before `write` guarantees. That sentence is your loop invariant, and it tells you what to compare against.

# Common mistakes: comparing with `nums[read - 1]` when the rule needs the kept part; not rechecking a value after swapping it from 
# the right (Sort Colors); returning the array instead of the length.

# Recognize the pattern: “in place”, “O(1) extra space”, “return the new length”, three categories to partition, “how much water / area”.

#  Practice first (do these 4 before the plan problems)

# 1. Remove Element (#27)
# 2. Remove Duplicates from Sorted Array (#26)
# 3. Move Zeroes (#283)
# 4. Linked List Cycle (#141)

# ----------------------------------------- 



def keep_if(nums, keep):                   # read-write template
    write = 0
    for read in range(len(nums)):
        if keep(nums, read, write):        # your rule for “this value stays”
            nums[write] = nums[read]
            write += 1
    return write                           # new length


def has_cycle_idea(head):                  # fast/slow on a linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False