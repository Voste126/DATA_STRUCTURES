class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0  # Return 0 if the height array is empty
        
        left, right = 0, len(height) - 1  # Two pointers at the start and end
        left_max, right_max = 0, 0  # Track the max heights on the left and right
        total_water = 0  # To store the total trapped water
        
        while left < right:
            if height[left] < height[right]:
                # Update left_max and calculate trapped water at the left pointer
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                # Update right_max and calculate trapped water at the right pointer
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
        
        return total_water
