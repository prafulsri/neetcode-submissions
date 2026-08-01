class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen ={}
        n = len(numbers)
        for i in range(0,n):
            num = numbers[i]
            diff = target - num
            if diff in seen:
                return [seen[diff]+1, i+1]
            seen[num] = i    
        return []