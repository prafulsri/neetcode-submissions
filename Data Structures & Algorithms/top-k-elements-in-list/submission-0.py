class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        count = 0
        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num in seen:
                seen[curr_num] += 1
            else:
                seen[curr_num] = 1
        sorted_nums = sorted(seen, key=seen.get, reverse=True) 
        return sorted_nums[:k]
        