class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for i, price in enumerate(prices):
            if price < low:
                low = price
                continue
            if price - low > profit:
                profit = price - low
                continue
        return profit

