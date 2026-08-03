class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left = 0
        # right = len(nums)

        # if len(nums) < 1 and nums[0] == target:
        #     return 0
        
        # while left<right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left += mid
        #     else:
        #         right -= mid
                    
        # return -1

        if not nums:
            return -1
        
        left = 0 
        right = len(nums) - 1  # Fix: Use valid maximum index
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:  # Fix: Compare array element, not index
                left = mid + 1        # Fix: Move past mid
            else:
                right = mid - 1       # Fix: Move below mid
                
        return -1



        