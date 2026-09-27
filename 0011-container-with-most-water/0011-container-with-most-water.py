class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        maxWater=0

        left=0
        right=n-1
       

        while left < right:

            minHeight = min(height[left], height[right])
            width = minHeight*(right-left)
            maxWater=max(maxWater,width)

            if height[left] < height[right]:
                left=left+1
            else:
                right=right-1
              
            
            
        return maxWater
        