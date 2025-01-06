class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0  # Pointer at the beginning of the array
        right = len(height) - 1  # Pointer at the end of the array
        max_area = 0  # Initialize the maximum area
        
        # Move the pointers towards each other
        while left < right:
            # Calculate the area between the two pointers
            area = min(height[left], height[right]) * (right - left)
            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
