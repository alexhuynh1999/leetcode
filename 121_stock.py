class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force:
        #   go through each price
        #   for each price, go through each price again and find the diff
        #   keep track of the max difference
        #   return the numbers that correlate to the max difference
        #
        #   time:  O(n^2) -> n * n
        #   space: O(1)
        
        # sorting:
        #   sort the array
        #   max difference is just end - start
        #   return end and start
        #
        #   jk that will never work
        
        # two pointer:
        #   left ptrs keeps track of min
        #   right ptr keeps track of max
        buyLow = float('inf')
        bestProfit = 0
        for price in prices:
            buyLow = min(price, buyLow)
            bestProfit = max(bestProfit, price - buyLow)
        return bestProfit
            
