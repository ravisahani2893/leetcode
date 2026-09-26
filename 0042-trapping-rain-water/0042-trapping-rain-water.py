class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        trapWater=0

        leftMax=height[0]
        rightMax=height[-1]

        while(left < right):

            if(height[left] <= height[right]):
                trapWater=trapWater+ (leftMax-height[left])
                leftMax = max(leftMax,height[left+1])
                left=left+1
            else:
                trapWater=trapWater+ (rightMax-height[right])
                rightMax = max(rightMax,height[right-1])
                right=right-1
        return trapWater
        