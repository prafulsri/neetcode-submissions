class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
                
            seen[num] = i    
       
        