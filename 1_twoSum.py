class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, n in enumerate(nums):
            complements[n] = i
        
        for i, n in enumerate(nums):
            if target - n in complements:
                if complements[target-n] == i: continue
                
                return [min(i, complements[target - n]), max(i, complements[target-n])]
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force:
        #   go through each elem in nums
        #   sum that elem with every other elem individually
        #   -> check if that equals target
        #   
        #   time:  O(n^2)
        #   space: O(1)
        
        # complements soln:
        #   go through each elem in nums
        #   find the complement to the target (elem + complement = target)
        #   store complements in a dictionary/set
        #   go through each elem in nums again
        #   check if elem is a complement in the set
        #
        #   time:  O(n)
        #   space: O(n)
        
        complements = {}
        for i, n in enumerate(nums):
            if target - n in complements: return [i, complements[target - n]]
            complements[n] = i
        return False
