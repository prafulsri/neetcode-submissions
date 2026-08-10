class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_prices = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            min_prices = min(min_prices, prices[i])
            pot_prices = prices[i] - min_prices
            max_profit = max(max_profit, pot_prices)
            
        return max_profit        
        