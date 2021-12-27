class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        glob_max, loc_max = nums[0], nums[0]
        for i, x in enumerate(nums):
            if i == 0: continue
            loc_max = max(x, loc_max+x)
            if glob_max < loc_max: glob_max = loc_max
        return glob_max
