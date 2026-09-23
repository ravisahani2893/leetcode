class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min=prices[0]
        best=0

        for price in prices[1:]:
            if price < min:
                min=price
                print("Min ", min)
            elif best < price-min:
                print("best ", price-min)
                best = price-min
        
        return best