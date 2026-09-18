class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        allNegative= all(x < 0 for x in nums)
    
        if allNegative:
            max1=float("-inf")
            for n in nums:
                max1 = max(max1, n)
            return max1

        maxSum = nums[0]
        currentSum=0
        for n in nums:
            
            currentSum = currentSum+n

            if currentSum < 0:
                currentSum=0
            
            maxSum = max(maxSum, currentSum)
        
        return maxSum

        