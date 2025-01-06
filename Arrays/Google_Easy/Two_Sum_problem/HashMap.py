# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# Use of a hash map- this is a datastucture the stores key-value pairs. It is a collection of items where each item is stored as a key-value pair.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Hash Map: Use a dictionary to store each number in the array (num) as the key and its index (i) as the value.
        # Complement Calculation: For each number in the array, calculate the complement (target - num).
        #Hash Map Lookup: Check if the complement is already in the hash map:
            # If yes, the current number and its complement add up to the target, so return their indices.
            # If no, add the current number and its index to the hash map.
        
        # Create a hash map to store numbers and their indices
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement exists in the hash map
            if complement in num_map:
                # If found, return the indices
                return [num_map[complement], i]
            
            # Otherwise, store the number with its index
            num_map[num] = i


# Execution:
# num_map = {} (initially empty)
# Iterate:
# i = 0, num = 2:
# Complement =  9−2=7
# 7 not in num_map, so add 2:0 to num_map.
# num_map = {2: 0}

# i = 1, num = 7:
# Complement =9−7=2
# 2 is in num_map at index 0. Return [0, 1].
