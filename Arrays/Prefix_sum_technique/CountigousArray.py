# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.


class Solution(object):
    def findMaxLength(self,nums):
    # Initialize the hashmap and variables
        sum_index_map = {0: -1}  # To handle the case where the subarray starts at index 0
        max_length = 0
        running_sum = 0

        for i, num in enumerate(nums):
            # Replace 0 with -1
            running_sum += -1 if num == 0 else 1
            
            if running_sum in sum_index_map:
                # If running_sum was seen before, calculate subarray length
                max_length = max(max_length, i - sum_index_map[running_sum])
            else:
                # Otherwise, store the index of this running_sum
                sum_index_map[running_sum] = i

        return max_length
