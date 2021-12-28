class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            print(n, n-1)
            n &= n - 1
            count += 1
        return count
        
