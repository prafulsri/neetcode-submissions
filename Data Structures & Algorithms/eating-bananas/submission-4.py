class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # if not piles:
        #     return 0
        # k = 1
        # while True:
        #     result = 0
        #     for num in piles:
        #         hour = (num + k - 1) // k
        #         result = result + hour
        #     if result <= h:
        #         return k
        #     k = k + 1 
        # return -1           

        left = 1
        right = max(piles) 
        ans = right 
        
        while left <= right:
            
            mid = (left + right) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
                
            
            if total_hours <= h:
                ans = mid        
                right = mid - 1  
            else:
                left = mid + 1   
                
        return ans