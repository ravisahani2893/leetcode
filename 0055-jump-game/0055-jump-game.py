class Solution:
    def canJump(self, nums: list[int]) -> bool:

        if len(nums) == 1:
            return True

        maxVal=0

        for i in range(len(nums)):

            if i > maxVal:
                return False

            maxVal = max(maxVal, i+nums[i])

            if maxVal >= len(nums) - 1:
                return True
        
        return False
        

        