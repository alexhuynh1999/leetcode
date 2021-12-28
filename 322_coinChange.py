class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # look up the [i - coin] value, add i, see if it adds up
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount+1):
            for coin in coins:
                if (i - coin) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        count = -1
        if dp[amount] < (amount + 1):
            count = dp[amount]
        
        return count 
            
