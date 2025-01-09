    
def searchInsert(self,nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    # Binary Tree 
    # O(log n): The binary search reduces the search space by half in   
    #  O(1) space as no additional structures are used.