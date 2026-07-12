class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans:List[int] = [] 
        for i in range(2): 
            ans.extend(nums)
        return ans
        