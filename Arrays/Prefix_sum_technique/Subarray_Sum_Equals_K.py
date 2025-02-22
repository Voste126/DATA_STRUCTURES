# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    
        prefix_sum_map = {0: 1}  # Initialize with 0:1 to handle subarrays starting from index 0
        running_sum = 0
        count = 0

        for num in nums:
            running_sum += num  # Update the cumulative sum
            
            # Check if the complement exists
            complement = running_sum - k
            if complement in prefix_sum_map:
                count += prefix_sum_map[complement]
            
            # Add the current running_sum to the map or increment its count
            prefix_sum_map[running_sum] = prefix_sum_map.get(running_sum, 0) + 1

        return count
