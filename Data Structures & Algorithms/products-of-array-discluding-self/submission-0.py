class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        result = 1
        for i in range(len(nums)):
            prefix[i] = result
            result = result * nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            prefix[i] *= postfix
            postfix = postfix*nums[i]
        return prefix    


        