# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

# Example 1:

# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:

# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:

# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dictionary to store the earliest index at which a particular count occurs.
        count_to_index = {0: -1}
        count = 0
        max_length = 0
        
        for i, num in enumerate(nums):
            # Convert 0 to -1, so that sum becomes 0 when there are equal 0s and 1s.
            count += 1 if num == 1 else -1
            
            # If this count has been seen before, update max_length.
            if count in count_to_index:
                max_length = max(max_length, i - count_to_index[count])
            else:
                # Store the first occurrence of this count.
                count_to_index[count] = i
                
        return max_length

