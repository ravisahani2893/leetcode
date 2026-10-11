class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        result, count = 0,0
        for n in nums:
            if count == 0:
                result = n
            if n == result:
                count = count + 1
            else:
                count = count -1
        return result