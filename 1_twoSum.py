class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, n in enumerate(nums):
            complements[n] = i
        
        for i, n in enumerate(nums):
            if target - n in complements:
                if complements[target-n] == i: continue
                
                return [min(i, complements[target - n]), max(i, complements[target-n])]
        
