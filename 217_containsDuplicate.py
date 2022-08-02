class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen: return True
            else: seen.add(n)
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force:
        #   touch each element in nums
        #   check every element after that if it is equal
        #   time:  o(n^2)
        #   space: o(1)
        
        # faster:
        #   make a set
        #   check length of set == length of nums
        
        unique = set(nums)
        return len(unique) != len(nums)
