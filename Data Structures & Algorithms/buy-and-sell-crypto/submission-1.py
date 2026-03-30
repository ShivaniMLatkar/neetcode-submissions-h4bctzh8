class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        for b in range(len(prices)):
            for s in range (b+1, len(prices)):
                p = prices[s] - prices[b]
                maxx = max(maxx, p)

        return maxx
        