class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplets = []
        for i in range(len(nums)-1):
            k = nums[i]
            if i > 0 and k == nums[i - 1]: continue
                
            # solve sorted two-sum
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum3 = k + nums[left] + nums[right]
                
                if sum3 > 0: right -= 1
                elif sum3 < 0: left += 1
                else: 
                    triplets.append([k, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                
        return triplets
