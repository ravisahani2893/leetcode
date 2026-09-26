class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left=[1]*len(nums)
        left_product=1

        for i in range(len(nums)):
            left[i]=left_product
            left_product=left_product*nums[i]
            
        right_product=1
        for i in range(len(nums)-1,-1,-1):
            left[i]=right_product* left[i]
            right_product=right_product* nums[i]

        return left
