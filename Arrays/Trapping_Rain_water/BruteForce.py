
#TRAPPING RAIN WATER- hard problem
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0  # Return 0 if the height array is empty
        
        n = len(height)
        total_water = 0  # To store the total trapped water
        
        # Iterate through each bar in the height array
        for i in range(n):
            # Find the maximum height to the left of the current bar
            left_max = max(height[:i + 1])
            # Find the maximum height to the right of the current bar
            right_max = max(height[i:])
            
            # Calculate the trapped water for the current bar
            trapped_water = min(left_max, right_max) - height[i]
            total_water += trapped_water
        
        return total_water