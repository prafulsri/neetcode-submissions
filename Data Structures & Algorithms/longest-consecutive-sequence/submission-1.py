class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uniq_nums = sorted(set(nums))
        m = len(uniq_nums)
        max_len = 1
        curr_len = 1
        for i in range(m-1):
            if uniq_nums[i] + 1 == uniq_nums[i+1]:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1    
        return max(max_len, curr_len)       


        