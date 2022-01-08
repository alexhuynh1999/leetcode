class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                m = len(word)
                if i + m > len(s): continue
                
                prefix = s[i:i+m]
                if prefix == word:
                    dp[i] = dp[i+m]
                if dp[i]: break
        
        return dp[0]
