# n^2 soln

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == (len(nums) - 1): continue
            
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        print(dp)
                
        return max(dp)

# n log n soln
      
class Solution:
    def binSearch(self, lis, val):
        lower = 0
        upper = len(lis) - 1
        idx = 10**5
        
        while lower <= upper:
            mid = int(lower + (upper - lower)/2)
                        
            if (lis[mid]) >= val:
                idx = min(idx, mid)
                upper = mid - 1
            else:
                lower = mid + 1
        
        if idx != 10**5: return idx
        return -1
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [10**5]
        for n in nums:
            idx = self.binSearch(dp, n)
            if idx == -1: dp.append(n)
            else:         dp[idx] = n
        return len(dp)
