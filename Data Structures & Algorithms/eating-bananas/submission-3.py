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
        # The maximum speed we ever need is the size of the biggest pile
        right = max(piles) 
        
        # Store the best successful speed we find
        ans = right 
        
        while left <= right:
            # Pick the middle speed to test
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed 'mid'
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
                
            # If we finished within h hours, this speed works!
            if total_hours <= h:
                ans = mid        # Save this working speed
                right = mid - 1  # Try to find a slower working speed on the left 
            else:
                left = mid + 1   # Too slow! We must look for a faster speed on the 
                
        return ans