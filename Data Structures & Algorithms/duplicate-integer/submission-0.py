from functools import reduce

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        for i,num in enumerate(nums):
            if i != len(nums) -1:
                if nums[i] == nums[i+1]:
                    duplicate = True       
        return duplicate