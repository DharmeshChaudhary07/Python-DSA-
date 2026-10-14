
# -----------------------# -----------------------# -----------------------# -----------------------# -----------------------
#                                           Rough work (leetcode and shit)
# -----------------------# -----------------------# -----------------------# -----------------------# -----------------------



# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# nums = [1,7,3,6,5,6]

# def pivot(arr):
#     leftsum = []
#     rightsum = []
#     # for i in range(1, len(nums)):
#     #     nums[i] = nums[i] + nums[i - 1]
    
#     for j in range(len(nums)- 1, 0, -1):
#         nums[j] = nums[j] - nums[j - 1]
#     return nums

# print(pivot(nums))

# -----------------------

# Move zeros

# nums = [0,1,0,3,12]
# def moveZeroes(nums):
#         temp = []
#         for num in nums:
#             if num != 0:
#                 temp.append(num)

#         for i in range(len(temp)):
#              nums[i] = temp[i]     

#         # return nums           # [1,3,12,3,12] -> still holds the 3,12 at index 3 and 4.

#         for i in range(len(temp), len(nums)):
#              nums[i] = 0

#         return nums

# print(moveZeroes(nums))




# ----------------------- 

# Remove element


# Brute force

def removeElement(nums: list[int], val: int) -> int:
    temp = []
        
    for num in nums:
        if num != val:
            temp.append(num)

    for i in range(len(temp)):
        nums[i] = temp[i]

    return len(temp)

    # return nums       # output -> [2, 2, 2, 3], its still holding last two index (2, 3) values. 


print(removeElement([3,2,2,3],3))
