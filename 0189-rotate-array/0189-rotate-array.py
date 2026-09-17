class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k% len(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        if  len(nums) == k or k==0:
            return nums

        if len(nums) == 1:
            return nums

        output=[]
        i = len(nums) - k
        while i < len(nums):
            element = nums[i]
            output.append(element)
            i=i+1
        j=0
        while j < len(nums)-k:
            output.append(nums[j])
            j=j+1
        nums[:]= output[:len(nums)]
      