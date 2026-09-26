class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = []
        left_product = 1

        for i in range(len(nums)):
            if i == 0:
                left.append(left_product)
            else:
                left_product = left_product * nums[i - 1]
                left.append(left_product)

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_product = nums[i]
                nums[i] = left[i]
            else:
                temp = nums[i]

                nums[i] = right_product * left[i]
                right_product = right_product * temp

        return nums
